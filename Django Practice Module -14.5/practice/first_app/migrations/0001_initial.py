# Generated by Django 4.2.7 on 2023-12-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('bool_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=220)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='')),
                ('file_path_field', models.FilePathField()),
                ('float_field', models.FloatField()),
                ('generic_ip_address_field', models.GenericIPAddressField()),
                ('image_field', models.ImageField(upload_to='images')),
                ('integer_field', models.IntegerField()),
                ('json_field', models.JSONField()),
                ('positive_big_integer_field', models.PositiveBigIntegerField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integer_field', models.PositiveSmallIntegerField()),
                ('slug_field', models.SlugField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
                ('uuid_field', models.UUIDField()),
            ],
        ),
    ]