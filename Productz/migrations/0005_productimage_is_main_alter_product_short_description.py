# Generated by Django 4.0 on 2022-01-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productz', '0004_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=60, null=True),
        ),
    ]
