# Generated by Django 2.0.5 on 2018-05-20 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180520_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='person_id',
            new_name='person',
        ),
    ]
