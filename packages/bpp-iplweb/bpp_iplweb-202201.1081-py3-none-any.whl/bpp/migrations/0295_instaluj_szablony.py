# Generated by Django 3.0.14 on 2021-09-25 19:34

import os

from django.db import migrations

dirname = os.path.dirname(__file__)


def template_n(elem):
    return f"{dirname}/../templates/{elem}"


def create_template(Template, name):
    Template.objects.create(
        name=name,
        content=open(template_n(name), "r").read(),
    )


def instaluj_szablony(apps, schema_editor):
    Template = apps.get_model("dbtemplates", "Template")

    create_template(Template, "opis_bibliograficzny.html")
    create_template(Template, "browse/praca_tabela.html")

    SzablonDlaOpisuBibliograficznego = apps.get_model(
        "bpp", "SzablonDlaOpisuBibliograficznego"
    )
    SzablonDlaOpisuBibliograficznego.objects.create(
        model=None,
        template=Template.objects.get(name="opis_bibliograficzny.html"),
    )


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0294_szablony_opisu_stron"),
    ]

    operations = [migrations.RunPython(instaluj_szablony, migrations.RunPython.noop)]
