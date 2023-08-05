# Generated by Django 3.0.11 on 2021-04-01 22:10

from django.db import migrations

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):

    dependencies = [
        ("rozbieznosci_dyscyplin", "0006_recreate"),
        ("bpp", "0253_rekord_mat_slug"),
    ]

    operations = [
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql(
                "0002_rok_2017_i_wyzej", app_name="rozbieznosci_dyscyplin"
            )
        )
    ]
