# Generated by Django 2.0.7 on 2018-08-30 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='bank_address',
        ),
    ]
