# Generated by Django 2.2.3 on 2019-11-28 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0045_wsediconnection_receiver_identifier"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="wsedisoapcall",
            options={"verbose_name": "WS-EDI SOAP call", "verbose_name_plural": "WS-EDI SOAP calls"},
        ),
    ]
