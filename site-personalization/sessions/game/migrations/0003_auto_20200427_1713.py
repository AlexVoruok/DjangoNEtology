# Generated by Django 2.2.10 on 2020-04-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200426_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='playergameinfo',
            name='currenttry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='aim',
            field=models.IntegerField(default=0, verbose_name='Загадайте число от 1 до 10'),
        ),
    ]
