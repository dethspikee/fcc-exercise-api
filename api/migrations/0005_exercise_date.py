# Generated by Django 3.0.5 on 2020-04-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200425_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
