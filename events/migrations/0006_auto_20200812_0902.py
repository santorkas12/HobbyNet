# Generated by Django 3.0.7 on 2020-08-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20200812_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='coverimg',
            field=models.ImageField(default='event_imgs/sports_def.jpg', upload_to='event_imgs'),
        ),
    ]