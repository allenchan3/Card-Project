# Generated by Django 3.1.6 on 2021-02-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210218_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=7),
            preserve_default=False,
        ),
    ]