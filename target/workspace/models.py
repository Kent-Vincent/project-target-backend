from django.db import models

class Workspace(models.Model):
    workspace_ID = models.BigAutoField(primary_key=True)
    workspace_name = models.CharField(max_length=255)



    def __str__(self):
        return self.workspace_name