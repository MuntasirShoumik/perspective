# Generated by Django 4.1.5 on 2023-06-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=100)),
                ("following_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="user_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="profile_image",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
