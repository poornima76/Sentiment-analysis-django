from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('products/<int:product_id>/', views.product_detail, name='product_detail'), 
]