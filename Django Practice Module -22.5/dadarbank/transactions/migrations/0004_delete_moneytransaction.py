# Generated by Django 4.2.7 on 2023-12-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MoneyTransaction',
        ),
    ]
