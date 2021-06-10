# Generated by Django 3.2.4 on 2021-06-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParselVerileri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ada', models.PositiveIntegerField(null=True)),
                ('parsel', models.IntegerField(null=True)),
                ('kordinatx', models.FloatField(null=True)),
                ('kordinaty', models.FloatField(null=True)),
                ('alan', models.IntegerField(null=True)),
            ],
        ),
    ]