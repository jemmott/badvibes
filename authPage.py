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
    <head>
    <meta charset="UTF-8">
    <title>Bad Vibes!</title>
    <body>
    <h1>Bad Vibes!</h1><br>
    <a href="{}">Authorize</a><br><br>
    You can trust me.<br><br>
    Email cjemmott@gmail.com if this breaks or you have feedback.
    </body>""".format(authUrl)
    
    return websiteHtml