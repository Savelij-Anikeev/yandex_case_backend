# Generated by Django 4.2.7 on 2023-12-03 11:23

from django.db import migrations, models
import event_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0010_event_organizer_fio_alter_event_organizer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=event_app.models.upload_to),
        ),
    ]
