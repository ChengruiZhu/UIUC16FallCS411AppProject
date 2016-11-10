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

    addrFile = open("./data/address")

    dict = {}
    line = addrFile.readline()
    while len(line) != 0:
        imdbNum = line.split('|')[0]
        address = line.split('|')[1]
        dict[imdbNum] = address
        line = addrFile.readline()
    addrFile.close()

    outputFile = open("./data/address",'a')
    inputFile = open("./data/movies.csv")

    inputFile.readline()
    num = inputFile.readline().split(',')[0][3:-1]
    while len(num) != 0:
        try:
            if num > '0521868' and num not in dict.keys():
                address = getLocation(num)
                if len(address) > 1 and 'locations' not in address:
                    outputFile.writelines(num+'|'+address)
                    dict[num] = address
                print(num)
            num = inputFile.readline().split(',')[0][3:-1]

        except:
            outputFile.close()
            inputFile.close()
            print("Errors! Last num is", num)
            exit()
    outputFile.close()
    inputFile.close()

main()