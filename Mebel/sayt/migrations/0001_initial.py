# Generated by Django 4.1.3 on 2023-01-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familya', models.CharField(max_length=256, null=True)),
                ('yoshi', models.IntegerField(null=True)),
                ('lavozimi', models.CharField(max_length=256, null=True)),
                ('salary', models.IntegerField(null=True)),
            ],
        ),
    ]