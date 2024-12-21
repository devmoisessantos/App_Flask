import urllib.request
import json

def result_filmes(tipo):
    if \
        tipo == 'Mais Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3e76f25f7d1073ddc33de64aa8e881a8'
    elif \
        tipo == 'Mais Votados':
        url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3e76f25f7d1073ddc33de64aa8e881a8'
    elif \
        tipo == 'Ano 2010':
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=3e76f25f7d1073ddc33de64aa8e881a8'
    else:
        return []

    # Fazendo a requisição HTTP
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    dados_json = json.loads(dados)

    # Arredondando os valores de 'vote_average'
    for filme in dados_json['results']:
        filme['vote_average'] = round(filme['vote_average'], 1)

    return dados_json['results']
