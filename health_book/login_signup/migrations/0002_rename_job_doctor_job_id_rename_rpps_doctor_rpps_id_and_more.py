# Generated by Django 4.0.1 on 2022-01-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='job',
            new_name='job_id',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rpps',
            new_name='rpps_id',
        ),
        migrations.RenameField(
            model_name='trustedperson',
            old_name='address',
            new_name='address_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='address_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='main_doctor',
            new_name='main_doctor_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='parent1',
            new_name='parent1_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='parent2',
            new_name='parent2_id',
        )
    ]