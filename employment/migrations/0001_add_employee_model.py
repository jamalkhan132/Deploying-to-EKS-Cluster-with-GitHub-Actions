# Generated by Django 3.2.13 on 2022-05-01 23:20

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
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
            ],
        ),
    ]