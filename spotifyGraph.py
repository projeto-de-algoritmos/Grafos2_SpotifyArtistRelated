import requests
import urllib.parse
from operator import attrgetter


token = "Bearer"
id = ''
artistName = ''
firstArtists = []
secondArtists = []
idFirst = []


def userInput():
    print('Descubra seu grafo de artistas relacionados!')
    artistName = input('Qual artista gostaria de pesquisar?\n')
    artistName = urllib.parse.quote(artistName)
    return artistName


def getId(name):
    request = requests.get("https://api.spotify.com/v1/search?q=" + name + "&type=artist",
                           headers={"content-type": "application/json", "Authorization": token})
    request = request.json()
    id = request['artists']['items'][0]['id']
    return id


def getRelatedArtists(idArtista):
    request = requests.get("https://api.spotify.com/v1/artists/" + idArtista + "/related-artists",
                           headers={"content-type": "application/json", "Authorization": token})
    request = request.json()
    for x in range(5):
        idFirst.append(request['artists'][x]['id'])
    for i in range(5):
        firstArtists.append(request['artists'][i]['name'])
    print(firstArtists)
    return firstArtists, idFirst


def getSecondRelatedArtists(id2Artista):
    for i in range(5):
        request = requests.get("https://api.spotify.com/v1/artists/" + id2Artista[i] + "/related-artists",
                               headers={"content-type": "application/json", "Authorization": token})
        request = request.json()
        for x in range(5):
            secondArtists.append(request['artists'][x]['name'])
    print(secondArtists)
    return secondArtists


artistName = userInput()
id = getId(artistName)
idFirst = getRelatedArtists(id)
getSecondRelatedArtists(idFirst[1])
