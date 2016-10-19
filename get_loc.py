from imdb import IMDb

def getLocation(id):
        imdb_tool = IMDb()
        location= imdb_tool.get_movie_locations(id))
        loc = location['data']
        
        if not loc:
                return ''
                
        loc = loc['locations'][0] #only get first location in the list
        loc = loc.split('(')[0] #get rid of everythign after '('

        return loc

#nice try
#print(getLocation('1000093')) #input value shoud be a string of digits
