# Generated by Django 3.2.9 on 2021-12-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='profile_pic',
            field=models.ImageField(upload_to='media/profile_pic'),
        ),
    ]
