# Generated by Django 3.2.3 on 2021-05-25 16:20

from django.db import migrations
import jutil.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0009_referencepaymentbatchfile_cached_total_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="statementrecorddetail",
            name="creditor_account_scheme",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=8, verbose_name="creditor account scheme"),
        ),
    ]
