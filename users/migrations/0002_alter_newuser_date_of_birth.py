# Generated by Django 3.2 on 2022-09-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]