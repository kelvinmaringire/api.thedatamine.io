# Generated by Django 4.2.11 on 2024-08-12 08:37

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_delete_contactform"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="websites",
            field=wagtail.fields.StreamField(
                [
                    (
                        "websites",
                        wagtail.blocks.StructBlock(
                            [
                                ("url", wagtail.blocks.URLBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ]
                        ),
                    )
                ],
                null=True,
            ),
        ),
    ]