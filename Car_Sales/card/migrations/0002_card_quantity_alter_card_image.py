# Generated by Django 4.2.7 on 2023-12-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
