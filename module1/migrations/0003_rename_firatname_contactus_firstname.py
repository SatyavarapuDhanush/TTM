# Generated by Django 5.0 on 2024-02-09 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='firatname',
            new_name='firstname',
        ),
    ]
