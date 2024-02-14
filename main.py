from GetUrl.OfficialYGG import GetUrl
from GetName.TorrentName import GetNames, FindImageGoogle
from GetName.TraitementChaine import SuppressionCharVide
from GetName.TorrentSeedLeech import GetSeedLeech
from Web.FonctionHtml import GenerateurDivMain

import json

if __name__ == '__main__':
    
    # A refaire car l'URL ne fonctionne pas pour la requete
    # YggUrl = GetUrl()
    # print(YggUrl)
    
    TorrentName = input('Entrez votre torrent recherché : ')
    TorrentCategory = input('Entrez votre categorie : ')
    
    DictNames = GetNames(name=TorrentName,description='',file='',uploader='',category=TorrentCategory,sub_category='',order='',sort='seed',page=0)
    
    print(f"Vous avez trouvé '{len(DictNames)}' torrents ")
    print(DictNames)
    
    with open("./Data/Section.json", "w") as f:
        json.dump(DictNames, f)