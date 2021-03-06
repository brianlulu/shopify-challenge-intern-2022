# Generated by Django 4.0.4 on 2022-05-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouse',
            old_name='inventories',
            new_name='product_list',
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse_list',
            field=models.ManyToManyField(through='inventory.Inventory', to='inventory.warehouse'),
        ),
    ]
