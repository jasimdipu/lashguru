# Generated by Django 3.2 on 2022-09-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lashguru', '0003_auto_20220925_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbrandfields',
            name='colored_files',
            field=models.ImageField(upload_to='colored_files'),
        ),
        migrations.AlterField(
            model_name='addbrandfields',
            name='negative_files',
            field=models.ImageField(upload_to='negative_files'),
        ),
        migrations.AlterField(
            model_name='addbrandfields',
            name='positive_files',
            field=models.ImageField(upload_to='positive_files'),
        ),
    ]