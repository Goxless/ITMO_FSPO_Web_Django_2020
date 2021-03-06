# Generated by Django 3.0.4 on 2020-03-25 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('gov_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_start', models.DateField()),
                ('data_end', models.DateField()),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Auto')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Person')),
            ],
        ),
        migrations.CreateModel(
            name='DriverDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('SC', 'sport car'), ('С', 'crossover'), ('M', 'micro car')], max_length=30)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Person')),
            ],
        ),
    ]
