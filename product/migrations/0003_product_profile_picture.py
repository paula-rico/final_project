# Generated by Django 4.1.4 on 2023-02-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
    ]
