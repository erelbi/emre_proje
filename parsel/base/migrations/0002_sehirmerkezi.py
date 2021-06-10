# Generated by Django 3.2.4 on 2021-06-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SehirMerkezi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parselid', models.PositiveIntegerField(null=True)),
                ('kordinatx', models.FloatField(null=True)),
                ('kordinaty', models.FloatField(null=True)),
            ],
        ),
    ]
