import requests
from lxml.html import fromstring
from GetUrl.RandomAgent import RandomAgent
from GetName.TraitementChaine import SuppressionCharVide

def GetSeedLeech(name:str,description:str,file:str,uploader:str,category:str,sub_category:str,order:str,sort:str,page:int)->dict:
    """Retourne les noms et URL des torrents par page

    Args:
        name (str): Nom du torrent
        description (str): description du torrent
        file (str): _description_
        uploader (str): Nom de l'uploader
        category (str): Categorie du torrent
        sub_category (str): Sous-categorie du torrent
        order (str): Trie par Desc ou Asc
        sort (str): Trie sur quel paramètre (seed, leech, etc)
        page (int): Nombre de film au total (50 par page)

    Returns:
        dict: Dictionnaire de clés/ Valeurs (Nom du torrent/ URL du torrent)
    """

    Url = 'https://www3.yggtorrent.qa/engine/search?name='+name+\
                                                        '&description='+description+\
                                                            '&file='+file+\
                                                                '&uploader'+uploader+\
                                                                    '&category='+category+\
                                                                        '&sub_category='+sub_category+\
                                                                            '&do=search&order='+order+\
                                                                                '&sort='+sort+\
                                                                                    '&page='+str(page)
    YggDict = {}
    CleanDict = {}
    YggResponse = requests.get(Url, RandomAgent())
    
    soup = fromstring(YggResponse.text)

    FetchUrl = soup.xpath('//*[@id="#torrents"]/div/table/tbody/tr/td[8]')

    for element in FetchUrl:
        print(element.text)

    CleanDict = SuppressionCharVide(YggDict)
    
    return CleanDict
