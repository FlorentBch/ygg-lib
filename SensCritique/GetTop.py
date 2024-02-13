import requests
# from GetUrl.RandomAgent import RandomAgent
from lxml.html import fromstring
from bs4 import BeautifulSoup
import json

# https://www.senscritique.com/films/tops/top111
# https://www.senscritique.com/series/streaming?universe=tvShow

def testFetch():

    url = 'https://apollo.senscritique.com/'

    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.8",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "referrer": "https://www.senscritique.com/",
        "referrerPolicy": "no-referrer-when-downgrade"
    }

    payload = {
        "operationName": "Top",
        "variables": {
            "limit": 111,
            "offset": 0,
            "subtype": "TOP_111",
            "universe": "movie"
        },
        "query": 'query Top($limit: Int, $offset: Int, $subtype: TopSubtype, $universe: String) { top(limit: $limit, offset: $offset, subtype: $subtype, universe: $universe) { ...ProductList synopsis albums(limit: 1) { ...ProductNano __typename } currentUserInfos { ...ProductUserInfos __typename } scoutsAverage { average count __typename } __typename }} fragment ProductList on Product { category channel dateRelease dateReleaseEarlyAccess dateReleaseJP dateReleaseOriginal dateReleaseUS displayedYear duration episodeNumber seasonNumber frenchReleaseDate id numberOfSeasons originalRun originalTitle rating slug subtitle title universe url yearOfProduction tvChannel { name url __typename } countries { id name __typename } gameSystems { id label __typename } medias { picture __typename } genresInfos { label __typename } artists { name person_id url __typename } authors { name person_id url __typename } creators { name person_id url __typename } developers { name person_id url __typename } directors { name person_id url __typename } pencillers { name person_id url __typename } stats { ratingCount __typename } __typename } fragment ProductNano on Product { id rating slug title universe url yearOfProduction medias(backdropSize: "1200") { backdrop picture screenshot __typename } __typename } fragment ProductUserInfos on ProductUserInfos { dateDone hasStartedReview isCurrent id isDone isListed isRecommended isReviewed isWished productId rating userId numberEpisodeDone lastEpisodeDone { episodeNumber id season { seasonNumber id episodes { title id episodeNumber __typename } __typename } __typename } gameSystem { id label __typename } review { author { id name __typename } url __typename } __typename }'
    }

    response = requests.post(url, headers=headers, json=[payload])

    if response.status_code == 200:
        data = response.json()
        # Traitement des données JSON ici
        # Enregistrez les données dans un fichier JSON
        with open('resultat.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    else:
        print("Erreur lors de la requête.")


def AllTopsFilms():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.9",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
    }
    
    payload = [
        {
            "operationName": "Polls",
            "variables": {
                "limit": 1000,
                "offset": 0,
                "sortBy": "ALL",
                "universe": "movie"
            },
            "query": "query Polls($limit: Int, $offset: Int, $sortBy: PollSortBy, $universe: String!) { polls(limit: $limit, offset: $offset, sortBy: $sortBy, universe: $universe) { limit offset total items { cover id label participationCount url listSubtype universe __typename } __typename } }"
        }
    ]

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('Tops.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'Tops.json'.")
    else:
        print("Erreur lors de la requête.")