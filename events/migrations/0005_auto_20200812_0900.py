# Generated by Django 3.0.7 on 2020-08-12 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200617_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='coverimg',
            field=models.ImageField(default='sports_def.jpg', upload_to='event_imgs'),
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
