# Generated by Django 3.0.14 on 2021-08-08 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0021_auto_20210808_1204"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="scientist",
            options={
                "ordering": (
                    "from_institution_api",
                    "lastName",
                    "name",
                    "qualifications",
                ),
                "verbose_name": "Osoba w PBN API",
                "verbose_name_plural": "Osoby w PBN API",
            },
        ),
        migrations.AlterUniqueTogether(
            name="publication",
            unique_together={("mongoId", "title", "isbn", "doi", "publicUri")},
        ),
    ]
