# Generated by Django 4.2.7 on 2023-12-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0003_category_eventcategoryrelations'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(through='event_app.EventCategoryRelations', to='event_app.category'),
        ),
    ]