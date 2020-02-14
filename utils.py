# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:17:42 2020

@author: ColinJemmott
"""

import slack
import os

def log(text, channel="#general"):
    try: # getting weird async error.  Don't want to fix it.
        client = slack.WebClient(token=os.environ.get('SLACK_API_TOKEN'))
        
        _ = client.chat_postMessage(
            channel=channel,
            text=str(text))
    except:
        return
        
    