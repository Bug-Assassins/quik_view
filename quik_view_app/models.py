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
  def get_by_city_cat(cls, city, cat_list):
    result_set = quik_ad.objects.filter(city=city, category__in=cat_list)
    result = {}
    for record in result_set:
      if record.ip in result:
        result[record.ip] += record.count
      else:
        result[record.ip] = record.count
    return result

  #Pass the dictionary to this method and it will get saved
  @classmethod
  def load_database(dic):
    ads_added = 0
    for city in dic:
      for cat in city:
        for ip, val in cat.iteritems():
          try:
            quikr_ad.save_data(city, cat, ip, val)
            ads_added += 1
          except Exception:
            print "Error In Saving Data"
            pass
    print "Total Number of Ads Added =", ads_added
