# Generated by Django 3.0.6 on 2020-06-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
    ]