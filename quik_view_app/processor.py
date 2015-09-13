from tempo import data
#from geopy.geocoders import Nominatim 
def process() :
	result = {}
	#geolocator = Nominatim()
	for ad in data :
		city = ad['cityName']
		category = ad['categoryId']
		loc = ad['ad_locality']
		if city not in result.keys() :
			result[city] = {}
		if category not in result[city].keys() :
			result[city][category] = {}
		#geo_pin = []
		
		if 'geo_pin' in ad.keys() :
			geopin = ad['geo_pin']

		else :
			continue

		# else if type(loc) is str :
			
		# 	gp = 
		# 	geo_pin[0] = gp;
		
		# else :
		# 	i = 0
		# 	for ad_loc in loc :
		# 		gp = 
		# 		geo_pin[i] = gp
		# 		i += 1

		#for geopin in geo_pin :
		if(geopin not in result[city][category].keys()) :
			result[city][category][geopin] = 1
		else :
			result[city][category][geopin] += 1
	#for key in result.keys() : 
	print result

if __name__ == '__main__':
	process()