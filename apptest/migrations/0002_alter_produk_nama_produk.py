# Generated by Django 5.1.4 on 2025-01-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='nama_produk',
            field=models.CharField(max_length=255),
        ),
    ]
