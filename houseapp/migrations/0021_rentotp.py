# Generated by Django 5.1.3 on 2024-11-30 19:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseapp', '0020_delete_rentotp'),
    ]

    operations = [
        migrations.CreateModel(
            name='rentOTP',
            fields=[
                ('rentOTPid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hid', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/images/')),
                ('price', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimages', models.FileField(upload_to='')),
                ('emailId', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('add_date', models.DateField()),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
