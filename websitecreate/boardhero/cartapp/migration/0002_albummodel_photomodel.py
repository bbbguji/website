# Generated by Django 3.2.7 on 2021-12-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adate', models.DateTimeField(auto_now=True)),
                ('alocation', models.CharField(blank=True, default='', max_length=200)),
                ('atitle', models.CharField(max_length=100)),
                ('adesc', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psubject', models.CharField(max_length=100)),
                ('pdate', models.DateTimeField(auto_now=True)),
                ('purl', models.CharField(max_length=100)),
                ('phit', models.IntegerField(default=0)),
                ('palbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.albummodel')),
            ],
        ),
    ]