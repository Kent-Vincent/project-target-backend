from django.db import models
from users.models import User

class Workspace(models.Model):
    workspace_ID = models.BigAutoField(primary_key=True)
    workspace_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.workspace_name

class Stage(models.Model):
    stages_ID = models.BigAutoField(primary_key=True)
    stage_name = models.CharField(max_length=50)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.stage_name