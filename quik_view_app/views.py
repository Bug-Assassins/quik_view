from django.shortcuts import render
import urllib2
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json, urllib

#Global Variables
cities = { 'Ahmedabad' : 22, 'Bangalore' : 23, 'Chandigarh' : 24, 'Chennai' : 25, 'Coimbatore' : 26, 'Delhi' : 27, 'Hyderabad' : 28, 'Kochi' : 29, 'Kolkata' : 30, 'Mumbai' : 31, 'Mysore' : 32, 'Pune' : 33, 'Faridabad' : 121001, 'Hisar' : 125001, 'Sirsa' : 125055, 'Gurgaon' : 132222, 'Panchkula' : 134102, 'Mohali' : 140110, 'Ludhiana' : 141001, 'Indore' : 142222, 'Amritsar' : 143104, 'Jalandhar' : 144001, 'Jaipur' : 152222, 'Lucknow' : 162222, 'Shimla' : 171206, 'Nagpur' : 172222, 'Jammu' : 180001, 'Surat' : 182222, 'Srinagar' : 190001, 'Ghaziabad' : 201002, 'Noida' : 201301, 'GreaterNoida' : 201310, 'Kanpur' : 208001, 'Allahabad' : 211001, 'Varanasi' : 221002, 'Bareilly' : 243001, 'Moradabad' : 244302, 'Dehradun' : 248003, 'Meerut' : 250002, 'Mathura' : 281001, 'Agra' : 282002, 'Ajmer' : 305001, 'Udaipur' : 313001, 'Bikaner' : 334001, 'Jodhpur' : 342001, 'Rajkot' : 360001, 'Jamnagar' : 361001, 'Gandhinagar' : 382010, 'Vadodara' : 390001, 'Bharuch' : 393110, 'Thane' : 400601, 'NaviMumbai' : 400701, 'Goa' : 403108, 'Solapur' : 413001, 'Satara' : 415002, 'Kolhapur' : 416001, 'Kalyan' : 421301, 'Nashik' : 422001, 'Aurangabad' : 431001, 'Akola' : 444001, 'Bhopal' : 462001, 'Gwalior' : 474003, 'Jabalpur' : 482004, 'Katni' : 483775, 'Bilaspur' : 495001, 'Warangal' : 506002, 'Vijayawada' : 520001, 'Nellore' : 524101, 'Vizag' : 531001, 'Mangalore' : 575001, 'Hubli' : 580020, 'Belgaum' : 590001, 'Pondicherry' : 605001, 'Trichy' : 620015, 'Madurai' : 625001, 'Vellore' : 632001, 'Salem' : 636001, 'Kozhikode' : 673003, 'Thrissur' : 680001, 'Trivandrum' : 695001, 'Kharagpur' : 721301, 'Bhubaneswar' : 751001, 'Cuttack' : 753001, 'Guwahati' : 781001, 'Shillong' : 793001, 'Aizawl' : 796001, 'Kohima' : 797001, 'Patna' : 800001, 'Dhanbad' : 826001, 'Jamshedpur' : 831001, 'Ranchi' : 834002, 'Gudur' : 1003601, 'Guntakal' : 1003781, 'Guntur' : 1003961, 'Jagtial' : 1004321, 'Kakinada' : 1004861, 'Karimnagar' : 1005401, 'Nizamabad' : 1008821, 'Ongole' : 1009181, 'Rajahmundry' : 1010441, 'Tirupati' : 1014221, 'Jorhat' : 1016561, 'Bhagalpur' : 1019081, 'Chapra' : 1019441, 'Darbhanga' : 1019621, 'Gaya' : 1020161, 'Motihari' : 1022141, 'Munger' : 1022321, 'Muzaffarpur' : 1022501, 'Durg' : 1025381, 'Raigarh' : 1025921, 'Raipur' : 1026101, 'RajNandgaon' : 1026281, 'Daman' : 1026641, 'Diu' : 1026821, 'Anand' : 1027721, 'Bhuj' : 1028621, 'Gandhidham' : 1030781, 'Godhra' : 1031141, 'Junagadh' : 1031861, 'Mahuva' : 1032761, 'Mehsana' : 1033301, 'Morbi' : 1033661, 'Nadiad' : 1033841, 'Porbandar' : 1034921, 'Valsad' : 1036361, 'Panipat' : 1040142, 'Rohtak' : 1040502, 'BokaroSteelCity' : 1042842, 'Deoghar' : 1043742, 'Gulbarga' : 1049322, 'Raichur' : 1051842, 'Shimoga' : 1052742, 'Tumkur' : 1053642, 'Palakkad' : 1056882, 'Ahmednagar' : 1066783, 'Dhule' : 1070383, 'Jalgaon' : 1071283, 'Nanded' : 1073803, 'Osmanabad' : 1074343, 'PimpriChinchwad' : 1075603, 'Ratnagiri' : 1075963, 'PortBlair' : 1146883}

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
  req = urllib2.Request('https://api.quikr.com/public/trending?' + params,
    headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 3034456,
    "X-Quikr-Signature" : "301605be9525c9b137cc13a518d2d48ef1f16094",
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
    "X-Quikr-Token-Id" : 3034456,
    "X-Quikr-Signature" : "a6ec2b109402f0126d6baef748804aee509a9d93",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  print resp
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
  return render(request, 'trending.html', {'city_list' : cities})

def get_ads_by_location(request):
  params = urllib.urlencode(request.GET)
  req = urllib2.Request('https://api.quikr.com/public/adsByLocation?' + params,
    headers = {
    "X-Quikr-App-Id" : 524,
    "X-Quikr-Token-Id" : 3034456,
    "X-Quikr-Signature" : "54a19e57342715d4dbe7e9edfda19a6ca7556b75",
    "Content-Type" : "application/json"
    })
  resp = json.load(urllib2.urlopen(req))
  print resp['AdsByLocationResponse']['AdsByLocationData']
  return JsonResponse(resp['AdsByCategoryResponse']['AdsByCategoryData'])
