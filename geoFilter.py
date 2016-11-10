#!/usr/bin/python

def main():

    inputFile = open("./data/address")
    outputFile = open("./data/addr", 'w+')
    line = inputFile.readline()


    dict = {}
    while len(line) != 0:
        imdbNum = line.split('|')[0]
        address = line.split('|')[1]
        dict[imdbNum] = address

        line = inputFile.readline()

    keylist = dict.keys()
    keylist.sort()

    for k in keylist:
        if 'locations' not in dict[k]:
            outputFile.writelines(k+"|"+dict[k])

    inputFile.close()
    outputFile.close()

main()