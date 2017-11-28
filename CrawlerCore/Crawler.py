'''
Created on 22 Oct 2017

@author: tictaclu
'''

from weibo import APIClient
import webbrowser
from selenium import webdriver
from pip._vendor.requests.api import request
import requests
from time import sleep
import urllib2
from sepolgen.defaults import headers

APP_KEY = '974904498'
APP_SECRET= '5b2a65ac03d37540594ef198875057a4'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

webbrowser.open_new(url)

r = requests.get(url)
print(r.url)
  
code = raw_input()  
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)
comments = client.comments.show.get(id=4165801081080870, count=1, page = 1)
length = len(comments['comments'])
for i in range(0, length):
    print comments['comments'][i]['text']




