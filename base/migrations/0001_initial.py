# Generated by Django 3.0.3 on 2020-12-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UninorteUser',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('schedule', models.CharField(max_length=98)),
            ],
        ),
    ]