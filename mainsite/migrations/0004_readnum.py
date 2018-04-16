# Generated by Django 2.0.3 on 2018-04-16 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20180416_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0, verbose_name='阅读计数')),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Blog', verbose_name='博客外键')),
            ],
        ),
    ]
