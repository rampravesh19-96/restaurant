# Generated by Django 2.2.12 on 2022-06-29 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20220629_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='idd',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
