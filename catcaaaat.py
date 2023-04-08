# -*- coding:utf-8 -*-
__author__ = "twilightsuz326"
__version__ = "0.0.1"
__date__    = "01 November 2011"

import requests
import os
import json
import random
from win11toast import toast

# Set the API key
api_key = " < API KEY > "

# Download and save the cat image
response = json.loads(requests.get('https://api.thecatapi.com/v1/images/search?has_breeds=1', headers={'x-api-key': api_key}).content)
image = requests.get(response[0]['url']).content

with open("cat.jpg" ,mode='wb') as f: 
  f.write(image)

# Display the toast notification with the breed description, related link, and cat image
breeds = response[0]["breeds"][0]
title = (f' {breeds["name"]} [{breeds["origin"]}]')
link = breeds["vetstreet_url"] if "vetstreet_url" in breeds else ""
toast(title, breeds["description"],
            image=os.path.abspath('cat.jpg'), 
            audio=os.path.abspath('mp3/' + str(random.randint(1, 4)) + '.mp3'),
            app_id='🐾ねこが遊びにきました',
            on_click=link
      )