# Generated by Django 3.2.6 on 2021-08-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='12 apple road', max_length=80),
        ),
    ]
