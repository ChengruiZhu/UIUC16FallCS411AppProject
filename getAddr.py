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
    res = loc['locations'][0] #only get first location in the list

    # find the max len
    for s in loc:
        if len(s) > len(res):
            res = s
    res = res.split('(')[0] #get rid of everythign after '('
    res = re.sub('[^a-zA-Z\d\s,]', '', res)#regex remove banned chars
    return res


def main():
    print('Starting...')

    outputFile = open("./data/address", 'a')
    inputFile = open("./data/movies.csv")
    inputFile.readline()
    num = inputFile.readline()
    while num < '0000001':
        num = inputFile.readline()
    print('Starting...')
    while len(num) != 0:
        num = num.split(',')[0][3:-1]
        address = getLocation(num)
        if len(address) > 1:
            outputFile.write(num+'|'+address+'\n')
        print(num)
        print(float(num)/94833.0)
        num = inputFile.readline()
    outputFile.close()
    inputFile.close()
main()