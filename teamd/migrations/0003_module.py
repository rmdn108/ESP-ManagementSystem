# Generated by Django 3.2.12 on 2023-05-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamd', '0002_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(editable=False, max_length=7, unique=True)),
                ('departement', models.CharField(max_length=3)),
                ('intitule', models.CharField(max_length=200)),
                ('coef', models.IntegerField()),
                ('nombre_credit', models.IntegerField()),
                ('volume_horaires_cm', models.IntegerField()),
                ('volume_horaires_td', models.IntegerField()),
                ('volume_horaires_tp', models.IntegerField()),
                ('unite_enseignement', models.CharField(max_length=100)),
                ('semestre', models.IntegerField()),
                ('enseignant_responsable', models.CharField(max_length=100)),
            ],
        ),
    ]
