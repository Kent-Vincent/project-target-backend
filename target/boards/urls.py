from django.urls import path
from .views import BoardsDisplay, BoardsCreate

urlpatterns = [
    path('create/', BoardsCreate.as_view(), name='boards-create'),
    path('display/', BoardsDisplay.as_view(), name='boards-display'),
]
