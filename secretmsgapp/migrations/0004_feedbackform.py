# Generated by Django 3.0.7 on 2021-06-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretmsgapp', '0003_auto_20210627_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('feedtxt', models.TextField(max_length=500)),
            ],
        ),
    ]