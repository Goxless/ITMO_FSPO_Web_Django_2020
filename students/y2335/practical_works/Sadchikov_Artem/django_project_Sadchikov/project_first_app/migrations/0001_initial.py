# Generated by Django 3.0.5 on 2020-04-08 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('governmentNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('secondName', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStart', models.DateField()),
                ('dateEnd', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Driver_license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('dateIssued', models.DateField()),
                ('type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car_owner')),
            ],
        ),
        migrations.AddField(
            model_name='car_owner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Possession', to='project_first_app.Car'),
        ),
    ]
