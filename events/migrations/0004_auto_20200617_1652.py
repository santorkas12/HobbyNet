# Generated by Django 3.0.7 on 2020-06-17 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200617_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='user',
            new_name='participant',
        ),
    ]
