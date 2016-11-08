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
    outputFile = open("./data/address", 'a')
    inputFile = open("./data/movies.csv")
    inputFile.readline()
    num = inputFile.readline().split(',')[0][3:-1]
    while num <= '0166137':
        num = inputFile.readline().split(',')[0][3:-1]
    print('Starting...')
    cnt = 0
    while len(num) != 0:
        try:
            address = getLocation(num)
            if len(address) > 1:
                outputFile.write(num+'|'+address+'\n')
            print(num)
            print(float(cnt)/94833.0)
            cnt += 1
            num = inputFile.readline().split(',')[0][3:-1]
        except:
            outputFile.close()
            inputFile.close()
            print("Errors! Last num is %d" % num)
    outputFile.close()
    inputFile.close()

main()