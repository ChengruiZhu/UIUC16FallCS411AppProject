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
		print('Google API Address Invilid : ' + addr)
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
    outputFile = open("./data/geolocation", 'a')
    line = inputFile.readline()
    i = 0
    cnt = 0


    while line.split('|')[0] <= '0056201':
        line = inputFile.readline()
    print('Starting...')

    while len(line) != 0:
        imdbNum = line.split('|')[0]
        address = line.split('|')[1]
        if 'locations' not in address:
            lat, lng = geoCoding(address, key[i])
        else:
            lat = 555
        if lat != 888 and lat != 666 and lat != 555:
            outputFile.write(imdbNum+'|' + str(lat) + ',' + str(lng) + '\n')
            cnt += 1
            print(cnt)
        elif lat == 888:
            if i < 3:
                i += 1
                print('new key is: ' + key[i])
            else:
                print('Key used up!')
                print('imdbNum = ' + imdbNum)
                inputFile.close()
                outputFile.close()
                return
        line = inputFile.readline()

    inputFile.close()
    outputFile.close()

main()