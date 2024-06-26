# Generated by Django 4.2.11 on 2024-06-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "thedatabet",
            "0003_rename_guest_sc_r_squared_bettingtips_guest_sc_r2_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="bettingtips",
            old_name="result_mse",
            new_name="guest_result_mse",
        ),
        migrations.RenameField(
            model_name="bettingtips",
            old_name="result_r2",
            new_name="guest_result_r2",
        ),
        migrations.AddField(
            model_name="bettingtips",
            name="home_result_mse",
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bettingtips",
            name="home_result_r2",
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
