# Generated by Django 3.0.5 on 2021-06-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('points', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
