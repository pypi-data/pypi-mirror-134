# Generated by Django 3.0.14 on 2021-10-27 21:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import ewaluacja2021.fields
import ewaluacja2021.validators

import django.contrib.postgres.fields.jsonb


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0306_delete_ewaluacja2021liczbandlauczelni"),
        ("ewaluacja2021", "0002_auto_20211026_1137"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportMaksymalnychSlotow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "plik",
                    models.FileField(
                        upload_to="",
                        validators=[
                            ewaluacja2021.validators.validate_xlsx,
                            ewaluacja2021.validators.xlsx_header_validator(
                                columns=[
                                    "Stopień / Tytuł",
                                    "Nazwisko",
                                    "Imię",
                                    "ORCID",
                                    "Dyscyplina",
                                    "Uwzględniony w ewaluacji",
                                    "maksymalna suma udziałów jednostkowych - wszystkie dyscypliny",
                                    "maksymalna suma udziałów jednostkowych - monografie",
                                ],
                                max_header_row=100,
                            ),
                        ],
                    ),
                ),
                ("przeanalizowany", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name="iloscudzialowdlaautora",
            name="ilosc_udzialow",
            field=ewaluacja2021.fields.LiczbaNField(
                decimal_places=4,
                max_digits=9,
                validators=[django.core.validators.MaxValueValidator(4)],
            ),
        ),
        migrations.CreateModel(
            name="WierszImportuMaksymalnychSlotow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orig_data", django.contrib.postgres.fields.jsonb.JSONField()),
                ("poprawny", models.NullBooleanField(default=None)),
                ("wymagana_integracja", models.NullBooleanField(default=None)),
                ("zintegrowany", models.BooleanField(default=False)),
                (
                    "matched_autor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="bpp.Autor",
                    ),
                ),
                (
                    "matched_dyscyplina",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="bpp.Dyscyplina_Naukowa",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ewaluacja2021.ImportMaksymalnychSlotow",
                    ),
                ),
            ],
        ),
    ]
