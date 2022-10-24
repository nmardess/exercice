from utils import decorateur


def test_cosmetique():
    decoration = decorateur.cosmetique("test decorateur")(lambda x: x)
    decoration("test execution") == "test execution"
