# Generated by Django 2.0.2 on 2018-03-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20180330_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.CharField(choices=[('Executive Member', 'Executive Member'), ('Member', 'Member'), ('Alumni', 'Alumni')], default='Member', max_length=20),
        ),
    ]