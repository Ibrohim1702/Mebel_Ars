# Generated by Django 4.1.6 on 2023-06-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_category_img_remove_product_bed_height_and_more'),
        ('sayt', '0007_productctg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ism', models.CharField(max_length=256)),
                ('Familiya', models.CharField(max_length=256)),
                ('yoshi', models.IntegerField(null=True)),
                ('city', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Andijon', 'Andijon'), ('Farg`ona', 'Farg`ona'), ('Namangan', 'Namangan'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxandaryo', 'Surxandaryo'), ('Buxoro', 'Buxoro'), ('Samarqand', 'Samarqand'), ('Jizzax', 'Jizzax'), ('Navoiy', 'Navoiy'), ('Sirdaryo', 'Sirdaryo'), ('Xorazm', 'Xorazm')], max_length=125, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bascade',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='ProductCtg',
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayt.user'),
        ),
    ]
