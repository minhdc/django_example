# Generated by Django 2.0.3 on 2018-07-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvoexample', '0004_wordexamplerelation_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordexamplerelation',
            name='relation',
            field=models.CharField(max_length=200),
        ),
    ]
