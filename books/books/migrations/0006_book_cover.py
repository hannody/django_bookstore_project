# Generated by Django 3.2 on 2021-04-07 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_delete_extrainfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]