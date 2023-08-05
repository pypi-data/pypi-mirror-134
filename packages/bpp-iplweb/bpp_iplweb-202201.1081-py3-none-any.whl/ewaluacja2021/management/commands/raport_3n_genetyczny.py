from django.core.management import BaseCommand
from django.db import transaction

from ewaluacja2021.core.genetyczny import GAD


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--dyscyplina", default="nauki medyczne")
        parser.add_argument("--generations", default=500, type=int)
        parser.add_argument("--ile_najlepszych", default=40, type=int)
        parser.add_argument("--ile-losowych", default=50, type=int)
        parser.add_argument("--ile-zupelnie-losowych", default=30, type=int)
        parser.add_argument("--ile_epok", default=10, type=int)
        parser.add_argument("--saturate", default=100, type=int)
        parser.add_argument("--output-path", default=None, type=str)

    @transaction.atomic
    def handle(
        self,
        dyscyplina,
        generations,
        ile_najlepszych,
        ile_losowych,
        ile_zupelnie_losowych,
        output_path,
        ile_epok,
        saturate,
        liczba_n=None,
        *args,
        **options
    ):

        algorytm = GAD(
            nazwa_dyscypliny=dyscyplina,
            max_gen=generations,
            ile_najlepszych=ile_najlepszych,
            ile_losowych=ile_losowych,
            ile_zupelnie_losowych=ile_zupelnie_losowych,
            output_path=output_path,
            saturate=saturate,
            ile_epok=ile_epok,
        )
        algorytm.powitanie()
        algorytm.pracuj()
        algorytm.zrzuc_dane("genetyczny")
        algorytm.pozegnanie()
