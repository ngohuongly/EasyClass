# Generated by Django 3.1.6 on 2021-03-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentsinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Emails', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Parents_name', models.CharField(max_length=100)),
                ('Parents_emails', models.CharField(max_length=100)),
            ],
        ),
    ]
