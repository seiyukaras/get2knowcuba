from django.urls import path
from . import views

urlpatterns = [
    path('/<slug:slug>', views.billing, name="Billing"),
]