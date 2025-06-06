# Generated by Django 5.1.3 on 2024-11-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseapp', '0005_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('emailaddress', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('usertype', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('conpassword', models.CharField(max_length=50)),
                ('registerdate', models.CharField(max_length=30)),
            ],
        ),
    ]
