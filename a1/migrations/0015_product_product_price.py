# Generated by Django 4.2.3 on 2023-07-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0014_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
