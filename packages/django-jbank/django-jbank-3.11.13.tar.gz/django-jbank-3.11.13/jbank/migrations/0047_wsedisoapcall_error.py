# Generated by Django 2.2.3 on 2019-11-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0046_auto_20191128_2242"),
    ]

    operations = [
        migrations.AddField(
            model_name="wsedisoapcall",
            name="error",
            field=models.TextField(blank=True, verbose_name="error"),
        ),
    ]
