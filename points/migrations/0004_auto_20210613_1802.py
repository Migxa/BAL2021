# Generated by Django 3.0.5 on 2021-06-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_team_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='color',
            field=models.CharField(default='grey', max_length=32),
        ),
    ]