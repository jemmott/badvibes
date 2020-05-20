# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:05:32 2020

@author: ColinJemmott
"""

import utils

def getHtml(baseUrl, code):
    
    farthestNeighborUrl = baseUrl + "farthestneighbor/" + "?code=" + code
    
    websiteHtml = """<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Bad Vibes!</title>
    <body>
    <h1>Bad Vibes!</h1><br>
    Huh.  I didn't think you would actually go for it...<br>
    <a href="{}">Generate Farthest Neighbor Playlist</a><br>
    (this takes a minute)<br><br>
    </body>""".format(farthestNeighborUrl)
    
    #results = {"code":code,
    #           "baseUrl":baseUrl}
    #utils.log(str(results), "callback")
    
    return websiteHtml