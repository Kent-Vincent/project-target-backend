from django.db import models


# Create your models here.

class Tickets(models.Model):
    TICKET_PRIORITIES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    ticket_name = models.CharField(max_length=100)  
    description = models.TextField()
    attachments = models.FileField(null=True, upload_to='assets/attachment')
    time_elapsed = models.DurationField(null=True, blank=True)
    avatar_icon = models.ImageField(upload_to='assets/avatars', null=True, blank=True)
    assignee = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=TICKET_PRIORITIES, default='LOW')
    filed_by_avatar_icon = models.ImageField(upload_to='assets/avatars', null=True, blank=True)
    filed_by = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='assets/cover', null=True, blank=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"