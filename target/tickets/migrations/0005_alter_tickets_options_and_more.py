# Generated by Django 5.0.4 on 2024-04-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_tickets_attachments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.RenameField(
            model_name='tickets',
            old_name='fileBy_avatar_icon',
            new_name='filed_by_avatar_icon',
        ),
        migrations.RenameField(
            model_name='tickets',
            old_name='ticketName',
            new_name='ticket_name',
        ),
        migrations.AlterField(
            model_name='tickets',
            name='attachments',
            field=models.FileField(null=True, upload_to='attachments/'),
        ),
    ]
