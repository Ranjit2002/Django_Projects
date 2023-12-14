# Generated by Django 5.0 on 2023-12-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('email', models.EmailField(max_length=277, verbose_name='Student Email')),
            ],
        ),
    ]