# Generated by Django 5.0 on 2024-02-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('firatname', models.TextField(max_length=100)),
                ('lastname', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]