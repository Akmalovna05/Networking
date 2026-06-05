# Screenshot Guide

> Evidence capture checklist for the Cloud ERP Platform (BTEC Unit 6 submission).

Capture each screenshot below and save it into `docs/screenshots/` using the
exact filename shown. These filenames match the links used in `README.md`.

## Before you start

1. Run the project:

```bash
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

2. Log in with **admin / Admin@2026ERP**.
3. Use a clean browser window (no unrelated tabs/extensions visible).
4. Capture full-page where possible; PNG format; readable resolution.

---

## Capture Checklist

| # | Screen | URL | Save as | What must be visible | Done |
|---|--------|-----|---------|----------------------|------|
| 1 | Login page | `/login/` | `login.png` | Login form with username/password fields | ☐ |
| 2 | Dashboard | `/` | `dashboard.png` | CRM, ERP, WMS cards with counts | ☐ |
| 3 | CRM Customers | `/crm/customers/` | `crm_customers.png` | Customer table (10 demo rows) | ☐ |
| 4 | CRM Customer detail | `/crm/customers/1/` | `crm_customer_detail.png` | Customer info + their orders | ☐ |
| 5 | CRM Orders | `/crm/orders/` | `crm_orders.png` | Order table (20 demo rows) with statuses | ☐ |
| 6 | ERP Products | `/erp/products/` | `erp_products.png` | Product table (30 demo rows) | ☐ |
| 7 | ERP Inventory | `/erp/inventory/` | `erp_inventory.png` | Inventory with quantity + reorder status | ☐ |
| 8 | WMS Warehouses | `/wms/warehouses/` | `wms_warehouses.png` | Warehouse table (3 demo rows) | ☐ |
| 9 | WMS Stock Movements | `/wms/movements/` | `wms_movements.png` | Movement table with in/out/transfer types | ☐ |
| 10 | Django Admin | `/admin/` | `admin.png` | Admin index listing CRM/ERP/WMS models | ☐ |
| 11 | Database records | `/admin/crm/customer/` (or any model) | `database_records.png` | List of stored records proving data persists | ☐ |

---

## Detailed checklist by area

### Authentication evidence
- [ ] `login.png` — login page renders with Bootstrap styling
- [ ] (optional) failed login showing the "Invalid username or password" alert
- [ ] Logout button visible in the navbar after login

### Dashboard evidence
- [ ] `dashboard.png` — three module cards (CRM / ERP / WMS)
- [ ] Live counts displayed on each card

### CRM evidence
- [ ] `crm_customers.png` — customer list populated
- [ ] `crm_customer_detail.png` — single customer with related orders
- [ ] `crm_orders.png` — order list with reference, customer, amount, status

### ERP evidence
- [ ] `erp_products.png` — product list populated
- [ ] `erp_inventory.png` — inventory list with OK / Reorder badges

### WMS evidence
- [ ] `wms_warehouses.png` — warehouse list populated
- [ ] `wms_movements.png` — stock movements with types and quantities

### Admin & database evidence
- [ ] `admin.png` — admin home showing all registered models
- [ ] `database_records.png` — a model changelist proving stored records

---

## Tips

- Take screenshots **after** running `seed_data` so tables are populated.
- For the database evidence you can use the Django admin changelist (proves the
  ORM persisted records) or a DB browser viewing `db.sqlite3`.
- Keep image widths reasonable (~1200–1600px) for clear printing in the report.
