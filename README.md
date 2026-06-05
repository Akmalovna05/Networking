# Cloud ERP Platform

A cloud-oriented business platform built with **Django**, combining three
integrated modules — **CRM**, **ERP** and **WMS** — behind a single dashboard
with authentication and a Bootstrap 5 responsive interface.

This repository also contains the **BTEC Unit 6 (Cloud & Networking)**
documentation set: network design, cloud strategy, infrastructure security,
optimisation and the final evaluation report, plus Mermaid architecture
diagrams.

---

## Project Features

- **CRM** — Customer management (list + detail) and Orders.
- **ERP** — Products and Inventory with reorder indicators.
- **WMS** — Warehouses and Stock Movements (linked to ERP products).
- **Dashboard** — Cards summarising CRM / ERP / WMS with live counts.
- **Authentication** — Login / logout, all module views protected.
- **Admin panel** — All models registered and manageable.
- **Sample data command** — One command to seed demo data and an admin user.
- **Bootstrap 5 UI** — Responsive layout with navigation menu.

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Django (Python) |
| Database | SQLite (dev) / managed SQL (prod) |
| Frontend | Bootstrap 5 + Bootstrap Icons (CDN) |
| Auth | Django authentication framework |

---

## Project Structure

```
Networking/
├── cloud_erp_platform/      # Project settings, root URLs
├── users/                   # Authentication (login/logout)
├── dashboard/               # Dashboard + sample data command
├── crm/                     # Customer, Order
├── erp/                     # Product, Inventory
├── wms/                     # Warehouse, StockMovement
├── templates/               # Bootstrap 5 templates
├── static/                  # Custom CSS
├── diagrams/                # Mermaid architecture diagrams (01–07)
├── docs/screenshots/        # Evidence screenshots
├── NETWORK_DESIGN.md
├── CLOUD_STRATEGY.md
├── INFRASTRUCTURE_SECURITY.md
├── TECH_OPTIMIZATION.md
├── FINAL_MISSION_REPORT.md
├── PROJECT_STRUCTURE.md
├── DEPLOYMENT_GUIDE.md
├── TESTING_REPORT.md
├── SCREENSHOT_GUIDE.md
├── ASSESSMENT_CHECKLIST.md
└── README.md
```

