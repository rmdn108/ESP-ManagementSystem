# Generated by Django 3.2.12 on 2023-05-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('Matricule', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('moyenne_S1', models.FloatField()),
                ('moyenne_S2', models.FloatField()),
                ('moyenne_generale', models.FloatField()),
                ('Decision', models.CharField(max_length=50)),
            ],
        ),
    ]
