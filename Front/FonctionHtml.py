import json
import requests

def GenerateurDivMain(infos:dict, Titre:str):
    
    divMain ="""
        <div class="location" id="home">
            <h1 id="home">"""+Titre+"""</h1>
            <div class="box">
    """
    
    for key, value in infos.items():
        divMain += """<a href=\""""+value['url']+"""\"><img src=\""""+value['img']+"""\" alt=\""""+key+"""\"></a>"""
    
    divMain+="""</div></div>"""
    
    return divMain

def Top10(Infos:dict, Titre:str):
    divMain ="""
        <div class="location" id="home">
            <h1 id="home">"""+Titre+"""</h1>
            <div class="box">
    """ 
    # Utiliser enumerate pour limiter à 10 films
    for index, (titre, details) in enumerate(Infos.items()):
        divMain += """<a href=\""""+details['url']+"""\"><img src=\""""+details['img']+"""\" alt=\"https://fr.web.img3.acsta.net/pictures/22/09/20/12/10/2512840.jpg\"></a>"""
        if index == 9:  # Arrêter après les 10 premiers films
            break

    divMain+="""</div></div>"""
    
    return divMain

def LectureJson(path:str):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
    
# URL la plus courte pour parcourir google image -> https://www.google.com/search?q=anatomie+dune+chute&tbm=isch