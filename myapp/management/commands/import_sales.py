import csv 
from django.core.management.base import BaseCommand 
from myapp.models import SalesData

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(r'C:\Users\swamy\OneDrive\Desktop\sales_data.csv')

    def handle(self, *args, **kwargs):
        file_path = kwargs[r'C:\Users\swamy\OneDrive\Desktop\sales_data.csv']
        try:
            with open(file_path,"r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    product_name = row['PRODUCTLINE']
                    quantity = int(row['QUANTITYORDERED'])
                    price = float(row['PRICEEACH'])
                    SalesData.objects.create(product=product_name,quantity = quantity,price = price)
                self.stdout.write(self.style.SUCCESS('Data imported Successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found:{file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error:{e}'))