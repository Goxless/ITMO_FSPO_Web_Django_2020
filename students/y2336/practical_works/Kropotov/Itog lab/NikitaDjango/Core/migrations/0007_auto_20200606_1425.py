# Generated by Django 3.0.3 on 2020-06-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_auto_20200606_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='img',
            field=models.ImageField(null=True, upload_to='UserPics'),
        ),
    ]
