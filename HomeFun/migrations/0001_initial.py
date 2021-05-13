# Generated by Django 3.1.6 on 2021-05-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, unique=True)),
                ('Desc', models.TextField()),
                ('Preparation', models.TextField()),
                ('How_to_do', models.TextField()),
            ],
        ),
    ]
