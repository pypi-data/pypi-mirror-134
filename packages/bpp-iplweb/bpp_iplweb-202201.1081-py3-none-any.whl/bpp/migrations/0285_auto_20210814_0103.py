# Generated by Django 3.0.14 on 2021-08-13 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0284_auto_20210814_0023"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bppmultiseekvisibility",
            options={
                "ordering": ("sort_order",),
                "verbose_name": "widoczność opcji wyszukiwania",
                "verbose_name_plural": "widoczność opcji wyszukiwania",
            },
        ),
        migrations.RenameField(
            model_name="bppmultiseekvisibility",
            old_name="name",
            new_name="field_name",
        ),
    ]