For a full breakdown of apps, models, URLs, templates and static files, see
[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

---

## Installation

Requirements: Python 3.x and Django installed (a virtual environment is
recommended).

```bash
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> and log in with **admin / Admin@2026ERP**.

> `seed_data` creates the demo administrator automatically — no
> `createsuperuser` prompt is required.

### Load demo admin + sample data (no manual input)

You do **not** need to run `createsuperuser`. The `seed_data` command
automatically creates a demo administrator and populates demo data:

```bash
python manage.py seed_data
```

After running, log in with:

| Field | Value |
|-------|-------|
| Username | `admin` |
| Email | `admin@gmail.com` |
| Password | `Admin@2026ERP` |

If the `admin` user already exists, the command updates its password and email
instead of failing. It is safe to run multiple times.

**Demo data generated:**

| Module | Records |
|--------|---------|
| CRM | 10 customers, 20 orders |
| ERP | 30 products + inventory records |
| WMS | 3 warehouses + stock movement records |

### Verify the project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py runserver
```

---

## Key URLs

| URL | Description |
|-----|-------------|
| `/` | Dashboard (login required) |
| `/login/` | Login page |
| `/logout/` | Logout (POST) |
| `/crm/customers/` | Customer list |
| `/crm/customers/<id>/` | Customer detail |
| `/crm/orders/` | Order list |
| `/erp/products/` | Product list |
| `/erp/inventory/` | Inventory list |
| `/wms/warehouses/` | Warehouse list |
| `/wms/movements/` | Stock movement list |
| `/admin/` | Django admin panel |

---

## Evidence

This project is submitted as BTEC Unit 6 evidence. The evidence consists of:

| Evidence type | Where |
|---------------|-------|
| Working application | Django apps: `users`, `dashboard`, `crm`, `erp`, `wms` |
| Source structure reference | [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) |
| Architecture diagrams | [diagrams/](diagrams/) (7 Mermaid diagrams) |
| Screenshots | [docs/screenshots/](docs/screenshots/) — capture using [SCREENSHOT_GUIDE.md](SCREENSHOT_GUIDE.md) |
| Demo admin + data | `python manage.py seed_data` |
| Testing evidence | [TESTING_REPORT.md](TESTING_REPORT.md) |
| Deployment evidence | [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) |
| Criterion mapping | [ASSESSMENT_CHECKLIST.md](ASSESSMENT_CHECKLIST.md) |

---

## Screenshots

> Placeholders — capture real images once the server is running
> (`python manage.py runserver`) and save them into `docs/screenshots/` using
> the filenames below. Follow the [Screenshot Guide](SCREENSHOT_GUIDE.md).

### Login

![Login page](docs/screenshots/login.png)

### Dashboard

![Dashboard with CRM / ERP / WMS cards](docs/screenshots/dashboard.png)

### CRM — Customer List

![Customer list](docs/screenshots/crm_customers.png)

### CRM — Customer Detail

![Customer detail with orders](docs/screenshots/crm_customer_detail.png)

### CRM — Orders

![Order list](docs/screenshots/crm_orders.png)

### ERP — Products

![Product list](docs/screenshots/erp_products.png)

### ERP — Inventory

![Inventory list](docs/screenshots/erp_inventory.png)

### WMS — Warehouses

![Warehouse list](docs/screenshots/wms_warehouses.png)

### WMS — Stock Movements

![Stock movements](docs/screenshots/wms_movements.png)

### Admin Panel

![Django admin](docs/screenshots/admin.png)

### Database Records

![Database records](docs/screenshots/database_records.png)

---

## Documentation Index

| Document | Purpose |
|----------|---------|
| [NETWORK_DESIGN.md](NETWORK_DESIGN.md) | VPC, subnets, routing, gateways, DNS, LB, VPN, module architecture |
| [CLOUD_STRATEGY.md](CLOUD_STRATEGY.md) | Cloud architectures, standards, communication, performance (A criteria) |
| [INFRASTRUCTURE_SECURITY.md](INFRASTRUCTURE_SECURITY.md) | VPN, firewall, IAM, security groups, NACLs, encryption |
| [TECH_OPTIMIZATION.md](TECH_OPTIMIZATION.md) | Auto scaling, LB, CDN, CI/CD, monitoring (D.P8) |
| [FINAL_MISSION_REPORT.md](FINAL_MISSION_REPORT.md) | Testing, comparison, evaluation (D.P7, D.M4, D.D3) |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Folder structure, apps, models, URLs, templates, static |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | Local + production deployment, security, backups |
| [DEPLOY_AWS_EC2.md](DEPLOY_AWS_EC2.md) | Step-by-step AWS EC2 deployment (Gunicorn + Nginx + HTTPS) |
| [TESTING_REPORT.md](TESTING_REPORT.md) | Functional, auth, CRM/ERP/WMS, performance tests |
| [SCREENSHOT_GUIDE.md](SCREENSHOT_GUIDE.md) | Evidence screenshot capture checklist |
| [ASSESSMENT_CHECKLIST.md](ASSESSMENT_CHECKLIST.md) | Full criterion-to-evidence mapping |
| [diagrams/](diagrams/) | 7 Mermaid architecture diagrams |

### Diagrams

| File | Diagram |
|------|---------|
| [01_cloud_architecture.md](diagrams/01_cloud_architecture.md) | Cloud Architecture |
| [02_network_topology.md](diagrams/02_network_topology.md) | Network Topology |
| [03_vpn_architecture.md](diagrams/03_vpn_architecture.md) | VPN Architecture |
| [04_load_balancer_architecture.md](diagrams/04_load_balancer_architecture.md) | Load Balancer Architecture |
| [05_auto_scaling_workflow.md](diagrams/05_auto_scaling_workflow.md) | Auto Scaling Workflow |
| [06_cicd_workflow.md](diagrams/06_cicd_workflow.md) | CI/CD Workflow |
| [07_erp_crm_wms_integration.md](diagrams/07_erp_crm_wms_integration.md) | ERP / CRM / WMS Integration |

---

## BTEC Unit 6 — Criterion Mapping

Each criterion below is mapped to where the evidence is satisfied.

| Criterion | Description | Evidence location |
|-----------|-------------|-------------------|
| **A.P1** | Explain cloud networking architectures | `CLOUD_STRATEGY.md` §1–2 |
| **A.M1** | Assess architectures/standards for performance & communication | `CLOUD_STRATEGY.md` §5 |
| **A.D1** | Evaluate & justify the cloud networking solution | `CLOUD_STRATEGY.md` §6 |
| **A.P2** | Explain networking standards & protocols | `CLOUD_STRATEGY.md` §3–4 |
| **B.P3** | Design a cloud network solution to requirements | `NETWORK_DESIGN.md` §1–11; `diagrams/01,02` |
| **B.P4** | Produce network design diagrams & addressing | `NETWORK_DESIGN.md` §2,§5; `diagrams/02_network_topology.md` |
| **B.M2** | Justify design decisions against requirements | `NETWORK_DESIGN.md` §12; `CLOUD_STRATEGY.md` §6 |
| **C.P5** | Configure/implement the cloud network & services | `PROJECT_STRUCTURE.md`; Django apps + `settings.py`; `NETWORK_DESIGN.md` §11 |
| **C.P6** | Implement security on the cloud network | `INFRASTRUCTURE_SECURITY.md` §2–7 |
| **C.M3** | Configure security to protect the infrastructure | `INFRASTRUCTURE_SECURITY.md` §4–8 |
| **C.D2** | Evaluate the implemented & secured solution | `INFRASTRUCTURE_SECURITY.md` §9; `FINAL_MISSION_REPORT.md` §6 |
| **D.P7** | Test the cloud network for performance & functionality | `TESTING_REPORT.md`; `FINAL_MISSION_REPORT.md` §2–3 |
| **D.P8** | Optimise the network for performance & scalability | `TECH_OPTIMIZATION.md` (all) |
| **D.M4** | Analyse results & recommend improvements | `FINAL_MISSION_REPORT.md` §3–5; `TESTING_REPORT.md` §10 |
| **D.D3** | Evaluate & justify the optimised solution | `FINAL_MISSION_REPORT.md` §6–7 |

> Full criterion-to-section mapping: [ASSESSMENT_CHECKLIST.md](ASSESSMENT_CHECKLIST.md).

---

## Notes

- Bootstrap and icons load from a CDN, so styling requires an internet
  connection when viewing the running app.
- `DEBUG = True` and the bundled `SECRET_KEY` are for development only; see the
  hardening checklist in `INFRASTRUCTURE_SECURITY.md` before any production use.
