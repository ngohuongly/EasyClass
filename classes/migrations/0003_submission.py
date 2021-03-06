# Generated by Django 3.1.6 on 2021-05-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20210512_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_ID', models.CharField(max_length=64)),
                ('Student_name', models.CharField(max_length=64)),
                ('Student_ID', models.CharField(max_length=64)),
                ('Note', models.TextField()),
                ('Github_page', models.URLField()),
                ('File_upload', models.FileField(upload_to='')),
            ],
        ),
    ]
