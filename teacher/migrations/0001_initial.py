# Generated by Django 5.1 on 2024-08-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=17)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('date_de_naissance', models.DateField(null=True)),
                ('matiere', models.CharField(choices=[('Math', 'Math'), ('Physique', 'Physique'), ('Eps', 'Eps'), ('Anglais', 'Anglais'), ('SVT', 'SVT'), ('Philosophie', 'Philosophie'), ('Français', 'Français')], max_length=15)),
                ('telephone', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=7)),
            ],
        ),
    ]
