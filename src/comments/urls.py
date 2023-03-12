from django.urls import path
from . import views
app_name = 'comments'
urlpatterns = [
    path('products/<int:product_id>/comments/create/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]



