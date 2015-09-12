from django.shortcuts import render
import urllib2
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
  return render(request, 'index.html', {})

def map_plot(request):
  return render(request, 'map.html', {})

def live_data_render(request):
  return render(request, 'live_data.html', {})

def get_trending_data(request):
  req = urllib2.Request('https://api.quikr.com/public/trending', headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "1fa00abc8c53033294c7a25ba7ffd5f9fdfd35ec",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  return JsonResponse(resp)

def get_live_data(request) :
  req = urllib2.Request('https://api.quikr.com/public/liveOnQuikr', headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "eea5541957250c25c17c4d617c472e7832572d10",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  return JsonResponse(resp['liveOnQuikrResponse']['liveOnQuikrData'])

def get_ads_by_category(request) :
  req = urllib2.Request('https://api.quikr.com/public/adsByCategory', headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "fb22e528145f29eae46f1dfc304751b7dafd53e3",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  print resp['AdsByCategoryResponse']['AdsByCategoryData']
  return JsonResponse(resp['AdsByCategoryResponse']['AdsByCategoryData'])
