from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.create_book, name='create_book'),
    path('create_data/', views.create_data, name='create_data')
]
