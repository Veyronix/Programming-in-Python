# Generated by Django 2.0.5 on 2018-05-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='amount_of_vacancies',
            new_name='amount_of_places',
        ),
    ]
