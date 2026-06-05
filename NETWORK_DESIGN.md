# Network Design — Cloud ERP Platform

> BTEC Unit 6: Cloud & Networking — Network Architecture Document
> Application: Cloud ERP Platform (CRM + ERP + WMS) built on Django

This document describes the target cloud network design that hosts the Django
CRM/ERP/WMS platform. It covers the Virtual Private Cloud (VPC), public and
private subnets, routing, gateways, DNS, load balancing and VPN connectivity,
and shows how the three business modules map onto the infrastructure.

---

## 1. Design Goals

| Goal | Description |
|------|-------------|
| Security | Application and database tiers isolated in private subnets, no direct internet exposure. |
| High availability | Resources spread across two Availability Zones (AZs). |
| Scalability | Application tier sits behind a load balancer in an Auto Scaling Group. |
| Controlled egress | Private resources reach the internet only through a NAT Gateway. |
| Hybrid access | Corporate office connected via a site-to-site VPN for admin/back-office traffic. |

---

## 2. VPC Architecture

The platform runs inside a single **VPC** with CIDR block `10.0.0.0/16`,
spanning two Availability Zones for resilience. Each AZ contains one public and
one private subnet.

| Component | CIDR | AZ | Purpose |
|-----------|------|----|---------|
| VPC | `10.0.0.0/16` | Region | Overall isolated network boundary |
| Public Subnet A | `10.0.1.0/24` | az-a | Load balancer, NAT GW, bastion |
| Public Subnet B | `10.0.2.0/24` | az-b | Load balancer (HA) |
| Private Subnet A | `10.0.11.0/24` | az-a | Django app servers (CRM/ERP/WMS) |
| Private Subnet B | `10.0.12.0/24` | az-b | Django app servers (HA) |
| DB Subnet A | `10.0.21.0/24` | az-a | Primary database |
| DB Subnet B | `10.0.22.0/24` | az-b | Standby database |

```mermaid
graph TB
    Internet((Internet))
    IGW[Internet Gateway]
    Internet --> IGW

    subgraph VPC["VPC 10.0.0.0/16"]
        IGW --> ALB

        subgraph AZA["Availability Zone A"]
            subgraph PubA["Public Subnet 10.0.1.0/24"]
                ALB[Application Load Balancer]
                NAT[NAT Gateway]
                Bastion[Bastion Host]
            end
            subgraph PrivA["Private Subnet 10.0.11.0/24"]
                App1[Django App Server 1]
            end
            subgraph DBA["DB Subnet 10.0.21.0/24"]
                DB1[(Primary DB)]
            end
        end

        subgraph AZB["Availability Zone B"]
            subgraph PubB["Public Subnet 10.0.2.0/24"]
                ALB2[ALB Node]
            end
            subgraph PrivB["Private Subnet 10.0.12.0/24"]
                App2[Django App Server 2]
            end
            subgraph DBB["DB Subnet 10.0.22.0/24"]
                DB2[(Standby DB)]
            end
        end

        ALB --> App1
        ALB --> App2
        App1 --> DB1
        App2 --> DB1
        DB1 -. replication .-> DB2
        App1 --> NAT
        App2 --> NAT
        NAT --> IGW
    end
```

---

## 3. Public Subnet

The public subnets host only internet-facing or egress components:

- **Application Load Balancer (ALB)** — receives HTTPS traffic from users.
- **NAT Gateway** — provides outbound internet access for private resources.
- **Bastion Host** — controlled SSH entry point for administration.

Public subnets have a route to the **Internet Gateway** (`0.0.0.0/0 → IGW`),
which is what makes them "public". No application or database servers live here.

## 4. Private Subnet

The private subnets host the workload that must never be reached directly from
the internet:

- **Django application servers** running the CRM, ERP and WMS modules
  (Gunicorn/uWSGI behind the ALB).
- **Database subnets** hold the managed relational database (primary + standby).

Private subnets route outbound traffic (`0.0.0.0/0`) to the **NAT Gateway**, so
servers can pull OS/package/security updates without being publicly addressable.

---

## 5. Route Tables

```mermaid
graph LR
    subgraph PublicRT["Public Route Table"]
        P1["10.0.0.0/16 -> local"]
        P2["0.0.0.0/0 -> IGW"]
    end
    subgraph PrivateRT["Private Route Table"]
        R1["10.0.0.0/16 -> local"]
        R2["0.0.0.0/0 -> NAT Gateway"]
    end
    subgraph DBRT["DB Route Table"]
        D1["10.0.0.0/16 -> local"]
    end
```

| Route Table | Destination | Target | Attached Subnets |
|-------------|-------------|--------|------------------|
| Public RT | `10.0.0.0/16` | local | Public A, Public B |
| Public RT | `0.0.0.0/0` | Internet Gateway | Public A, Public B |
| Private RT | `10.0.0.0/16` | local | Private A, Private B |
| Private RT | `0.0.0.0/0` | NAT Gateway | Private A, Private B |
| DB RT | `10.0.0.0/16` | local | DB A, DB B |

The DB route table has **no default route** — the database tier cannot reach or
be reached from the internet at all.

---

## 6. Internet Gateway (IGW)

The Internet Gateway is attached to the VPC and is the only component that
provides bidirectional internet connectivity. It is referenced by the public
route table and is used by:

- The ALB to accept inbound user traffic.
- The NAT Gateway to forward private subnet egress traffic outward.

## 7. NAT Gateway

The NAT Gateway lives in a public subnet and allows private subnet resources to
initiate **outbound-only** connections to the internet (package updates, API
calls, license checks). Inbound connections initiated from the internet to
private resources are not possible through the NAT Gateway.

