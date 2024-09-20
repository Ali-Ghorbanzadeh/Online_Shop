# Generated by Django 5.1.1 on 2024-09-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]