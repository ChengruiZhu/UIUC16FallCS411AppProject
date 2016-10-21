import urllib2
import json

addr = 'TVW7 Studios, Perth, Western Australia, Australia'

def geoCoding(addr, API_KEY):
	addr = addr.strip().replace (" ", "+")
	req = urllib2.Request('https://maps.googleapis.com/maps/api/geocode/json?address='+ addr +'&key='+API_KEY)
	response = urllib2.urlopen(req)
	the_page = response.read()

	parsed_json = json.loads(the_page)
	if parsed_json['status'] == 'OK':
		lat = parsed_json['results'][0]['geometry']['location']['lat']
		lng = parsed_json['results'][0]['geometry']['location']['lng']
		return lat, lng
	elif parsed_json['status'] == 'OVER_QUERY_LIMIT':
		print ('Google API Over Quota!')
		return 888, 888
	elif parsed_json['status'] == 'ZERO_RESULTS':
		print('Google API Address Invilid!')
		return 222, 222
	else:
		print ('Google API response: ' + parsed_json[status])
		return 555, 555