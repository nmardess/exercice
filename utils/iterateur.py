from .calculs import resultat_ligne

class CalculLigne:
    '''
    Itérateur retournant chaque élément de la liste calculé.

            Parameters:
                    liste (list): Liste contenant les éléments à calculer

            Returns:
                    ligne (str): Ligne contenant l'élément calculé
    '''
    def __init__ (self, liste: list):
        self.liste = liste
        self.iteration = 0
        if type(self.liste) != list:
            print("Le paramètre doit être une liste")
            raise TypeError()
        self.taille_liste = len(self.liste)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iteration < self.taille_liste:
            ligne = self.liste[self.iteration]
            self.iteration += 1
            return resultat_ligne(ligne)
        else:
            raise StopIteration