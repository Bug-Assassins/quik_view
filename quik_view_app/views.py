from django.shortcuts import render
import urllib2
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json, urllib

#Global Variables
cities = [['Agra', 282002, 27.02317485, 78.0925527], ['Ahmedabad', 22, 23.0216238, 72.5797068], ['Aizawl', 796001, 23.7414092, 92.7209297], ['Ajmer', 305001, 26.3305191, 74.7125556877547], ['Akola', 444001, 20.76697255, 77.2541275298075], ['Allahabad', 211001, 25.2859603, 81.896732069544], ['Amritsar', 143104, 31.5650861, 74.9770583945168], ['Anand', 1027721, 22.462708, 72.7433566269231], ['Aurangabad', 431001, 20.0328377, 75.158951321935], ['Bangalore', 23, 12.9791198, 77.5912997], ['Bareilly', 243001, 28.45843965, 79.3784627731263], ['Belgaum', 590001, 16.333333, 74.75], ['Bhagalpur', 1019081, 25.2852913, 87.1273317333307], ['Bharuch', 393110, 21.7080427, 72.9956936], ['Bhopal', 462001, 23.2530923, 77.3962718], ['Bhubaneswar', 751001, 20.2603328, 85.8393432], ['Bhuj', 1028621, 23.2472446, 69.668339], ['Bikaner', 334001, 28.1201648, 72.7864640162954], ['Bilaspur', 495001, 22.39558325, 81.6869862830063], ['Bokaro', 1042842, 23.672514, 86.2106449302686], ['Chandigarh', 24, 30.7351539, 76.7705033208026], ['Chapra', 1019441, 23.5200113, 88.550019], ['Chennai', 25, 13.0796914, 80.2829533], ['Coimbatore', 26, 11.0018115, 76.9628425], ['Cuttack', 753001, 20.3640012, 85.4611959771265], ['Daman', 1026641, 20.4169701, 72.833173], ['Darbhanga', 1019621, 26.1564716, 85.9255196], ['Dehradun', 248003, 30.3255646, 78.0436813], ['Delhi', 27, 28.6572914, 77.2272603], ['Deoghar', 1043742, 24.32948885, 86.7102353277855], ['Dhanbad', 826001, 23.8437824, 86.5845469328641], ['Dhule', 1070383, 21.135601, 74.4866627414739], ['Diu', 1026821, 20.7161177, 70.9106124], ['Durg', 1025381, 21.2009417, 81.3943241838917], ['Faridabad', 121001, 28.18325055, 77.348507062651], ['Gandhidham', 1030781, 23.0718743, 70.131715], ['Gandhinagar', 382010, 23.21379125, 72.6720876695242], ['Gaya', 1020161, 24.6798308, 85.0027993266777], ['Ghaziabad', 201002, 28.666667, 77.666667], ['Goa', 403108, 15.3004543, 74.0855134], ['Godhra', 1031141, 22.7785001, 73.6245157], ['Gudur', 1003601, 14.1463241, 79.8503768], ['Gulbarga', 1049322, 17.166667, 77.083333], ['Guntakal', 1003781, 15.1610981, 77.3768931], ['Guntur', 1003961, 16.416667, 80.25], ['Gurgaon', 132222, 28.4646148, 77.0299194], ['Guwahati', 781001, 26.1805978, 91.753943], ['Gwalior', 474003, 26.2, 78.2], ['Hisar', 125001, 29.24319675, 75.8086885741358], ['Hubli', 580020, 15.3518378, 75.1379848], ['Hyderabad', 28, 17.3616227, 78.4747305], ['Indore', 142222, 22.7140354, 75.8061182385911], ['Jabalpur', 482004, 23.3288622, 80.1072871013991], ['Jagtial', 1004321, 18.7954182, 78.9158262], ['Jaipur', 152222, 26.9161293, 75.8204056], ['Jalandhar', 144001, 31.29694945, 75.5592634063918], ['Jalgaon', 1071283, 20.9968453, 75.5683795], ['Jammu', 180001, 32.7280616, 74.9488478649601], ['Jamnagar', 361001, 22.4732415, 70.0552244], ['Jamshedpur', 831001, 22.8015194, 86.2029579], ['Jodhpur', 342001, 26.2989301, 73.0334001], ['Jorhat', 1016561, 26.76917135, 94.2649328175936], ['Junagadh', 1031861, 21.5174107, 70.4642757], ['Kakinada', 1004861, 16.9437385, 82.2350607], ['Kalyan', 421301, 19.2434721, 73.1397700989874], ['Kanpur', 208001, 26.5, 80.0], ['Karimnagar', 1005401, 18.52688015, 79.3862924635745], ['Katni', 483775, 23.87232715, 80.4167962788748], ['Kharagpur', 721301, 22.34309, 87.3012875], ['Kochi', 29, 9.9633864, 76.2536614], ['Kohima', 797001, 25.6155628, 93.8146949980969], ['Kolhapur', 416001, 16.45856815, 74.1015075745028], ['Kolkata', 30, 22.568746, 88.3462999], ['Kozhikode', 673003, 11.2446144, 75.7759372], ['Lucknow', 162222, 26.834512, 80.9080181406892], ['Ludhiana', 141001, 30.79197145, 75.89292025672], ['Madurai', 625001, 9.9248807, 77.9966469968149], ['Mahuva', 1032761, 21.0914409, 71.7621979], ['Mangalore', 575001, 12.8698101, 74.8430082], ['Mathura', 281001, 27.60477375, 77.5829471617707], ['Meerut', 250002, 29.00569565, 77.7756376135674], ['Mehsana', 1033301, 23.6017934, 72.3869915453049], ['Mohali', 140110, 30.7287676, 76.7138075], ['Moradabad', 244302, 28.8170328, 78.7777028569385], ['Morbi', 1033661, 22.8176662, 70.8345928], ['Motihari', 1022141, 26.6476203, 84.9143193], ['Mumbai', 31, 18.9523804, 72.8327112], ['Munger', 1022321, 25.0, 86.25], ['Muzaffarpur', 1022501, 26.166667, 85.416667], ['Mysore', 32, 12.3051828, 76.6553609], ['Nadiad', 1033841, 22.6859, 72.8601289156627], ['Nagpur', 172222, 21.1500964, 79.0127048991187], ['Nanded', 1073803, 19.09398365, 77.4734700838277], ['Nashik', 422001, 20.2217236, 74.1136047894734], ['NaviMumbai', 400701, 19.0215214, 73.0322633], ['Nellore', 524101, 14.4493717, 79.9873763], ['Nizamabad', 1008821, 18.53825345, 78.1148523091258], ['Noida', 201301, 28.5726442, 77.3547609], ['Ongole', 1009181, 15.505859, 80.050029], ['Osmanabad', 1074343, 18.16828695, 76.1186341738876], ['Palakkad', 1056882, 10.7759233, 76.6438011], ['Panchkula', 134102, 30.72663075, 76.9617566314072], ['Panipat', 1040142, 29.3281619, 76.8911770826338], ['Patna', 800001, 25.609575, 85.1238191], ['Pondicherry', 605001, 10.90253775, 79.9752370356183], ['Porbandar', 1034921, 21.6409, 69.611], ['PortBlair', 1146883, 11.6614772, 92.7392701], ['Pune', 33, 18.64395815, 73.9325681901252], ['Raichur', 1051842, 16.083333, 77.166667], ['Raigarh', 1025921, 22.06241275, 83.4011194147103], ['Raipur', 1026101, 20.82071695, 82.1229768974802], ['RajNandgaon', 1026281, 20.9714688, 80.6908767121225], ['Rajahmundry', 1010441, 17.0050454, 81.7804732], ['Rajkot', 360001, 22.3409469, 70.7860061733424], ['Ranchi', 834002, 23.14064535, 85.3732723225793], ['Ratnagiri', 1075963, 17.27448005, 73.2761783699303], ['Rohtak', 1040502, 28.8948618, 76.5489879043326], ['Salem', 636001, 11.6337735, 78.1977076579604], ['Satara', 415002, 17.64154745, 74.3056645244908], ['Shillong', 793001, 25.5760154, 91.8828027], ['Shimla', 171206, 31.24445, 77.7006251484403], ['Shimoga', 1052742, 14.05471745, 75.1311701627145], ['Sirsa', 125055, 29.6145013, 74.8919064559074], ['Solapur', 413001, 17.8337784, 75.2994133110269], ['Srinagar', 190001, 34.0747444, 74.8204443], ['Surat', 182222, 21.1864607, 72.8081281], ['Thane', 400601, 19.1943294, 72.9701779], ['Thrissur', 680001, 10.5251898, 76.2159825], ['Tirupati', 1014221, 13.631655, 79.4231899], ['Trichy', 620015, 10.804973, 78.686904], ['Trivandrum', 695001, 8.5057492, 76.9573562], ['Tumkur', 1053642, 13.4999406, 77.0002445], ['Udaipur', 313001, 24.38033415, 73.9551544176044], ['Vadodara', 390001, 22.3177543, 73.362540944666], ['Valsad', 1036361, 20.42000485, 72.8635372612251], ['Varanasi', 221002, 25.38029175, 82.938821088128], ['Vellore', 632001, 12.72092635, 78.8003825786974], ['Vijayawada', 520001, 16.5087586, 80.6185102], ['Vizag', 531001, 17.7231276, 83.3012842], ['Warangal', 506002, 17.96156065, 79.5874436511009]]

