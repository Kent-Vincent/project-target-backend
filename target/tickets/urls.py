# myapp/urls.py
from django.urls import path
from .views import TicketsCreate, TicketDisplay

urlpatterns = [
    path('create/', TicketsCreate.as_view(), name='ticket-create'),
    # path('display/', TicketDisplay.as_view(), name='ticket-display'),
]
