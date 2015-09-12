from django.shortcuts import render
import urllib2
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json, urllib

# Create your views here.
def home(request):
  return render(request, 'index.html', {})

def map_plot(request):
  if 'city' not in request.GET:
    return HttpResponseRedirect('/')
  return render(request, 'map.html', {'city' : request.GET['city']})

def live_data_render(request):
  return render(request, 'live_data.html', {})

def get_trending_data(request):
  params = urllib.urlencode(request.GET)
  req = urllib2.Request('https://api.quikr.com/public/trending' + params,
    headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "1fa00abc8c53033294c7a25ba7ffd5f9fdfd35ec",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  trend_arr = resp['getTrendingResponse']['trendingData'];
  return_json = {'name' : 'Quikr Trending Ads', 'children' : []}
  for node in trend_arr:
    x = {'name' : ''}
    for key, value in node['attr'].iteritems():
      x['name'] += value + ' '
    x['size'] = node['count']
    return_json['children'].append(x)
  print return_json
  return JsonResponse(return_json)

def get_heat_map_context():
  # First list is category (id, name) tuple
  # Second list is city (id, name) tuple
  return {
            'category' : [['10', 'First category'], ['11', 'Second category']], 
            'city' : [['13', 'City1'], ['12', 'City2']],
            'selected_city' : ['13', 'City1'],
            'category_count' : [['10', ['37.751266', '-122.403355', '5']], ['11', ['37.751266', '-122.403355', '2']]] 
          }

def get_heat_map(request):
  return render(request, 'heatmap.html', get_heat_map_context())

def get_live_data(request):
  req = urllib2.Request('https://api.quikr.com/public/liveOnQuikr', headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "eea5541957250c25c17c4d617c472e7832572d10",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  return JsonResponse(resp['liveOnQuikrResponse']['liveOnQuikrData'])

def get_ads_by_category(request):
  params = urllib.urlencode(request.GET)
  req = urllib2.Request('https://api.quikr.com/public/adsByCategory?' + params,
    headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 2902886,
    "X-Quikr-Signature" : "fb22e528145f29eae46f1dfc304751b7dafd53e3",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  print resp['AdsByCategoryResponse']['AdsByCategoryData']
  return JsonResponse(resp['AdsByCategoryResponse']['AdsByCategoryData'])

def trending_plot(request):
  return render(request, 'trending.html', {})
