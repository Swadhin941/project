# Generated by Django 3.2.6 on 2022-01-15 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='email_id',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='accounts',
            old_name='fullname',
            new_name='first_name',
        ),
    ]
