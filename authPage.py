# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:57:42 2020

@author: ColinJemmott
"""

import spotipy
import os

def getHtml(baseUrl):
    
    clientId = os.environ.get('SPOTIPY_CLIENT_ID')
    clientSecret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    redirectUri = baseUrl + "callback/"
    scope = " ".join(['playlist-modify-public',"user-top-read","user-read-recently-played","playlist-read-private"])
    
    sp_oauth = spotipy.oauth2.SpotifyOAuth(clientId, clientSecret, redirectUri, scope=scope)
    
    # Force auth every time
    authUrl = sp_oauth.get_authorize_url(show_dialog=True)
    
    websiteHtml = """<!DOCTYPE html>
    <html>
    <style>
    body {{
        background-image: url('https://live.staticflickr.com/1052/3171953619_94b503e0f8_b.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        height: 100%;
    }}
    </style>
    <head>
    <meta charset="UTF-8">
    <title>Bad Vibes!</title>
    </head>
    <body> 
    <h1>Bad Vibes!</h1><br>
    During the excellent <a href="https://cultureddata.net/">Cultured Data Symposium 2020</a>, 
    <a href="http://www.tobinchodos.com/">Tobin Chodos</a> said something like <br><br>
    <blockquote>"Since there is no mathematically coherent measure of a 
    "success" in music recommendation, since human love of music is so strange and capricious, 
    you could probably reverse the logic of Spotify's recommender engine and get similarly satisfying 
    results, perhaps more satisfying"</blockquote>
    <h2>Challenge Accepted!</h2>
    <a href="{}"><button type="button">Click here to create your own customized bad playlist -></button></a><br><br>
    This is a bad Spotify recommender. Like, the worst. Bad vibes anti-recommendations.<br><br>
    This is currently very much a proof of concept. It grabs your top 50 songs (long-term), 
    and then does a "farthest neighbor recommendation" based on the audio features Spotify provides. 
    I restricted myself to the <a href="https://www.kaggle.com/prasertk/spotify-global-2019-moststreamed-tracks">2019 global most streamed tracks</a>
    , so I couldn't pick total shit. In other words, it is a recommender system that tries to find music that is popular, but you won't like.<br><br>

    Though, to be honest, that *NYSYNC Christmas song is pretty rough.<br><br>
    
    Send feedback to <a href="http://www.cjemmott.com/">Colin Jemmott</a><br><br>
    

    <a href="https://github.com/jemmott/badvibes">Source code</a><br><br>
    </body>""".format(authUrl)
    
    return websiteHtml