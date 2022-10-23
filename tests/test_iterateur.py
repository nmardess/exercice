import pytest
from utils import iterateur


@pytest.mark.parametrize("test_input, expected", [
                (["Number(999999999999) - Number(232)"], "Opération possible "
                 ": Number(999999999999) - Number(232) ==>  999999999999 - "
                 "232 = 999999999767"),
                (["Number(86) - Number(5"], "Opération possible : Number(86) "
                 "- Number(5 ==>  86 - 5 = 81"),
                (["Number(797)"], "Opération impossible : Number(797)")
            ])
def test_resultat_ligne(test_input, expected):
    for calcul in iterateur.CalculLigne(test_input):
        calcul == expected


def test_resultat_ligne_is_iterator():
    iter(iterateur.CalculLigne([]))
