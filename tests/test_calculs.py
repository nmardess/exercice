import pytest
from utils import calculs


@pytest.mark.parametrize("test_input, expected", [("Number(86)", 86),
                                                  ("Number()", int()),
                                                  ("Number(86", 86),
                                                  ("Number86)", 86)])
def test_nettoyage_caracteres(test_input, expected):
    calculs.nettoyage_caracteres(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("86 - 5", 81),
                                                  ("299 - 24", 275),
                                                  ("999999999999 - 232",
                                                   999999999767)])
def test_eval_operation(test_input, expected):
    calculs.eval_operation(test_input) == expected


test_value = [
                ("Number(999999999999) - Number(232)", "Opération possible : "
                 "Number(999999999999) - Number(232) ==>  999999999999 - 232 "
                 "= 999999999767"),
                ("Number(86) - Number(5", "Opération possible : Number(86) - "
                 "Number(5 ==>  86 - 5 = 81"),
                ("Number(797)", "Opération impossible : Number(797)")
            ]


@pytest.mark.parametrize("test_input, expected", test_value)
def test_resultat_ligne(test_input, expected):
    calculs.resultat_ligne(test_input) == expected
