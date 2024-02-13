import requests
from lxml.html import fromstring
from GetUrl.RandomAgent import RandomAgent
from GetName.TraitementChaine import SuppressionCharVide
from GetName.TraitementCategories import MappageCategories, TrouverCode
from bs4 import BeautifulSoup

def FindImageGoogle(Titre:str):

    url = 'https://www.google.com/search?q='+Titre+'&tbm=isch'
    YggResponse = requests.get(url, RandomAgent())
    
    soup = BeautifulSoup(YggResponse.text, 'lxml')

    # Trouver la balise img (vous pouvez ajuster cette recherche en fonction de la structure HTML de la page)
    img_tag = soup.find_all('img')

    # Extraire l'URL de l'attribut 'src' de la balise img
    if img_tag:
        img_url = img_tag[1].get('src')
        print("URL de l'image:", img_url)
    else:
        print("Aucune balise img trouvée sur la page.")
    
    return img_url

def GetNames(name:str,description:str,file:str,uploader:str,category:str,sub_category:str,order:str,sort:str,page:int)->dict:
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
    
    FetchUrl = soup.xpath('//*[@id="torrent_name"]')
    i = 0
    
    for element in FetchUrl:
        
        FetchSeed = soup.xpath('//*[@id="#torrents"]/div/table/tbody/tr/td[8]')
        FetchLeech = soup.xpath('//*[@id="#torrents"]/div/table/tbody/tr/td[9]')
        FetchCategory = soup.xpath('//*[@id="#torrents"]/div/table/tbody/tr/td[1]/div')
        SrcImg = FindImageGoogle(str(element.text).rstrip())      
        
        if int(FetchSeed[i].text) > 0:
            YggDict[element.text] = {'url':element.get('href'),'category': MappageCategories(str(FetchCategory[i].text)) ,'seed':FetchSeed[i].text,'leech':FetchLeech[i].text, 'img':SrcImg}

        i+=1

    CleanDict = SuppressionCharVide(YggDict)
    print(Url)
    return CleanDict