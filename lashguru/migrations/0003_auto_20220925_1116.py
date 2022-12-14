# Generated by Django 3.2 on 2022-09-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lashguru', '0002_addbrandfields_catmanagetemplates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbrandfields',
            name='colored_files',
            field=models.ImageField(height_field='300px', upload_to='colored_files', width_field='500px'),
        ),
        migrations.AlterField(
            model_name='addbrandfields',
            name='negative_files',
            field=models.ImageField(height_field='300px', upload_to='negative_files', width_field='500px'),
        ),
        migrations.AlterField(
            model_name='addbrandfields',
            name='positive_files',
            field=models.ImageField(height_field='300px', upload_to='positive_files', width_field='500px'),
        ),
    ]
