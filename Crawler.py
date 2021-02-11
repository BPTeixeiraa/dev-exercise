#!/usr/bin/python
#*****************************************************************************************************************************************************
# Linguagem ..........: Python
# Criado por..........: Bruno Teixeira
# Data da Criação.....: 10/02/2021
# Exercicios...........: Crie um crawler (aplicação de busca de informação na web) que leia as 3 primeiras notícias
# do site g1.globo.com e organize em um JSON contendo o título, subtitulo (se tiver) e url da imagem de destaque (se tiver).
# Não utilize bibliotecas automáticas (scrappy ou similares)
#*****************************************************************************************************************************************************


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html = urlopen("https://g1.globo.com/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    tags = res.findAll("div", {"class": "bastian-feed-item"})
    noticias = []
    for tag in tags[:3]:
        titulo = tag.findAll("a", {"class": "feed-post-link"})
        subtitulo = tag.findAll("div", {"class": "feed-post-body-resumo"})
        noticias.append({'Titulo': titulo[0].get_text() if titulo else None, 'Subtitulo': subtitulo[0].get_text() if subtitulo else None, 'Url': titulo[0].get('href') if titulo else None})
    print (noticias)