# Generated by Django 3.0.7 on 2020-06-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200619_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pictures/profile.png', upload_to='profile_pictures'),
        ),
    ]
