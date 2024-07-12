from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('books/', views.books, name='books'),
    path('books/<int:pk>/', views.book_detail, name='book_detail')
]
