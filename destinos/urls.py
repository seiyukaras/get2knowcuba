from django.urls import path
from .views import destinations, PaqueteListView

urlpatterns = [
    path('', PaqueteListView.as_view(), name="destinos"),
    #path('', destinations, name="Destinations"),
    #path('details/', views.details, name="Details"),
]