# Generated by Django 3.0.14 on 2021-08-08 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pbn_api", "0023_auto_20210809_0122"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="scientist",
            unique_together={("mongoId", "lastName", "name", "orcid")},
        ),
    ]
