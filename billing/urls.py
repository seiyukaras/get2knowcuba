from django.urls import path
from .views import billing

urlpatterns = [
    path('', billing.as_view(), name="Billing"),
]