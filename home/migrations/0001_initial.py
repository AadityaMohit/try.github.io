# Generated by Django 4.2.6 on 2023-11-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('stream', models.CharField(max_length=10)),
                ('semmark', models.IntegerField()),
            ],
        ),
    ]
