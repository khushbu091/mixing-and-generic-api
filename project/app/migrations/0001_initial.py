# Generated by Django 5.0.4 on 2024-04-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=50)),
                ('empJdate', models.DateField()),
                ('empAddress', models.CharField(max_length=50)),
                ('empContact', models.IntegerField()),
            ],
        ),
    ]
