# Generated by Django 5.0.6 on 2024-06-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_users_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]
