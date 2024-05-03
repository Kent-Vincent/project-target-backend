from django.db import models
from tickets.models import Tickets
from users.models import User

class Workspace(models.Model):
    workspace_ID = models.BigAutoField(primary_key=True)
    workspace_name = models.CharField(max_length=255)
    # ticket = models.ForeignKey(Tickets.ticket_ID, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.workspace_name