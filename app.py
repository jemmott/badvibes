# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:31:09 2020

@author: ColinJemmott
"""

from flask import Flask, request
import authPage
import callback
import farthestNeighbor
import os

app = Flask(__name__)

baseUrl = os.environ.get('BAD_VIBES_URL')

@app.route("/")
def home():
    return authPage.getHtml(baseUrl)
    
@app.route("/callback/")
def callback_page():
    code = request.args.get('code')
    return callback.getHtml(baseUrl, code)

@app.route("/farthestneighbor/")
def farthestNeighbor_page():
    code = request.args.get('code')
    return farthestNeighbor.getHtml(baseUrl, code)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')