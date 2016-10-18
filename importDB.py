import urllib2
import json

for i in range(3603346, 3603456):

	req = urllib2.Request('http://www.omdbapi.com/?i=tt' + str(i)+'&plot=short&r=json')
	response = urllib2.urlopen(req)
	the_page = response.read()

	parsed_json = json.loads(the_page)
	# print(parsed_json)
	if 'imdbID' in parsed_json:
		print(parsed_json)


