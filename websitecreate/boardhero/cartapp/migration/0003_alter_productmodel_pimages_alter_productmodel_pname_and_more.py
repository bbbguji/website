# Generated by Django 4.0 on 2022-01-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_albummodel_photomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pimages',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pprice',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]