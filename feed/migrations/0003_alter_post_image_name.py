# Generated by Django 4.1.5 on 2023-06-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.ImageField(null=True, upload_to="post_images"),
        ),
    ]
