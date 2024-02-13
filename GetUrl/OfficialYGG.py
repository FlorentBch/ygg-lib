import requests
from lxml.html import fromstring
from GetUrl.RandomAgent import RandomAgent

def GetUrl()->str:
    """Récupere l'URL officiel de YGGTorrent via Wikipédia

    Returns:
        str: URL de Ygg
    """
    WikiUrl = 'https://fr.wikipedia.org/wiki/YggTorrent'  # Replace with the desired URL
    WikiResponse = requests.get(WikiUrl, RandomAgent())

    soup = fromstring(WikiResponse.text)

    # Select elements using XPath
    FetchUrl = soup.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[4]/td/span/a')  # Replace with your XPath expression

    YggUrl = 'Pas de valeur'
    # Iterate over the selected elements
    for element in FetchUrl:
        YggUrl = element.get('href')
    
    return YggUrl