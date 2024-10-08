# Generated by Django 4.2.11 on 2024-09-10 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtendedUser",
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
                ("cell_no", models.IntegerField(blank=True, null=True)),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Physical address",
                    ),
                ),
                ("sex", models.CharField(max_length=10, null=True)),
                (
                    "dob",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of birth"
                    ),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "pic",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_query_name="user_pic",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
