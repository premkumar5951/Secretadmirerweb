# Generated by Django 3.0.7 on 2021-06-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretmsgapp', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='user.png', upload_to='images'),
        ),
    ]
