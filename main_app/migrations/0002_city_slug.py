# Generated by Django 3.1.5 on 2021-01-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=20, null=True),
        ),
    ]