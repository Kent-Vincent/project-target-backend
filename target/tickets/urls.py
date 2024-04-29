# myapp/urls.py
from django.urls import path
from .views import TicketsCreate

urlpatterns = [
    path('create/', TicketsCreate.as_view(), name='ticket-create'),
    path('display/', TicketsCreate.as_view(), name='ticket-display'),
]
