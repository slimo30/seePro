# Generated by Django 5.0 on 2023-12-26 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_client_purchase_shop_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shop'),
        ),
    ]
