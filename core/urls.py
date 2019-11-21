from django.urls import path
from .views import homeListView

urlpatterns = [
    path('', homeListView.as_view(), name="Home"),
]