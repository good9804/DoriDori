# Generated by Django 3.2.16 on 2023-01-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=24, unique=True)),
                ('name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_passenger', models.TextField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
