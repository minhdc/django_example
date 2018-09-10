# Generated by Django 2.0.7 on 2018-09-10 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('example_desc', models.TextField()),
                ('keywords', models.TextField(default='nokeyword')),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=50)),
                ('definition', models.TextField(default='')),
                ('pic', models.ImageField(default='', upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='WordExampleRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_id', models.SmallIntegerField()),
                ('example_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvoexample.Example')),
                ('word_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvoexample.Word')),
            ],
        ),
        migrations.CreateModel(
            name='WordRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.SmallIntegerField()),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_id', to='pvoexample.Word')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_id', to='pvoexample.Word')),
            ],
        ),
    ]
