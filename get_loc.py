from imdb import IMDb
import re
def getLocation(id):
        imdb_tool = IMDb()
        location= imdb_tool.get_movie_locations(id)

#       for a in location['data']['locations']:
#               print(a)
        loc = location['data']
        if not loc:
                return ''
        loc = loc['locations'][0] #only get first location in the list
        loc = loc.split('(')[0] #get rid of everythign after '('
        loc = re.sub('[^a-zA-Z\d\s,]', '', loc)#regex remove banned chars
        return loc

#nice try
#print(getLocation('1000093')) #input value shoud be a string of digits
