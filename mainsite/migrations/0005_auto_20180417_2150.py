# Generated by Django 2.0.3 on 2018-04-17 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_readnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='blog',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]
