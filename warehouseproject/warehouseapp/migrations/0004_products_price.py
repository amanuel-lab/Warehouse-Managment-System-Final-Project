# Generated by Django 4.1.5 on 2023-02-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0003_alter_products_category_alter_products_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
