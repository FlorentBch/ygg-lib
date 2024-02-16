import json

def MappageCategories(Code:str)->str:
    """Mappage entre le dictionnaire de valeurs des categories et le code donnée

    Args:
        Code (str): Code de la categorie (2144)

    Returns:
        str: Texte de la categorie (Application)
    """
    
    with open("./Data/Categories.json", encoding='utf-8') as f:
        data = json.load(f)
    
    for cat in data['categories']:
            # Vérifier si la catégorie existe
        if Code == cat['valeur']:
            return cat['texte']
            
    sous_categories = data.get("sousCategories", {})

    for categorie, sous_cat_list in sous_categories.items():
        for sous_cat in sous_cat_list:
            if sous_cat["valeur"] == Code:
                return sous_cat["texte"]
            

def TrouverCode(categorie_texte: str) -> str:
    """Trouver le code à partir du texte de la catégorie

    Args:
        categorie_texte (str): Texte de la catégorie (par exemple, "Application")

    Returns:
        str: Code de la catégorie (par exemple, "2144")
    """
    with open("./Data/Categories.json", encoding='utf-8') as f:
        data = json.load(f)
    
    for cat in data['categories']:
        # Vérifier si le texte de la catégorie correspond
        if categorie_texte == cat['texte']:
            return cat['valeur']
    
    sous_categories = data.get("sousCategories", {})

    for categorie, sous_cat_list in sous_categories.items():
        for sous_cat in sous_cat_list:
            if sous_cat["texte"] == categorie_texte:
                return sous_cat["valeur"]
    
    # Si la catégorie n'est pas trouvée, vous pouvez retourner une valeur par défaut ou lever une exception selon le cas.
    return "Code non trouvé"
