# Generated by Django 4.0 on 2021-12-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productz', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
