# Generated by Django 4.1 on 2023-04-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0003_orders_address_orders_email_orders_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ispaid',
            field=models.CharField(default='Pending', max_length=500),
        ),
    ]
