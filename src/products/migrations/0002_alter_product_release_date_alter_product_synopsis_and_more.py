# Generated by Django 4.1.7 on 2023-03-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='synopsis',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(max_length=200),
        ),
    ]
