# Generated by Django 2.0.2 on 2018-04-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]