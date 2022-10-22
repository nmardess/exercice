def nettoyage_caracteres(chaine: str) -> int:
    '''
    Suppression des caractères non numériques.

            Parameters:
                    chaine (str): Chaine de caractères à nettoyer.
            Returns:
                    entier (int): Entier contenu dans la chaine de caractères.
    '''
    entier = ''.join(filter(str.isdigit, chaine))
    return int(entier)

def eval_operation(operation: str) -> int:
    '''
    Evaluation d'une opération python

            Parameters:
                    operation (str): Chaine de caractères à évaluer.
            Returns:
                    resultat (int): Résultat entier de l'opération.
    '''
    try:
        resultat = int(eval(operation))
    except:
        print(f"Une erreur s'est produite lors de l'évaluation de l'opération: {operation}")
    else:
        return resultat

def resultat_ligne(operation: str) -> str:
    '''
    Résultat de la ligne à calculer, si c'est possible avec le détail de l'opération
    qui a permis ce calcul.

            Parameters:
                    operation (str): Chaine de caractères provenant du fichier.
            Returns:
                    resultat (str): Chaine de caractères précisant l'opération, son résultat
                                    et le détail du calcul.
    '''
    liste = operation.split()
    if len(liste) == 3:
        try:
            operande1 = nettoyage_caracteres(liste[0])
            operator = liste[1]
            operande2 = nettoyage_caracteres(liste[2])
            evaluation = eval_operation(str(operande1)+ str(operator)+ str(operande2))
            if evaluation:
                resultat = (f"Opération possible : {operation.strip()} ==> " \
                        f" {str(operande1)} {str(operator)} {str(operande2)} = {evaluation}")
            else:
                resultat = (f"Opération impossible : {operation.strip()}")
        except:
            print(f"Une autre erreur est survenue avec l'opération {operation.strip()}")
        else:
            return resultat
    else :
        return(f"Opération impossible : {operation.strip()}")
        
