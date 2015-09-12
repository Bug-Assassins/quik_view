from data import category_data
from time import sleep
import json, urllib, urllib2

def get_response(params) :
  req = urllib2.Request('https://api.quikr.com/public/adsByCategory?' + params,
  headers = {
  "X-Quikr-App-Id" : 524,
  "X-Quikr-Token-Id" : 3034456,
  "X-Quikr-Signature" : "7c9f3c8014db5aa4d1bc1498a90ebf05d241b68a",
  "Content-Type" : "application/json"
  })
  resp = json.load(urllib2.urlopen(req))
  return resp

def get_ads_by_category() :

    attribute_list = {'cityName', 'categoryName', 'stateName', 'ad_locality'}
    allData = []
    record = {}
    for category in category_data :
      id = category['CategoryId']
      while True : 
        try:
          params = urllib.urlencode({'categoryId' : id, 'from' : 0, 'size' : 100})
          resp = get_response(params)
          total = resp['AdsByCategoryResponse']['AdsByCategoryData']['total']
          ads = resp['AdsByCategoryResponse']['AdsByCategoryData']['docs']
          for ad in ads :
            for attribute in attribute_list :
              record[attribute] = ad[attribute]
            record['categoryId'] = id
            allData.append(record)
          break
        except:
          sleep(5)       
      i = 101
      while i < total :
        try:
          params = urllib.urlencode({'categoryId' : id, 'from' : i, 'size' : 100})
          resp = get_response(params)
          ads = resp['AdsByCategoryResponse']['AdsByCategoryData']['docs']
          i += 100
          for ad in ads :
            for attribute in attribute_list :
              record[attribute] = ad[attribute]
            record['categoryId'] = id
            allData.append(record)
        except:
          sleep(5)
    print allData

if __name__ == '__main__':
  get_ads_by_category()
  
