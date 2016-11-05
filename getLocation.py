from imdb import IMDb
import re
import urllib2
import json


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
		return 666, 666
	else:
		print ('Google API response: ' + parsed_json['status'])
		return 555, 555



def main():

    key = ['AIzaSyAiAnz_K18bDdmJoCNCVFMjV0QqxfvuVb8',
           'AIzaSyDCNd_elCpRNEq9QOOPcHpGb4Xan4T03r4',
           'AIzaSyDAYjzp8PdS9qik5WfuwPXO6JYfJdrJpB8',
           'AIzaSyDgeVRx7kyJTN0T26r4PqEocBB6oKiqjZM',]

    inputFile = open("./data/address")
    outputFile = open("./data/geolocation", 'w')
    line = inputFile.readline()
    i = 0
    while len(line) != 0:
        imdbNum = line.split('|')[0]
        address = line.split('|')[1]
        lat, lng = geoCoding(address,)
        if lat != 888 and lat != 666 and lat != 555:
            outputFile.write(imdbNum+'|' + lat + ',' + lng + '\n')
            line = inputFile.readline()
        elif lat == 888:
            if ++i < 4:
                print(key[--i]+' used up')
                print('new key is: ' + [i])
            else:
                print('Key used up!')
                print('imdbNum = ' + imdbNum)
                return
        print(float(imdbNum)/94833.0)

main()