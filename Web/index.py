# coding: utf-8
import json
import cgi
from FonctionHtml import GenerateurDivMain, LectureJson, Top10

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))
# https://codepen.io/cb2307/pen/XYxyeY

# dataTopSeed = LectureJson("C:/Users/florent/Documents/Ygg0702/Section.json")
dataTopSeed = LectureJson("C:/Users/FlorentBUCHET/Documents/ygg-lib/Data/Section.json")

header = """<!-- HEADER -->
    <header>
      <div class="netflixLogo">
        <a id="logo" href="#home"><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/logo.PNG?raw=true" alt="Logo Image"></a>
      </div>      
      <nav class="main-nav">                
        <a href="#home">Home</a>
        <a href="#tvShows">TV Shows</a>
        <a href="#movies">Movies</a>
        <a href="#originals">Originals</a>
        <a href="#">Recently Added</a>
        <a target="_blank" href="https://codepen.io/cb2307/full/NzaOrm">Portfolio</a>        
      </nav>
      <nav class="sub-nav">
        <a href="#"><i class="fas fa-search sub-nav-logo"></i></a>
        <a href="#"><i class="fas fa-bell sub-nav-logo"></i></a>
        <a href="#">Account</a>        
      </nav>      
    </header>
    <!-- END OF HEADER -->"""
    
links = """
    <section class="link">
      <div class="logos">
        <a href="#"><i class="fab fa-facebook-square fa-2x logo"></i></a>
        <a href="#"><i class="fab fa-instagram fa-2x logo"></i></a>
        <a href="#"><i class="fab fa-twitter fa-2x logo"></i></a>
        <a href="#"><i class="fab fa-youtube fa-2x logo"></i></a>
      </div>
      <div class="sub-links">
        <ul>
          <li><a href="#">Audio and Subtitles</a></li>
          <li><a href="#">Audio Description</a></li>
          <li><a href="#">Help Center</a></li>
          <li><a href="#">Gift Cards</a></li>
          <li><a href="#">Media Center</a></li>
          <li><a href="#">Investor Relations</a></li>
          <li><a href="#">Jobs</a></li>
          <li><a href="#">Terms of Use</a></li>
          <li><a href="#">Privacy</a></li>
          <li><a href="#">Legal Notices</a></li>
          <li><a href="#">Corporate Information</a></li>
          <li><a href="#">Contact Us</a></li>
        </ul>
      </div>
    </section>"""

divMainContainer = """
<div class="location" id="home">
          <h1 id="home">Popular on Netflix</h1>
          <div class="box">
            <a href="https://www3.yggtorrent.qa/torrent/filmvid%C3%A9o/animation/511693-the+lion+king+2019+multi+truefrench+1080p+hdlight+x264+ac3-toxic+le+roi+lion"><img src="https://fr.web.img3.acsta.net/pictures/22/09/20/12/10/2512840.jpg" alt="Roi Lion"></a>
            <a href="https://www3.yggtorrent.qa/torrent/film-video/animation/332344-coco+2017+multi+3+1080p+bluray+light+x264+ac3+5+1-tg"><img src="https://lumiere-a.akamaihd.net/v1/images/p_coco_19736_fd5fa537.jpeg?region=0,0,540,810" alt=""></a>       
          </div>
      </div>
"""

footer = """
    <footer>
      <p>&copy 1997-2018 Netflix, Inc.</p>
      <p>Carlos Avila &copy 2018</p>
    </footer>
"""

with open('style.css', 'r') as file:
    css_content = file.read()

head = """
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Netflix</title>
  <style>"""+css_content+"""</style>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js" integrity="sha384-3LK/3kTpDE/Pkp8gTNp2gR/2gOiwQ6QaO7Td0zV76UFJVhqLl4Vl3KL1We6q6wR9" crossorigin="anonymous"></script>

  <script src="main.js"></script>
</head>"""

Top50Seed = GenerateurDivMain(dataTopSeed,'Top des torrents telecharge')
Top10Seed = Top10(dataTopSeed, 'Top 10 des seeds')

html = """<html>
"""+head+"""
<body>
  <div class="wrapper">

"""+header+"""
    
    <!-- MAIN CONTAINER -->
    <section class="main-container" >
    """+Top50Seed+"""
    
    <!-- LINKS -->
"""+links+"""

    <!-- FOOTER -->
"""+footer+"""
  </div>
</body>
</html>
"""

print(html)