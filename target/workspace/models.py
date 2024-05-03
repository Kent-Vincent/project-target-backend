from django.db import models
from users.models import User
from tickets.models import Tickets

class Workspace(models.Model):
    workspace_ID = models.BigAutoField(primary_key=True)
    workspace_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    tickets = models.ManyToManyField(Tickets)

    def __str__(self):
        return self.workspace_name