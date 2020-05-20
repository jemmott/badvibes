# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:05:32 2020

@author: ColinJemmott
"""

import spotipy
import numpy as np
import pandas as pd
import os
import utils

columns = ['acousticness', 'danceability', 'energy', 'liveness', 'loudness', 'speechiness', 'valence', 'tempo', 'mode']


def getHtml(baseUrl, code):

    
    clientId = os.environ.get('SPOTIPY_CLIENT_ID')
    clientSecret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    redirectUri = baseUrl + "callback/"
    scope = " ".join(['playlist-modify-public',"user-top-read","user-read-recently-played","playlist-read-private"])
    
    sp_oauth = spotipy.oauth2.SpotifyOAuth(clientId, clientSecret, redirectUri, scope=scope)
    
    token_info = sp_oauth.get_access_token(code)
    
    access_token = token_info['access_token']
    sp = spotipy.Spotify(auth=access_token)
    
    # get user top tracks and features
    topTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
    trackIds = [track['id'] for track in topTracks['items'] if not track['is_local']]
    
    topTracksFeatures = sp.audio_features(trackIds)
    topTracksFeaturesDf = pd.DataFrame.from_records(topTracksFeatures)
    
    # load the 2019 top tracks
    topTracks2019Df = pd.read_csv("spotify_global_2019_most_streamed_tracks_audio_features.csv")

    # Farthest neighbor (this is the slow part)
    columnsNormed = [c+"_norm" for c in columns]
    
    topTracksFeaturesDf = createNorm(topTracksFeaturesDf, topTracks2019Df)
    
    nearestNeighborDistance = []
    for ii in range(len(topTracks2019Df)):
        topTrack = topTracks2019Df.iloc[ii]
        distances = []
        for column in columnsNormed:
            distance = min(abs(topTrack[column] - topTracksFeaturesDf[column]))
            distances.append(distance)
        rmsDistance = np.sqrt(np.mean(np.power(distances,2)))
        nearestNeighborDistance.append(rmsDistance)
        
    topTracks2019Df['nearestNeighborDistance'] = nearestNeighborDistance
    
    recommendations = topTracks2019Df.sort_values('nearestNeighborDistance', ascending=False)
    track_ids = list(recommendations['Track_id'][:50])
    
    # Write playlist
    username = sp.current_user()['id']
    playlistName = "Bad Vibes: Farthest Neighbor {}".format(username)
    playlist = sp.user_playlist_create(username, playlistName)
    _ = sp.user_playlist_add_tracks(username, playlist['id'], track_ids)
    playlistUrl = playlist['external_urls']['spotify']
    
    results = {"username":username,
               "code":code,
               "baseUrl":baseUrl,
               "tokenInfo":token_info,
               "playlistUrl":playlistUrl}
    utils.log(str(results), "#farthest-neighbor")
    
    websiteHtml = """<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Bad Vibes!</title>
    <body>
    <h1>Bad Vibes!</h1><br>
    <a href="{}">Enjoy?</a>
    </body>""".format(playlistUrl)
    
    return websiteHtml

def createNorm(tableToNorm, tableToNormBy):
    for column in columns:
        mean = np.mean(tableToNormBy[column])
        stdev = np.std(tableToNormBy[column])
        tableToNorm[column + '_norm'] = np.divide(np.subtract(tableToNorm[column],mean), stdev)
    return tableToNorm