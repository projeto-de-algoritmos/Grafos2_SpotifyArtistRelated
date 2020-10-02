import plotly.graph_objects as go
import plotly.express as px
import array as arr
import requests
import urllib.parse
from operator import attrgetter


teste = [1, 2, 3],
x_val = arr.array('i', [10, 15, 20, 150, 22, 80, 66]),
y_val = [10, 15, 20, 150, 80, 17, 37],
y_value = [20, 30],
token = "Bearer "
id = ''
artistName = ''
name = []
firstArtists = []
secondArtists = []
idFirst = []
checkArtist = []
idCheck = []
artistComparison = []
artistComparisonID = []
firstRelated = []
secondRelated = []
thirdRelated = []
fouthRelated = []
fithRelated = []
compFinal = []
teste = 1


def userInput():
    print('Descubra seu grafo de artistas relacionados!')
    artistName = input('Qual artista gostaria de pesquisar?\n')
    return artistName


def getId(name):
    name = urllib.parse.quote(name)
    request = requests.get("https://api.spotify.com/v1/search?q=" + name + "&type=artist",
                           headers={"content-type": "application/json", "Authorization": token})
    request = request.json()
    id = request['artists']['items'][0]['id']
    artistComparison.append(name)
    idCheck.append(request['artists']['items'][0]['id'])
    return id


def getRelatedArtists(idArtista):
    request = requests.get("https://api.spotify.com/v1/artists/" + idArtista + "/related-artists",
                           headers={"content-type": "application/json", "Authorization": token})
    request = request.json()
    for x in range(5):
        idFirst.append(request['artists'][x]['id'])
        idCheck.append(request['artists'][x]['id'])
        artistComparison.append(request['artists'][x]['name'])
        artistComparisonID.append(x)
    for i in range(5):
        firstArtists.append(request['artists'][i]['name'])
    return firstArtists, idFirst


def getSecondRelatedArtists(id2Artista):
    for i in range(5):
        request = requests.get("https://api.spotify.com/v1/artists/" + id2Artista[i] + "/related-artists",
                               headers={"content-type": "application/json", "Authorization": token})
        request = request.json()
        for x in range(20):
            if(request['artists'][x]['name'] in artistComparison):
                artistComparison.append(request['artists'][x]['name'])
                artistComparisonID.append(x)
            if(request['artists'][x]['id'] not in idCheck):
                idCheck.append(request['artists'][x]['id'])
                secondArtists.append(request['artists'][x]['name'])
    return secondArtists


def getFellowBands(id, name):
    name.pop(0)
    nameLen = len(name)
    idLen = len(id)
    count = 0

    for i in range(nameLen - 1):
        if(id[i+1] > id[i]):

            if(count == 0):
                firstRelated.append(name[i])
            if(count == 1):
                secondRelated.append(name[i])
            if(count == 2):
                thirdRelated.append(name[i])
            if(count == 3):
                fouthRelated.append(name[i])
            if(count == 4):
                fithRelated.append(name[i])
        else:
            count += +1
    if firstArtists[4] in firstRelated and secondRelated: 
        print(firstArtists[4] + ' e ' + firstArtists[3] + ' sao fortemente conectados')
    if firstArtists[3] in secondRelated and thirdRelated: 
        print(firstArtists[3] + ' e ' + firstArtists[2] + ' sao fortemente conectados')
    if firstArtists[2] in thirdRelated and fouthRelated: 
        print(firstArtists[2] + ' e ' + firstArtists[1] + ' sao fortemente conectados')
    if firstArtists[1] in fouthRelated and fithRelated: 
        print(firstArtists[1] + ' e ' + firstArtists[0] + ' sao fortemente conectados')

    return compFinal


artistName = userInput()
id = getId(artistName)
idFirst = getRelatedArtists(id)
getSecondRelatedArtists(idFirst[1])
getFellowBands(artistComparisonID, artistComparison)


f_node_trace = go.Scatter(
    x=[250, 250], y=[250, 250],
    mode='markers',
    name='Primeiro artista',
    hoverinfo='text',
    marker=dict(
        reversescale=True,
        size=50,
        line_width=0))

s_node_trace = go.Scatter(
    x=[325, 250, 175, 200, 300],
    y=[275, 375, 275, 150, 150],
    mode='markers',
    name='Artistas secundarios',
    hoverinfo='text',
    marker=dict(
        reversescale=True,
        size=40,
        line_width=0))

t_node_trace = go.Scatter(
    x=[
        250, 275, 225, 287, 213,
        135, 145, 145, 160, 160,
        365, 355, 355, 340, 340,
        175, 175, 180, 190, 200,
        325, 325, 320, 310, 300,
    ],
    y=[
        450, 425, 425, 400, 400,
        275, 250, 300, 225, 325,
        275, 250, 300, 225, 325,
        175, 150, 125, 100, 75,
        175, 150, 125, 100, 75,
    ],
    mode='markers',
    hoverinfo='text',
    name="artistas terciarios",
    marker=dict(
        reversescale=True,
        size=30,
        line_width=0))


f_node_trace.text = artistName
s_node_trace.text = firstArtists
t_node_trace.text = secondArtists

edge_trace = go.Scatter(
    x=[
        250, 250, 250, 325, 250, 175, 250, 200, 250, 300,
        300, 325, 300, 325, 300, 320, 300, 310, 300, 300,
    ], y=[
        250, 375, 250, 275, 250, 275, 250, 150, 250, 150,
        150, 150, 150, 175, 150, 125, 150, 100, 150, 75,
    ],
    line=dict(width=0.75, color='black'),
    hoverinfo='none',

    mode='lines')

edge_trace2 = go.Scatter(
    x=[
        250, 250, 250, 225, 250, 213, 250, 287, 250, 275
    ], y=[
        375, 450, 375, 425, 375, 400, 375, 400, 375, 425
    ],
    line=dict(width=0.75, color='black'),
    hoverinfo='none',
    mode='lines')

edge_trace3 = go.Scatter(
    x=[
        200, 175, 200, 175, 200, 180, 200, 190, 200, 200
    ], y=[
        150, 150, 150, 175, 150, 125, 150, 100, 150, 75
    ],
    line=dict(width=0.75, color='black'),
    hoverinfo='none',
    mode='lines')

edge_trace4 = go.Scatter(
    x=[
        325, 365, 325, 355, 325, 355, 325, 340, 325, 340
    ], y=[
        275, 275, 275, 300, 275, 250, 275, 225, 275, 325
    ],
    line=dict(width=0.75, color='black'),
    hoverinfo='none',
    mode='lines')

edge_trace5 = go.Scatter(
    x=[
        175, 135, 175, 145, 175, 145, 175, 160, 175, 160,
    ], y=[
        275, 275, 275, 250, 275, 300, 275, 325, 275, 225,
    ],
    line=dict(width=0.75, color='black'),
    hoverinfo='none',
    mode='lines')

fig = go.Figure(data=[f_node_trace, s_node_trace, t_node_trace, edge_trace, edge_trace2,  edge_trace3,  edge_trace4,  edge_trace5], layout=go.Layout(
    title='<b>'+"Artistas Relacionados"+'</b>',
    titlefont_size=16,
    margin=dict(b=20, l=5, r=5, t=40),
))


fig.show()
