# Generated by Django 4.0.4 on 2022-07-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Website',
            field=models.ManyToManyField(to='main_app.website'),
        ),
    ]