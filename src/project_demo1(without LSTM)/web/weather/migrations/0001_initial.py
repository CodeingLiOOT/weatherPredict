# Generated by Django 3.0.3 on 2020-07-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=8)),
                ('userName', models.CharField(max_length=20)),
                ('userPassword', models.CharField(max_length=20)),
            ],
        ),
    ]
