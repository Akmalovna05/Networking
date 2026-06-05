# Assessment Checklist

> BTEC Unit 6: Cloud & Networking — criterion-to-evidence mapping for the
> Cloud ERP Platform (CRM + ERP + WMS).

This checklist maps **every assessment criterion** to the exact file and
section that satisfies it.

---

## Learning Aim A — Cloud networking architectures & standards

| Criterion | Description | Evidence file | Section |
|-----------|-------------|---------------|---------|
| **A.P1** | Explain cloud networking architectures and how they support an organisation | `CLOUD_STRATEGY.md` | §1 Cloud Networking Architectures; §2 Service Models |
| **A.P2** | Explain networking standards and protocols used in cloud communication | `CLOUD_STRATEGY.md` | §3 Networking Standards; §4 Cloud Communication |
| **A.M1** | Assess how architectures and standards support performance and communication | `CLOUD_STRATEGY.md` | §5 Impact on Performance |
| **A.D1** | Evaluate and justify the cloud networking solution for the organisation | `CLOUD_STRATEGY.md` | §6 Evaluation and Justification |

---

## Learning Aim B — Design a cloud network

| Criterion | Description | Evidence file | Section |
|-----------|-------------|---------------|---------|
| **B.P3** | Design a cloud network solution that meets requirements | `NETWORK_DESIGN.md` | §1–§11 (VPC, subnets, gateways, LB, VPN, modules) |
| **B.P4** | Produce network design diagrams and addressing scheme | `NETWORK_DESIGN.md` §2,§5 + `diagrams/02_network_topology.md`, `diagrams/01_cloud_architecture.md` | VPC table, route tables, topology diagram |
| **B.M2** | Justify design decisions against requirements | `NETWORK_DESIGN.md` §12 + `CLOUD_STRATEGY.md` §6 | Summary + Justification |

---

## Learning Aim C — Implement & secure the cloud network

| Criterion | Description | Evidence file | Section |
|-----------|-------------|---------------|---------|
| **C.P5** | Configure/implement the cloud network and services | `PROJECT_STRUCTURE.md` (apps, models, URLs, settings) + `NETWORK_DESIGN.md` §11 + Django source code | §2–§7; module architecture |
| **C.P6** | Implement security on the cloud network | `INFRASTRUCTURE_SECURITY.md` | §2 VPN, §3 Firewall, §4 IAM, §5 Security Groups, §6 NACLs, §7 Encryption |
| **C.M3** | Configure security to protect the infrastructure | `INFRASTRUCTURE_SECURITY.md` | §4–§8 + Django hardening checklist |
| **C.D2** | Evaluate the implemented and secured solution | `INFRASTRUCTURE_SECURITY.md` §9 + `FINAL_MISSION_REPORT.md` §6 + `TESTING_REPORT.md` | Security summary; evaluation |

---

## Learning Aim D — Test & optimise the cloud network

| Criterion | Description | Evidence file | Section |
|-----------|-------------|---------------|---------|
| **D.P7** | Test the cloud network for performance and functionality | `TESTING_REPORT.md` + `FINAL_MISSION_REPORT.md` §2–§3 | Functional/auth/module/performance tests |
| **D.P8** | Optimise the network for performance and scalability | `TECH_OPTIMIZATION.md` | §1 Auto Scaling, §2 LB, §3 CDN, §4 CI/CD, §5 Monitoring, §6 Network Optimisation |
| **D.M4** | Analyse test results and recommend improvements | `FINAL_MISSION_REPORT.md` §3–§5 + `TESTING_REPORT.md` §10 | Analysis + recommendations |
| **D.D3** | Evaluate and justify the optimised solution | `FINAL_MISSION_REPORT.md` §6–§7 | Final evaluation + business justification |

---

## Full Coverage Summary

| Criterion | Covered | Primary file |
|-----------|---------|--------------|
| A.P1 | ✅ | `CLOUD_STRATEGY.md` |
| A.M1 | ✅ | `CLOUD_STRATEGY.md` |
| A.D1 | ✅ | `CLOUD_STRATEGY.md` |
| A.P2 | ✅ | `CLOUD_STRATEGY.md` |
| B.P3 | ✅ | `NETWORK_DESIGN.md` |
| B.P4 | ✅ | `NETWORK_DESIGN.md` + `diagrams/` |
| B.M2 | ✅ | `NETWORK_DESIGN.md` |
| C.P5 | ✅ | `PROJECT_STRUCTURE.md` + source |
| C.P6 | ✅ | `INFRASTRUCTURE_SECURITY.md` |
| C.M3 | ✅ | `INFRASTRUCTURE_SECURITY.md` |
| C.D2 | ✅ | `INFRASTRUCTURE_SECURITY.md` + `FINAL_MISSION_REPORT.md` |
| D.P7 | ✅ | `TESTING_REPORT.md` |
| D.P8 | ✅ | `TECH_OPTIMIZATION.md` |
| D.M4 | ✅ | `FINAL_MISSION_REPORT.md` |
| D.D3 | ✅ | `FINAL_MISSION_REPORT.md` |

**15 / 15 criteria covered.**

---

## Supporting Evidence

| Evidence | Location |
|----------|----------|
| Working application | Django apps `users`, `dashboard`, `crm`, `erp`, `wms` |
| Screenshots | `docs/screenshots/` (see `SCREENSHOT_GUIDE.md`) |
| Architecture diagrams | `diagrams/01`–`07` (Mermaid) |
| Demo data + admin | `dashboard/management/commands/seed_data.py` |
| Project reference | `PROJECT_STRUCTURE.md` |
| Deployment | `DEPLOYMENT_GUIDE.md` |
| Testing | `TESTING_REPORT.md` |
