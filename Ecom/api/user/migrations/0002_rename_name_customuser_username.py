# Generated by Django 4.0.2 on 2022-02-22 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='username',
        ),
    ]
