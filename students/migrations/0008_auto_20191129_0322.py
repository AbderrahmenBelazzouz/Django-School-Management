# Generated by Django 2.2.7 on 2019-11-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20191127_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='studentavar.png', upload_to='students'),
        ),
    ]
