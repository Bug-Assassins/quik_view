from django.db import models

# Create your models here.

class quik_ad(models.Model):
  city = models.CharField(max_length = 200, null=False)
  category = models.IntegerField(null=False)
  ip = models.CharField(max_length = 500, null=False)
  count = models.IntegerField(default=1)

  @classmethod
  def save_data(cls, city, cat, ip, co):
    record = quik_ad(city=city, category=cat, ip=ip, count=co)
    record.save()

  @classmethod
  def get_by_city_cat(cls, city, catlist):
    result_set = quik_ad.objects.filter(city=city, category__in=catlist)
    result = {}
    for record in result_set:
      if record.ip in result:
        result[record.ip] += record.count
      else:
        result[record.ip] = record.count
    return result

  #Pass the dictionary to this method and it will get saved
  @classmethod
  def load_database(cls, dic):
    ads_added = 0
    for city, val in dic.iteritems():
      for cat, val in val.iteritems():
        for ip, val in val.iteritems():
          try:
            quik_ad.save_data(city, cat, ip, val)
            ads_added += 1
          except Exception:
            print "Error In Saving Data"
            pass
    print "Total Number of Ads Added =", ads_added

  @classmethod
  def get_all_geoip(cls, city):
    result_set = quik_ad.objects.filter(city=city)
    ret = {'docs' : []}
    for x in result_set:
      ret['docs'].append({
        'lat' : float(str(x.ip).split(',')[0]),
        'lng' : float(str(x.ip).split(',')[1])
      })
    return ret
