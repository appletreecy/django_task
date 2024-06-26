import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from trading.models import Stock, Trade


class Command(BaseCommand):
    help = 'Process bulk trades from a CSV file in a specified directory'

    def handle(self, *args, **options):
        # Directory where the CSV file is located, relative to the project directory
        csv_directory = os.path.join(settings.BASE_DIR, 'trading_system')

        # Specify the filename
        csv_filename = 'bulk_trades.csv'

        print(csv_directory)

        # Path to the CSV file
        csv_file_path = os.path.join(csv_directory, csv_filename)

        print(csv_file_path)

        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR('CSV file does not exist'))
            return

        # Process the CSV file
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    user = User.objects.get(username=row['username'])
                    stock = Stock.objects.get(name=row['stock'])
                    Trade.objects.create(
                        user=user,
                        stock=stock,
                        quantity=int(row['quantity']),
                        trade_type=row['trade_type'].upper()
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f"Error processing row {row}: {e}"))

        # Optionally, remove the file after processing
        os.remove(csv_file_path)

        self.stdout.write(self.style.SUCCESS(
            'Successfully processed bulk trades'))
