# Generated by Django 4.2.11 on 2024-05-10 09:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("heroTitle", models.CharField(max_length=100, null=True)),
                ("heroSubtitle", wagtail.fields.RichTextField(null=True)),
                ("heroOutlineButtonTitle", models.CharField(max_length=100, null=True)),
                ("heroOutlineButtonHref", models.CharField(null=True)),
                ("heroFlatButtonTitle", models.CharField(max_length=100, null=True)),
                ("heroFlatButtonHref", models.CharField(null=True)),
                ("services_title", models.CharField(max_length=100, null=True)),
                (
                    "services",
                    wagtail.fields.StreamField(
                        [
                            (
                                "service",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("subtitle", wagtail.blocks.RichTextBlock()),
                                    ]
                                ),
                            )
                        ],
                        null=True,
                    ),
                ),
                ("landing_page_title", models.CharField(max_length=100, null=True)),
                ("landing_page_box_title", models.CharField(max_length=100, null=True)),
                ("landing_page_box_subtitle", wagtail.fields.RichTextField(null=True)),
                (
                    "heroImage",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "landing_page_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
