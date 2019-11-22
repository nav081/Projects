# Generated by Django 2.2.6 on 2019-11-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(default='', max_length=10)),
                ('mobnum', models.BigIntegerField()),
                ('email', models.TextField(max_length=40)),
                ('pas', models.TextField(max_length=20)),
            ],
        ),
    ]
