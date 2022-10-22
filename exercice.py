from utils import calculs, decorateur, iterateur

@decorateur.cosmetique("map")
def test_map():
    with open("test.txt") as fichier:
        lignes = fichier.readlines()
        [print(l) for l in list(map(calculs.resultat_ligne, lignes))]

@decorateur.cosmetique("iterateur")
def test_iterator():
    with open("test.txt") as fichier:
        lignes = fichier.readlines()
        [print(l) for l in iterateur.CalculLigne(lignes)]


if __name__ == "__main__":
    test_iterator()
    test_map()