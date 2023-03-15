from django.urls import path
from . import views
app_name = 'comments'
urlpatterns = [
    path('', views.product_details, name='details'),
    path('products/<int:product_id>/create/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'), 
]




