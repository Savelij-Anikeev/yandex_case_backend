# Generated by Django 4.2.7 on 2023-12-02 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_app', '0009_event_event_type_event_organizer_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer_fio',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
