from django.db import models
from workspace.models import Stage


# Create your models here.

class Tickets(models.Model):
    # blank fields
    # description, attachments, coverphoto
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='tickets')
    ticket_ID = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, default='') 
    description = models.TextField(blank=True, null=True)
    attachments = models.FileField(blank=True, upload_to='assets/attachment', null=True)
    time_elapsed = models.DurationField(default=0)
    avatar_icon = models.CharField(max_length=100)
    assignee = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, default='LOW')
    filed_by_avatar_icon = models.CharField(max_length=100)
    filed_by = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='assets/cover', null=True, blank=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.title