```mermaid
sequenceDiagram
    participant App as Django App (Private)
    participant NAT as NAT Gateway (Public)
    participant IGW as Internet Gateway
    participant Ext as External Service

    App->>NAT: Outbound request (e.g. pip update)
    NAT->>IGW: Source NAT translation
    IGW->>Ext: Forward request
    Ext-->>IGW: Response
    IGW-->>NAT: Response
    NAT-->>App: Response (inbound from internet blocked)
```

---

## 8. DNS

DNS provides name resolution for both public users and internal services.

| Layer | Mechanism | Example |
|-------|-----------|---------|
| Public DNS | Hosted zone / public records | `erp.example.com → ALB` |
| Internal DNS | Private hosted zone | `db.internal → primary DB` |
| Health-based routing | DNS health checks / failover records | Fails over to standby region |
| VPC DNS | Built-in resolver | EC2/private resource resolution |

```mermaid
graph LR
    User((User)) -->|erp.example.com| DNS[DNS Resolver]
    DNS -->|A / Alias record| ALB[Application Load Balancer]
    ALB --> App[Django App Servers]
    App -->|db.internal| PDNS[Private Hosted Zone]
    PDNS --> DB[(Database)]
```

---

## 9. Load Balancer

An **Application Load Balancer (Layer 7)** distributes inbound HTTPS traffic
across the Django application servers in both AZs. It terminates TLS, performs
health checks, and routes by path if needed (e.g. `/crm`, `/erp`, `/wms`).

```mermaid
graph TB
    Users((Users)) -->|HTTPS 443| ALB[Application Load Balancer]
    ALB -->|Health Check /| TG[Target Group]
    TG --> App1[App Server 1 - AZ A]
    TG --> App2[App Server 2 - AZ B]
    App1 --> DB[(Database)]
    App2 --> DB
```

| Feature | Configuration |
|---------|---------------|
| Listener | HTTPS:443 (TLS termination), HTTP:80 → redirect to 443 |
| Health check | `GET /login/` expecting HTTP 200/302 |
| Algorithm | Round robin / least outstanding requests |
| Stickiness | Cookie-based session affinity (optional) |
| Cross-zone | Enabled for even distribution |

---

## 10. VPN Connectivity

A **site-to-site VPN** connects the corporate office to the VPC over an IPsec
tunnel, allowing back-office staff to reach internal admin tooling and the
database management interface without exposing them publicly.

```mermaid
graph LR
    subgraph Office["Corporate Office 192.168.0.0/16"]
        CGW[Customer Gateway / On-Prem Router]
        Admin[Back-office Staff]
    end
    subgraph Cloud["VPC 10.0.0.0/16"]
        VGW[Virtual Private Gateway]
        Priv[Private Subnet - App/Admin]
        DBnet[(Database)]
    end
    Admin --> CGW
    CGW == IPsec Tunnel ==> VGW
    VGW --> Priv
    Priv --> DBnet
```

| Element | Description |
|---------|-------------|
| Customer Gateway | On-premise router/firewall public endpoint |
| Virtual Private Gateway | VPC-side VPN endpoint |
| Tunnels | Two redundant IPsec tunnels for HA |
| Routing | Static or BGP routes for `192.168.0.0/16 ↔ 10.0.0.0/16` |
| Use case | Admin access, DB management, internal reporting |

---

## 11. ERP, CRM and WMS Architecture

All three Django modules are deployed as part of the same application image but
are logically separated by URL namespace and database models. They share the
application tier and database, communicating internally over private subnets.

```mermaid
graph TB
    subgraph Client["Client Layer"]
        Browser[Web Browser]
    end
    subgraph Edge["Edge Layer - Public Subnet"]
        ALB[Application Load Balancer]
    end
    subgraph AppTier["Application Tier - Private Subnet"]
        Dashboard[Dashboard Module]
        CRM[CRM Module<br/>Customers / Orders]
        ERP[ERP Module<br/>Products / Inventory]
        WMS[WMS Module<br/>Warehouses / Stock]
        Auth[Authentication]
    end
    subgraph DataTier["Data Tier - DB Subnet"]
        DB[(Relational Database)]
    end

    Browser -->|HTTPS| ALB
    ALB --> Dashboard
    ALB --> Auth
    Dashboard --> CRM
    Dashboard --> ERP
    Dashboard --> WMS
    CRM --> DB
    ERP --> DB
    WMS --> DB
    WMS -. references products .-> ERP
    CRM -. order totals .-> ERP
```

### Module interaction summary

| Module | Core models | Depends on | Network path |
|--------|-------------|-----------|--------------|
| CRM | `Customer`, `Order` | Shared DB | ALB → App → DB |
| ERP | `Product`, `Inventory` | Shared DB | ALB → App → DB |
| WMS | `Warehouse`, `StockMovement` | ERP `Product` (FK) | ALB → App → DB |
| Dashboard | aggregates counts | CRM/ERP/WMS | ALB → App → DB |

The **WMS `StockMovement` model references the ERP `Product` model**, which is
why the two modules are shown as integrated in the diagram. The CRM order
totals conceptually relate to ERP product pricing.

---

## 12. Summary

The design isolates the application and data tiers in private subnets, exposes
only the load balancer publicly, routes private egress through a NAT Gateway,
provides resilient DNS and VPN access, and spreads resources across two AZs for
high availability. This forms the foundation for the security and optimization
strategies documented in `INFRASTRUCTURE_SECURITY.md` and
`TECH_OPTIMIZATION.md`.