# Create your views here.
def home(request):
  return render(request, 'index.html', {})

def map_plot(request):
  return render(request, 'map.html', {'city_list' : cities})

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
  return JsonResponse(return_json)

def get_heat_map_context():
  # First list is category (id, name) tuple
  # Second list is city (id, name) tuple
  return {
            'category' : { 10: 'First category', 11: 'Second category'},
            'city' : [['Pune', 1, 18.5203, 73.8567], ['Kolkata', 2, 22.5667, 88.3667]],
            'selected_city' : 'Pune',
        }
def get_heat_map_data():
  return {'18.64216995,73.82109070': 1, '18.48844910,73.81771088': 2}

def get_heat_map(request):
  return render(request, 'heatmap.html', get_heat_map_context())

def get_heat_map_city_data(request):
  return JsonResponse(get_heat_map_data())

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
  resp = resp['AdsByLocationResponse']['AdsByLocationData']
  ret_json = {'total' : resp['total'], 'docs' : []}
  for ad in resp['docs']:
    if 'geo_pin' in ad and 'ad_locality' in ad:
      geo_str = ad['geo_pin'].split(',')
      ret_json['docs'].append({
        't' : ad['title'],
        'lat' : float(geo_str[0]),
        'lng' : float(geo_str[1]),
        'loc' : ad['ad_locality']
      })
  return JsonResponse(ret_json)

def get_ad_internal(request):
  city = request.GET['city_name']
  cat_list = request.GET['category']
  resp = quik_ad.get_by_city_cat(city, cat_list)
  print resp
  return JsonResponse(resp)
