import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = "Wait for the database to accept connection"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]

                with db_conn.cursor():
                    pass

            except OperationalError:
                self.stdout.write(self.style.WARNING("Database unavailable, waiting 1 second..."))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))