# Generated by Django 5.1.4 on 2025-01-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('running_time', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
    ]
