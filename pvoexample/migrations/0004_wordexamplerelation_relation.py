# Generated by Django 2.0.3 on 2018-07-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvoexample', '0003_auto_20180720_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordexamplerelation',
            name='relation',
            field=models.CharField(default='Undefined', max_length=200),
        ),
    ]