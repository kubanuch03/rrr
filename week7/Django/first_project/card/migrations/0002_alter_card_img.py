# Generated by Django 4.2.1 on 2023-06-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
