from django.core.management.base import BaseCommand
from myapp.models import SalesData 
from django.db.models import Sum,F,FloatField 

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        products = SalesData.objects.values('product').annotate(
            total_revenue = Sum(F('quantity') * F('price'), out_field = FloatField())
        )
        for product in products:
            self.stdout.write(f"Product:{product['product']} - Total Revenue:{product['total_revenue']:2F}")