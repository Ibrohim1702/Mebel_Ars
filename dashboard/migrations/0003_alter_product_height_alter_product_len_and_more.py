# Generated by Django 4.1.3 on 2023-01-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_height_alter_product_len_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='len',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]
