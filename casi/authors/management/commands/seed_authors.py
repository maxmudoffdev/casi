# authors/management/commands/benchmark_authors.py
import time
from django.core.management.base import BaseCommand
from faker import Faker
from casi.authors.models import Author

fake = Faker()


class Command(BaseCommand):
    help = "1000 ta author — create vs bulk_create solishtirish"

    def handle(self, *args, **kwargs):
        affiliations = [
            "Massachusetts Institute of Technology",
            "Harvard University",
            "Stanford University",
            "National University of Uzbekistan",
            "Oxford University",
        ]

        # --- 1. create() ---
        self.stdout.write("create() boshlandi...")
        start = time.time()

        for i in range(1000):
            Author.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                affiliation=fake.random_element(affiliations),
                email=fake.unique.email(),
            )

        create_time = time.time() - start
        self.stdout.write(self.style.WARNING(f"create()      → {create_time:.2f} sekund"))

        # --- 2. bulk_create() ---
        self.stdout.write("bulk_create() boshlandi...")
        start = time.time()

        authors = [
            Author(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                affiliation=fake.random_element(affiliations),
                email=fake.unique.email(),
            )
            for _ in range(1000)
        ]
        Author.objects.bulk_create(authors)

        bulk_time = time.time() - start
        self.stdout.write(self.style.WARNING(f"bulk_create() → {bulk_time:.2f} sekund"))

        # --- Natija ---
        self.stdout.write(
            self.style.SUCCESS(
                f"\nbulk_create {create_time / bulk_time:.1f}x tez!"
            )
        )
