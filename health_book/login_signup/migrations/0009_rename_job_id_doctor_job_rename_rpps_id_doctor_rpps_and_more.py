# Generated by Django 4.0.1 on 2022-01-31 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0008_user_diseases_alter_userdisease_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='job_id',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rpps_id',
            new_name='rpps',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='user_id',
            new_name='user',
        ),
    ]
