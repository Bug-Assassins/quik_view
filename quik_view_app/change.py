from data import category_data

if __name__ == '__main__':
	dict = {}
	for category in category_data :
		dict[category["CategoryId"]] = category["CategoryName"]
	print dict 