from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add_sales,name="add_sales"),
    path('delete/<int:id>/',views.delete_sales,name="delete_sales"),
    path('update/<int:id>/',views.update_sales,name="update"),
]