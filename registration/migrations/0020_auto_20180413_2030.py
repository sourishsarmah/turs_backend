# Generated by Django 2.0.2 on 2018-04-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20180406_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='roll',
            field=models.CharField(max_length=8),
        ),
    ]
