# Generated by Django 5.1.1 on 2024-09-30 12:49

from django.db import migrations, models

import market.models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0010_serviceoptionimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceimage",
            name="image",
            field=models.FileField(
                max_length=255, upload_to=market.models.get_service_image_upload_path
            ),
        ),
        migrations.AlterField(
            model_name="serviceoptionimage",
            name="image",
            field=models.FileField(
                max_length=255,
                upload_to=market.models.get_service_option_image_upload_path,
            ),
        ),
    ]
