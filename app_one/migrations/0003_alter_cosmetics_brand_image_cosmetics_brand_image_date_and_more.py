# Generated by Django 4.0 on 2022-09-17 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_alter_cosmetics_brand_image_cosmetics_brand_image_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmetics_brand_image',
            name='Cosmetics_brand_image_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 49, 19, 438605)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='Newsletter_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 49, 19, 436611)),
        ),
        migrations.AlterField(
            model_name='order_info',
            name='perchase_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 49, 19, 442593)),
        ),
        migrations.AlterField(
            model_name='stay_updated_subscribtion',
            name='Stay_Updated_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 49, 19, 437607)),
        ),
        migrations.AlterField(
            model_name='video_post',
            name='Blog_podt_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 49, 19, 436611)),
        ),
    ]
