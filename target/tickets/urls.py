# myapp/urls.py
from django.urls import path
from .views import TicketsCreate

urlpatterns = [
    path('create/', TicketsCreate.as_view(), name='ticket-create'),

    #  path('api/', include('myapp.urls')),
]
