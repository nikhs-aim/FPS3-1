# Generated by Django 4.1.4 on 2023-01-29 17:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0021_alter_faculty_fac_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_Date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('f8688a75-22f9-4867-8876-8ee4a2d117c8'), editable=False, primary_key=True, serialize=False),
        ),
    ]
