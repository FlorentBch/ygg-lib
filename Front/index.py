# coding: utf-8
import json
import cgi
from FonctionHtml import GenerateurDivMain, LectureJson, Top10

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))
# https://codepen.io/cb2307/pen/XYxyeY

# dataTopSeed = LectureJson("C:/Users/florent/Documents/Ygg0702/Section.json")
dataTopSeed = LectureJson("C:/Users/FlorentBUCHET/Documents/ygg-lib/Section.json")

Top50Seed = GenerateurDivMain(dataTopSeed,'Top des torrents telecharge')
Top10Seed = Top10(dataTopSeed, 'Top 10 des seeds')

css = """<style>/* CSS VARIABLES */
:root {
  --primary: #141414;
  --light: #F3F3F3;
  --dark: 	#686868;
}

html, body {
  width: 100vw;
  min-height: 100vh;
  margin: 0;
  padding: 0;
  background-color: var(--primary);
  color: var(--light);
  font-family: Arial, Helvetica, sans-serif;
  box-sizing: border-box;
  line-height: 1.4;
}

img {
  max-width: 100%;
  max-height: 100%;
}

h1 {
  padding-top: 60px;  
}

.wrapper {
  margin: 0;
  padding: 0;
}

/* HEADER */
header {
  padding: 20px 20px 0 20px;
  position: fixed;
  top: 0;
  display: grid;  
  grid-gap:5px;
  grid-template-columns: 1fr 4fr 1fr;
  grid-template-areas: 
   "nt mn mn sb . . . "; 
  background-color: var(--primary);
  width: 100%;
  margin-bottom: 0px;  
}

.netflixLogo {
  grid-area: nt;
  object-fit: cover;
  width: 100px;
  max-height: 100%;
  
  padding-left: 30px;
  padding-top: 0px;  
}

.netflixLogo img {  
  height: 35px;     
}

#logo {
  color: #E50914;  
  margin: 0; 
  padding: 0; 
}


.main-nav {
  grid-area: mn;
  padding: 0 30px 0 20px;
}

.main-nav a {
  color: var(--light);
  text-decoration: none;
  margin: 5px;  
}

.main-nav a:hover {
  color: var(--dark);
}

.sub-nav {
  grid-area: sb;
  padding: 0 40px 0 40px;
}

.sub-nav a {
  color: var(--light);
  text-decoration: none;
  margin: 5px;
}

.sub-nav a:hover {
  color: var(--dark);
}


/* MAIN CONTIANER */
.main-container {
  padding: 50px;
}

.box {
  display: grid;
  grid-gap: 20px;
  grid-template-columns: repeat(6, minmax(100px, 1fr));
}

.box a {
  transition: transform .3s;  
}

.box a:hover {
  transition: transform .3s;
  -ms-transform: scale(1.4);
  -webkit-transform: scale(1.4);  
  transform: scale(1.4);
}

.box img {
  border-radius: 2px;
}

/* LINKS */
.link {
  padding: 50px;
}

.sub-links ul {
  list-style: none;
  padding: 0;
  display: grid;
  grid-gap: 20px;
  grid-template-columns: repeat(4, 1fr);
}

.sub-links a {
  color: var(--dark);
  text-decoration: none;
}

.sub-links a:hover {
  color: var(--dark);
  text-decoration: underline;
}

.logos a{
  padding: 10px;
}

.logo {
  color: var(--dark);
}


/* FOOTER */
footer {
  padding: 20px;
  text-align: center;
  color: var(--dark);
  margin: 10px;
}

/* MEDIA QUERIES */

@media(max-width: 900px) {

  header {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
    "nt nt nt  .  .  . sb . . . "
    "mn mn mn mn mn mn  mn mn mn mn";
  }

  .box {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(4, minmax(100px, 1fr));
  }

}

@media(max-width: 700px) {

  header {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas: 
    "nt nt nt  .  .  . sb . . . "
    "mn mn mn mn mn mn  mn mn mn mn";
  }

  .box {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(3, minmax(100px, 1fr));
  }

  .sub-links ul {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(3, 1fr);
  }
   
}

@media(max-width: 500px) {

  .wrapper {
    font-size: 15px;
  }

  header {
    margin: 0;
    padding: 20px 0 0 0;
    position: static;
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(1, 1fr);
    grid-template-areas: 
    "nt"    
    "mn"
    "sb";
    text-align: center;
  }

  .netflixLogo {
    max-width: 100%;
    margin: auto;
    padding-right: 20px;
  }

  .main-nav {
    display: grid;
    grid-gap: 0px;
    grid-template-columns: repeat(1, 1fr);
    text-align: center;
  }

  h1 {
    text-align: center;
    font-size: 18px;
  }

  .box {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(1, 1fr);
    text-align: center;    
  }

  .box a:hover {
    transition: transform .3s;
    -ms-transform: scale(1);
    -webkit-transform: scale(1);  
    transform: scale(1.2);
  }

  .logos {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(2, 1fr);
    text-align: center;
  }

  .sub-links ul {
    display: grid;
    grid-gap: 20px;
    grid-template-columns: repeat(1, 1fr);
    text-align: center;
    font-size: 15px;
  }
}</style> """

divMainContainer = """
<div class="location" id="home">
          <h1 id="home">Popular on Netflix</h1>
          <div class="box">
            <a href="https://www3.yggtorrent.qa/torrent/filmvid%C3%A9o/animation/511693-the+lion+king+2019+multi+truefrench+1080p+hdlight+x264+ac3-toxic+le+roi+lion"><img src="https://fr.web.img3.acsta.net/pictures/22/09/20/12/10/2512840.jpg" alt="Roi Lion"></a>
            <a href="https://www3.yggtorrent.qa/torrent/film-video/animation/332344-coco+2017+multi+3+1080p+bluray+light+x264+ac3+5+1-tg"><img src="https://lumiere-a.akamaihd.net/v1/images/p_coco_19736_fd5fa537.jpeg?region=0,0,540,810" alt=""></a>       
          </div>
      </div>
"""

html = """<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Netflix</title>
  """+css+"""
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js" integrity="sha384-3LK/3kTpDE/Pkp8gTNp2gR/2gOiwQ6QaO7Td0zV76UFJVhqLl4Vl3KL1We6q6wR9" crossorigin="anonymous"></script>

  <script src="main.js"></script>
</head>
<body>
  <div class="wrapper">

    <!-- HEADER -->
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
    <!-- END OF HEADER -->
    
    <!-- MAIN CONTAINER -->
    <section class="main-container" >
    """+Top50Seed+"""
    
    <!-- END OF MAIN CONTAINER -->

    <!-- LINKS -->
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
    </section>
    <!-- END OF LINKS -->

    <!-- FOOTER -->
    <footer>
      <p>&copy 1997-2018 Netflix, Inc.</p>
      <p>Carlos Avila &copy 2018</p>
    </footer>
  </div>
</body>
</html>
"""

print(html)