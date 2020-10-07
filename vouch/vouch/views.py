from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import sys
import requests
import tweepy
import twitter
import time
from twython import Twython
import datetime

def home(request):
   
    return render(request,'index.html') 
def mlogin(request):
    client_key = '33nPMdgtG3zmBRpwhGeKEaVhB'
    client_secret = 'hNOQ2X7llEK59DGtwIjad1UnaVuRyY87FNX2ghspikQMYaV4yr'
    
    token = '303891450-XoN77keccPb87JKrCdpJXMAsDD1ECPy2T4Eh9BYs'
    secret = 'mXOIqWjaLEwFbL0qKu6yLyLnD1exztN7CryQYXi6U13ox'

    auth = tweepy.OAuthHandler(client_key,client_secret)
    auth.set_access_token(token,secret)
    data = tweepy.API(auth)
    li,lis,l = [],[],[]
    screen_name = "vyas81"
    for i in data.friends():
        li.append(i.screen_name)
    for i in li:
        tweetCount = 0
        for j in data.user_timeline(i):
            k = str(j.created_at).split(' ')[0]
            z1 = time.mktime(datetime.datetime.strptime(k,"%Y-%m-%d").timetuple())
            ct = str(datetime.datetime.now()).split(' ')[0] 
            z2 = time.mktime(datetime.datetime.strptime(ct,"%Y-%m-%d").timetuple())
            temp = (z2-z1)<=604800.0
            if 'https' in j.text and temp:
                lis.append([i,j.text])
                tweetCount += 1
        l.append([tweetCount,i])
    maxTweet = max(l)[1]
    params = {'li' : li, 'lis' : lis, 'maxTweet': maxTweet} 
    return render(request,'home.html',params)
def mlogout(request):    
    logout(request)
    messages.success(request,"Logged Out ")
    return redirect('/')