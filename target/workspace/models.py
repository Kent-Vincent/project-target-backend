from django.db import models
from users.models import User
from tickets.models import Tickets

class Workspace(models.Model):
    workspace_ID = models.BigAutoField(primary_key=True)
    workspace_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    stages = models.ForeignKey('Stage', on_delete=models.CASCADE)

    def __str__(self):
        return self.workspace_name

class Stage(models.Model):
    TICKET_CATEGORY = [
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('BLOCKED', 'Blocked'),
        ('FOR REVIEW', 'For Review'),
        ('DONE', 'Done'),
    ]
    stages_ID = models.BigAutoField(primary_key=True)
    stage_name = models.CharField(max_length=50, choices=TICKET_CATEGORY)
    tickets = models.ManyToManyField(Tickets)

    def __str__(self):
        return self.stage_name