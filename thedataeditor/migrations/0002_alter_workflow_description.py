# Generated by Django 4.2.11 on 2024-09-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thedataeditor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workflow",
            name="description",
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
