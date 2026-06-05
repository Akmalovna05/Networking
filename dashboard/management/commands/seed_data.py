import random
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from crm.models import Customer, Order
from erp.models import Inventory, Product
from wms.models import StockMovement, Warehouse

User = get_user_model()

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@gmail.com'
ADMIN_PASSWORD = 'Admin@2026ERP'


class Command(BaseCommand):
    help = (
        'Create a demo administrator and populate the database with sample '
        'data for CRM, ERP and WMS. Safe to run multiple times.'
    )

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Seeding demo administrator and sample data...')
        self._create_admin()
        products = self._seed_erp()
        customers = self._seed_crm()
        self._seed_wms(products)
        self.stdout.write(self.style.SUCCESS('Demo data created successfully.'))
        self.stdout.write(self.style.SUCCESS(
            f'Login -> username: {ADMIN_USERNAME} | password: {ADMIN_PASSWORD}'
        ))

    def _create_admin(self):
        """Create the demo admin, or update password/email if it exists."""
        user, created = User.objects.get_or_create(username=ADMIN_USERNAME)
        user.email = ADMIN_EMAIL
        user.is_staff = True
        user.is_superuser = True
        user.set_password(ADMIN_PASSWORD)
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS('Created admin user.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user existed - password and email updated.'))

    def _seed_erp(self):
        """Create 30 products, each with an inventory record."""
        products = []
        for i in range(1, 31):
            sku = f'SKU-{i:04d}'
            product, _ = Product.objects.get_or_create(
                sku=sku,
                defaults={
                    'name': f'Product {i}',
                    'description': f'Demo product number {i}.',
                    'price': Decimal(f'{random.randint(5, 2000)}.{random.randint(0, 99):02d}'),
                },
            )
            products.append(product)
            Inventory.objects.get_or_create(
                product=product,
                defaults={
                    'quantity': random.randint(0, 500),
                    'reorder_level': random.choice([10, 20, 50]),
                },
            )
        self.stdout.write(f'  ERP: {len(products)} products + inventory records.')
        return products

    def _seed_crm(self):
        """Create 10 customers and 20 orders distributed among them."""
        companies = [
            'Acme Corporation', 'Globex LLC', 'Initech', 'Umbrella Co',
            'Stark Industries', 'Wayne Enterprises', 'Wonka Inc', 'Hooli',
            'Soylent Corp', 'Vandelay Industries',
        ]
        customers = []
        for i, company in enumerate(companies, start=1):
            customer, _ = Customer.objects.get_or_create(
                name=f'Customer {i}',
                defaults={
                    'email': f'customer{i}@example.com',
                    'phone': f'555-01{i:02d}',
                    'company': company,
                    'address': f'{i} Business Park, Suite {i * 10}',
                },
            )
            customers.append(customer)

        statuses = ['pending', 'processing', 'completed', 'cancelled']
        for i in range(1, 21):
            reference = f'ORD-{i:04d}'
            Order.objects.get_or_create(
                reference=reference,
                defaults={
                    'customer': random.choice(customers),
                    'total_amount': Decimal(f'{random.randint(50, 9999)}.{random.randint(0, 99):02d}'),
                    'status': random.choice(statuses),
                },
            )
        self.stdout.write(f'  CRM: {len(customers)} customers + 20 orders.')
        return customers

    def _seed_wms(self, products):
        """Create 3 warehouses and stock movement records."""
        warehouses_data = [
            ('Central Warehouse', 'WH-CEN', 'New York, NY', 10000),
            ('West Coast Depot', 'WH-WST', 'Los Angeles, CA', 6000),
            ('Midwest Hub', 'WH-MID', 'Chicago, IL', 8000),
        ]
        warehouses = []
        for name, code, location, capacity in warehouses_data:
            warehouse, _ = Warehouse.objects.get_or_create(
                code=code,
                defaults={'name': name, 'location': location, 'capacity': capacity},
            )
            warehouses.append(warehouse)

        movement_types = ['in', 'out', 'transfer']
        notes = ['Initial stock', 'Sales order', 'Restock', 'Transfer between sites', 'Adjustment']
        created = 0
        if products and not StockMovement.objects.exists():
            for _ in range(30):
                StockMovement.objects.create(
                    warehouse=random.choice(warehouses),
                    product=random.choice(products),
                    movement_type=random.choice(movement_types),
                    quantity=random.randint(1, 200),
                    note=random.choice(notes),
                )
                created += 1
        self.stdout.write(f'  WMS: {len(warehouses)} warehouses + {created} stock movements.')
