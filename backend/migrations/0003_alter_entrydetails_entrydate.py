# Generated by Django 4.1.7 on 2023-05-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_entrydetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrydetails',
            name='EntryDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
