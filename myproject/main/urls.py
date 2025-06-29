from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_book, name='create_book'),
    path('icecream/', views.create_icecream, name='create_icecream'),
]
