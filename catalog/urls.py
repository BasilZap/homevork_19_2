from django.urls import path
from catalog.views import index, contact

urlpatterns = [
    path('contact/', contact),
    path('', index),
]