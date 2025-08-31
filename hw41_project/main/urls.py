from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signed/', views.signed_data, name="signed"),
]
