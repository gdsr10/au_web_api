# Generated by Django 4.1.7 on 2023-05-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_entrydetails_entrydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='UserTypeName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
