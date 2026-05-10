
from django.core.management.base import BaseCommand
from faker import Faker
from casi.journals.models import Journal

fake = Faker()


class Command(BaseCommand):
    help = "2000 ta test journal yaratadi"

    def handle(self, *args, **kwargs):
        descriptions = [
            "International journal of science",
            "Medical research journal",
            "Biology and chemistry journal",
            "Physics and mathematics journal",
            "Computer science journal",
        ]

        journals = [
            Journal(
                name=f"{fake.company()} Journal {i}",
                description=fake.random_element(descriptions),
                slug=f"journal-{i}-{fake.uuid4()}"  # ← unique slug
            )
            for i in range(2000)
        ]
        Journal.objects.bulk_create(journals, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("✅ 2000 ta journal yaratildi!"))
