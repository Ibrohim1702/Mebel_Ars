# Generated by Django 4.1.3 on 2023-01-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='city',
            field=models.CharField(choices=[('Toshkent', 'tosh'), ('Andijon', 'an'), ('Farg`ona', 'fa'), ('Namangan', 'nam'), ('Qashqadaryo', 'qash'), ('Surxandaryo', 'sur'), ('Buxoro', 'bux'), ('Samarqand', 'sam'), ('Jizzax', 'jiz'), ('Navoiy', 'nav'), ('Sirdaryo', 'sir'), ('Xorazm', 'xor')], max_length=125, null=True),
        ),
    ]
