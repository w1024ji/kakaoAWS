# purchase/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('purchase/', views.purchase_view, name='purchase'),
    path('purchase_action/', views.purchase_action, name='purchase_action'),
]
