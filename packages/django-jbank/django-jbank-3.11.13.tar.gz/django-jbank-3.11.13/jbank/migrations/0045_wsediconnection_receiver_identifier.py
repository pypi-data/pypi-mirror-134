# Generated by Django 2.2.3 on 2019-11-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0044_auto_20191128_2231"),
    ]

    operations = [
        migrations.AddField(
            model_name="wsediconnection",
            name="receiver_identifier",
            field=models.CharField(default="", max_length=32, verbose_name="receiver identifier"),
            preserve_default=False,
        ),
    ]
