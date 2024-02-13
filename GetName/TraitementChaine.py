def SuppressionCharVide(Dictionnaire: dict)->dict:
    
    nouveau_dictionnaire = {}
    
    for cle, valeur in Dictionnaire.items():
        cle_modifiee = cle.rstrip()
        nouveau_dictionnaire[cle_modifiee] = valeur
    return nouveau_dictionnaire