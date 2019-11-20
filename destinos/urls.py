from django.urls import path
from .views import PaqueteListView , PaqueteDetailView

urlpatterns = [
    path('', PaqueteListView.as_view(), name="Destinations"),
    path('<slug:slug>', PaqueteDetailView.as_view(), name='detail'),
    #path('', destinations, name="Destinations"),
    #path('details/', views.details, name="Details"),
]