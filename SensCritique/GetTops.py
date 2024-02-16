import requests
# from GetUrl.RandomAgent import RandomAgent
from lxml.html import fromstring
from bs4 import BeautifulSoup
import json

# https://www.senscritique.com/films/tops/top111
# https://www.senscritique.com/series/streaming?universe=tvShow

def stripCharPath(chaine):
    nouvelle_chaine = chaine.replace('/', ' & ')
    nouvelle_chaine = nouvelle_chaine.replace('"', '')
    return nouvelle_chaine

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
        with open('./Data/resultat.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    else:
        print("Erreur lors de la requête.")

def FetchListTopsFilms():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "Polls",
        "variables": {
            "limit": 10000,
            "offset": 0,
            "sortBy": "ALL",
            "universe": "movie"
        },
        "query": """
            query Polls($limit: Int, $offset: Int, $sortBy: PollSortBy, $universe: String!) { 
                polls(limit: $limit, offset: $offset, sortBy: $sortBy, universe: $universe) { 
                    limit 
                    offset 
                    total 
                    items { 
                        cover 
                        id 
                        label 
                        url
                    } 
                } 
            }
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_ListTopsFilms.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_ListTopsFilms.json'.")
    else:
        print("Erreur lors de la requête.")

def FetchListTopsGames():
    
    url = "https://apollo.senscritique.com/"
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }

    data = {
        "operationName": "Polls",
        "variables": {"limit": 10000, "offset": 0, "sortBy": "ALL", "universe": "game"},
        "query": """
            query Polls($limit: Int, $offset: Int, $sortBy: PollSortBy, $universe: String!) {
                polls(limit: $limit, offset: $offset, sortBy: $sortBy, universe: $universe) {
                    limit
                    offset
                    total
                    items {
                        cover
                        id
                        label
                        participationCount
                        url
                    }
                }
            }
        """
    }
    
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_ListTopsJeuxVideo.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_ListTopsJeuxVideo.json'.")
    else:
        print("Erreur lors de la requête.")

def FetchListTopsSeries():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "Polls",
        "variables": {
            "limit": 10000,
            "offset": 0,
            "sortBy": "ALL",
            "universe": "tvShow"
        },
        "query": """
            query Polls($limit: Int, $offset: Int, $sortBy: PollSortBy, $universe: String!) { polls(limit: $limit, offset: $offset, sortBy: $sortBy, universe: $universe) { limit offset total items { cover id label url }  } }"""
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_TopsSeries.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_TopsSeries.json'.")
    else:
        print("Erreur lors de la requête.")

def FetchAllStreaming():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "StreamingExplorer",
        "variables": {
            "subtype": "tvShow",
            "providers": None,
            "onlyWish": False,
            "hideSeen": False,
            "onlyPopular": True,
            "lastWeek": False,
            "lastMonth": False,
            "genres": None,
            "countries": None,
            "yearDateRelease": None,
            "duration": None,
            "rating": None,
            "order": "POPULARITY_DESC",
            "seasons": None,
            "offset": 0,
            "limit": 10000
        },
        "query": """
            query StreamingExplorer($providers: [Int], $genres: [Int], $lastWeek: Boolean, $lastMonth: Boolean, $yearDateRelease: [Int], $duration: [Int], $rating: [Int], $onlyWish: Boolean, $hideSeen: Boolean, $countries: [Int], $subtype: String!, $limit: Int, $offset: Int, $onlyPopular: Boolean, $order: StreamingSort, $seasons: [Int]) {
                streamingExplorer(
                    providers: $providers,
                    genres: $genres,
                    lastWeek: $lastWeek,
                    lastMonth: $lastMonth,
                    yearDateRelease: $yearDateRelease,
                    duration: $duration,
                    rating: $rating,
                    onlyWish: $onlyWish,
                    hideSeen: $hideSeen,
                    countries: $countries,
                    subtype: $subtype,
                    limit: $limit,
                    offset: $offset,
                    onlyPopular: $onlyPopular,
                    order: $order,
                    seasons: $seasons
                ) {
                    myProviders {
                        ...MyProviders
                        
                    }
                    filters {
                        period {
                            min
                            max
                            
                        }
                        genres {
                            id
                            name
                            
                        }
                        countries {
                            id
                            name
                            
                        }
                        providers {
                            id
                            name
                            tablePrefix
                            
                        }
                        
                    }
                    products {
                        ...ProductNano
                        scoutsAverage {
                            average
                            
                        }
                        currentUserInfos {
                            ...ProductUserInfos
                            
                        }
                        providers {
                            providerId
                            name
                            webUrl
                            
                        }
                        
                    }
                    total
                    
                }
            }

            fragment ProductNano on Product {
                id
                rating
                title
                universe
                url
                yearOfProduction
                medias(backdropSize: "1200") {
                    backdrop
                    picture
                    
                    
                }
                
            }

            fragment ProductUserInfos on ProductUserInfos {
                dateDone
                hasStartedReview
                isCurrent
                id
                isDone
                isListed
                isRecommended
                isReviewed
                isWished
                productId
                rating
                userId
                numberEpisodeDone
                lastEpisodeDone {
                    episodeNumber
                    id
                    season {
                        seasonNumber
                        id
                        episodes {
                            title
                            id
                            episodeNumber
                            
                        }
                        
                    }
                    
                }
                gameSystem {
                    id
                    label
                    
                }
                review {
                    author {
                        id
                        name
                        
                    }
                    url
                    
                }
                
            }

            fragment MyProviders on MyProviders {
                id
                providersIds
                
            }
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_StreamingExplorerSeries.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_StreamingExplorerSeries.json'.")
    else:
        print("Erreur lors de la requête.")

def FetchWeeklyStreaming():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "StreamingExplorer",
        "variables": {
            "subtype": "tvShow",
            "providers": None,
            "onlyWish": False,
            "hideSeen": False,
            "onlyPopular": True,
            "lastWeek": True,
            "lastMonth": False,
            "genres": None,
            "countries": None,
            "yearDateRelease": None,
            "duration": None,
            "rating": None,
            "order": "POPULARITY_DESC",
            "seasons": None,
            "offset": 0,
            "limit": 10000
        },
        "query": """
            query StreamingExplorer(
                $providers: [Int],
                $genres: [Int],
                $lastWeek: Boolean,
                $lastMonth: Boolean,
                $yearDateRelease: [Int],
                $duration: [Int],
                $rating: [Int],
                $onlyWish: Boolean,
                $hideSeen: Boolean,
                $countries: [Int],
                $subtype: String!,
                $limit: Int,
                $offset: Int,
                $onlyPopular: Boolean,
                $order: StreamingSort,
                $seasons: [Int]
            ) {
                streamingExplorer(
                    providers: $providers,
                    genres: $genres,
                    lastWeek: $lastWeek,
                    lastMonth: $lastMonth,
                    yearDateRelease: $yearDateRelease,
                    duration: $duration,
                    rating: $rating,
                    onlyWish: $onlyWish,
                    hideSeen: $hideSeen,
                    countries: $countries,
                    subtype: $subtype,
                    limit: $limit,
                    offset: $offset,
                    onlyPopular: $onlyPopular,
                    order: $order,
                    seasons: $seasons
                ) {
                    myProviders {
                        ...MyProviders
                        __typename
                    }
                    filters {
                        period {
                            min
                            max
                            __typename
                        }
                        genres {
                            id
                            name
                            __typename
                        }
                        countries {
                            id
                            name
                            __typename
                        }
                        providers {
                            id
                            name
                            tablePrefix
                            __typename
                        }
                        __typename
                    }
                    products {
                        ...ProductNano
                        scoutsAverage {
                            average
                            __typename
                        }
                        currentUserInfos {
                            ...ProductUserInfos
                            __typename
                        }
                        providers {
                            providerId
                            name
                            webUrl
                            __typename
                        }
                        __typename
                    }
                    total
                    __typename
                }
            }
            
            fragment ProductNano on Product {
                id
                rating
                slug
                title
                universe
                url
                yearOfProduction
                medias(backdropSize: "1200") {
                    backdrop
                    picture
                    screenshot
                    __typename
                }
                __typename
            }
            
            fragment ProductUserInfos on ProductUserInfos {
                dateDone
                hasStartedReview
                isCurrent
                id
                isDone
                isListed
                isRecommended
                isReviewed
                isWished
                productId
                rating
                userId
                numberEpisodeDone
                lastEpisodeDone {
                    episodeNumber
                    id
                    season {
                        seasonNumber
                        id
                        episodes {
                            title
                            id
                            episodeNumber
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                gameSystem {
                    id
                    label
                    __typename
                }
                review {
                    author {
                        id
                        name
                        __typename
                    }
                    url
                    __typename
                }
                __typename
            }
            
            fragment MyProviders on MyProviders {
                id
                providersIds
                __typename
            }
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_WeeklyStreaming.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_WeeklyStreaming.json'.")
    else:
        print("Erreur lors de la requête.")

def FetchMonthlyStreaming():
    url = "https://apollo.senscritique.com/"
    
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "authorization": "null",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "StreamingExplorer",
        "variables": {
            "subtype": "tvShow",
            "providers": None,
            "onlyWish": False,
            "hideSeen": False,
            "onlyPopular": True,
            "lastWeek": False,
            "lastMonth": True,
            "genres": None,
            "countries": None,
            "yearDateRelease": None,
            "duration": None,
            "rating": None,
            "order": "POPULARITY_DESC",
            "seasons": None,
            "offset": 0,
            "limit": 10000
        },
        "query": """
            query StreamingExplorer(
                $providers: [Int],
                $genres: [Int],
                $lastWeek: Boolean,
                $lastMonth: Boolean,
                $yearDateRelease: [Int],
                $duration: [Int],
                $rating: [Int],
                $onlyWish: Boolean,
                $hideSeen: Boolean,
                $countries: [Int],
                $subtype: String!,
                $limit: Int,
                $offset: Int,
                $onlyPopular: Boolean,
                $order: StreamingSort,
                $seasons: [Int]
            ) {
                streamingExplorer(
                    providers: $providers,
                    genres: $genres,
                    lastWeek: $lastWeek,
                    lastMonth: $lastMonth,
                    yearDateRelease: $yearDateRelease,
                    duration: $duration,
                    rating: $rating,
                    onlyWish: $onlyWish,
                    hideSeen: $hideSeen,
                    countries: $countries,
                    subtype: $subtype,
                    limit: $limit,
                    offset: $offset,
                    onlyPopular: $onlyPopular,
                    order: $order,
                    seasons: $seasons
                ) {
                    myProviders {
                        ...MyProviders
                        __typename
                    }
                    filters {
                        period {
                            min
                            max
                            __typename
                        }
                        genres {
                            id
                            name
                            __typename
                        }
                        countries {
                            id
                            name
                            __typename
                        }
                        providers {
                            id
                            name
                            tablePrefix
                            __typename
                        }
                        __typename
                    }
                    products {
                        ...ProductNano
                        scoutsAverage {
                            average
                            __typename
                        }
                        currentUserInfos {
                            ...ProductUserInfos
                            __typename
                        }
                        providers {
                            providerId
                            name
                            webUrl
                            __typename
                        }
                        __typename
                    }
                    total
                    __typename
                }
            }
            
            fragment ProductNano on Product {
                id
                rating
                slug
                title
                universe
                url
                yearOfProduction
                medias(backdropSize: "1200") {
                    backdrop
                    picture
                    screenshot
                    __typename
                }
                __typename
            }
            
            fragment ProductUserInfos on ProductUserInfos {
                dateDone
                hasStartedReview
                isCurrent
                id
                isDone
                isListed
                isRecommended
                isReviewed
                isWished
                productId
                rating
                userId
                numberEpisodeDone
                lastEpisodeDone {
                    episodeNumber
                    id
                    season {
                        seasonNumber
                        id
                        episodes {
                            title
                            id
                            episodeNumber
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                gameSystem {
                    id
                    label
                    __typename
                }
                review {
                    author {
                        id
                        name
                        __typename
                    }
                    url
                    __typename
                }
                __typename
            }
            
            fragment MyProviders on MyProviders {
                id
                providersIds
                __typename
            }
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Enregistrez les données dans un fichier JSON
        with open('./Data/SC_MonthlyStreaming.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        print("Les données ont été enregistrées avec succès dans 'SC_MonthlyStreaming.json'.")
    else:
        print("Erreur lors de la requête.")

def ScrapIntegralite():
    FetchListTopsFilms()
    FetchAllStreaming()
    FetchListTopsGames()
    FetchMonthlyStreaming()
    FetchWeeklyStreaming()

def FetchPoll(id):
    url = "https://apollo.senscritique.com/"
    
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
        "sec-gpc": "1"
    }
    
    payload = {
        "operationName": "Poll",
        "variables": {
            "id": id,
            "limit": 10000,
            "offset": 0
        },
        "query": """
            query Poll($id: Int!, $limit: Int, $offset: Int) {
                poll(id: $id) {
                    alternativeTitle
                    cover
                    description
                    id
                    label
                    participationCount
                    participationScoutsCount
                    universe
                    url
                    minimalProducts {
                        id
                        title
                        url
                    }
                    products(limit: $limit, offset: $offset) {
                        ...ProductList
                        albums(limit: 1) {
                            ...ProductNano
                        }
                        currentUserInfos {
                            ...ProductUserInfos
                        }
                        polls(currentPollId: $id, limit: 11) {
                            poll {
                                id
                                label
                                url
                            }
                        }
                        scoutsAverage {
                            average
                            count
                        }
                    }
                    userAnswer {
                        id
                        url
                        productCount
                    }
                    completionPercentage
                    badge {
                        id
                        label
                        image
                    }
                }
            }

            fragment ProductList on Product {
                category
                channel
                dateRelease
                displayedYear
                duration
                episodeNumber
                seasonNumber
                frenchReleaseDate
                id
                numberOfSeasons
                rating
                slug
                subtitle
                title
                universe
                url
                yearOfProduction
                tvChannel {
                    name
                    url
                }
                countries {
                    id
                    name
                }
                medias {
                    picture
                }
                genresInfos {
                    label
                }
                directors {
                    name
                    person_id
                    url
                }
                stats {
                    ratingCount
                }
            }

            fragment ProductNano on Product {
                id
                rating
                slug
                title
                universe
                url
                yearOfProduction
                medias(backdropSize: "1200") {
                    backdrop
                    picture
                }
            }

            fragment ProductUserInfos on ProductUserInfos {
                dateDone
                hasStartedReview
                isCurrent
                id
                isDone
                isListed
                isRecommended
                isReviewed
                isWished
                productId
                rating
                userId
                numberEpisodeDone
                lastEpisodeDone {
                    episodeNumber
                    id
                    season {
                        seasonNumber
                        id
                        episodes {
                            title
                            id
                            episodeNumber
                        }
                    }
                }
                review {
                    author {
                        id
                        name
                    }
                    url
                }
            }
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        NomFichier = data['data']['poll']['label']
        
        if NomFichier.count('/') > 0 or NomFichier.count('"') > 0:
            NomFichier = stripCharPath(NomFichier)
            
        NamePath = './Data/Top Films SC/SC_'+NomFichier+'.json'
        # Enregistrez les données dans un fichier JSON
        with open(NamePath, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        return ("Les données ont été enregistrées avec succès dans "+NomFichier)
    
def testAllPoll():
    with open("C:/Users/Florent/Documents/ygg-lib/Data/SC_ListTopsFilms.json", encoding='utf-8') as f:
        data = json.load(f)
    totalItems = data['data']['polls']['total']
    for i in range(totalItems):
        ListData = data['data']['polls']['items'][i]['id']
        print(str(i)+"/"+str(totalItems)+" : "+FetchPoll(ListData))

FetchListTopsFilms()
# FetchPoll(2457925)
testAllPoll()



                # {
                #     "cover": "https://media.senscritique.com/media/media/000018636959/480x0/cover.jpg",
                #     "id": 2457925, / 1006181
                #     "label": "Les films avec la meilleure ambiance/atmosphère",
                #     "url": "/top/resultats/les_films_avec_la_meilleure_ambiance_atmosphere/2457925"
                # },
                # Gerer le cas du slash (/) dans le nom du label