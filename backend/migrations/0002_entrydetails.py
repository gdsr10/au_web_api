# Generated by Django 4.1.7 on 2023-04-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetails',
            fields=[
                ('EntryDetailsCode', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('EntryDate', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Status', models.CharField(default='A', max_length=1)),
                ('MedicalCenterCode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.medicalcentermaster')),
                ('UserCode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.useraccount')),
            ],
        ),
    ]