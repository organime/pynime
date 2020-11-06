#!/usr/bin/env python3
import os
import json
from datetime import datetime

def theTime(tOp):
    # current date and time
    now = datetime.now()

    if tOp == 1:
        # return mm/dd/YY H:M:S format
        return now.strftime('%m/%d/%Y, %H:%M:%S')
    if tOp == 2:
        # return mm/dd/YY format
        return now.strftime('%m/%d/%Y')

def loadJson():
    try:
        with open("assets/list.json", "r") as file:
            data = json.load(file)
        return data
    except:
        print('Have any error while we are loading the file.')

def saveJson(data):
    try:
        with open("assets/list.json", "w") as file:
            json.dump(data, file, indent = 4)
    except:
        print('Have any error while we are saving new anime.')

def addAnimeJson(sName, sEp, sSea):
    # loads json data in array
    svdAn = loadJson()
    # new object with the anime's information
    sAn = {"name": sName, "episode": int(sEp), "season": int(sSea)}

    if not svdAn:
        # add new anime in the end of array
        svdAn = [sAn]
    else:
        svdAn.append(sAn)

    # save the content in json
    saveJson(svdAn)
    print('You added a new anime to the list.')

def allAnimesJson():
    # loads json data in array
    svdAn = loadJson()

    if not svdAn:
        print("You don\'t have saved animes.")
    else:
        print("Ex: <line> - <anime> (ep: <episode>, season: <season>)\n")
        for i, line in enumerate(svdAn):
            print("{} - {} (episode: {}, season: {})".format(i+1, svdAn[i]["name"], svdAn[i]["episode"], svdAn[i]["season"]))
        print("\nYou have {} animes in list.".format(len(svdAn)))

def editAnimeJson():
    # loads json data in array
    svdAn = loadJson()

    if not svdAn:
        print("You don\'t have saved animes.")
    else:
        allAnimesJson()

        line = int(input('What is the line you want to edit: '))

        if (line <= len(svdAn) and line >= 1):
            op = int(input("You want change: \n1 - name, episode and season\n2 - episode and season\n3 - only episode\nOption: "))

            if (op == 1):
                nName = input('Enter the name: ')
                nEp = input('Enter the episode: ')
                nSea = input('Enter the season: ')

                print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], nName, nEp, nSea))
                svdAn[line-1] = {"name": nName, "episode": int(nEp), "season": int(nSea)}
            if (op == 2):
                nEp = input('Enter the episode: ')
                nSea = input('Enter the season: ')

                acName = svdAn[line-1]["name"]

                print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], acName, nEp, nSea))
                svdAn[line-1] = {"name": acName, "episode": int(nEp), "season": int(nSea)}
            if (op == 3):
                nEp = input('Enter the episode: ')

                acName = svdAn[line-1]["name"]
                acSea = svdAn[line-1]["season"]

                print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], acName, nEp, acSea))
                svdAn[line-1] = {"name": acName, "episode": int(nEp), "season": acSea}
            if (op >= 3 or op <= 1):
                print('(^-^)b - "sorry, i can\'t make this."')
            saveJson(svdAn)
        else:
            print('(^-^)b - "sorry, i can\'t make this."')

def deleteAnimeJson():
    # loads json data in array
    svdAn = loadJson()

    if not svdAn:
        print("You don\'t have saved animes.")
    else:
        allAnimesJson()

        line = int(input('What is the line you want to delete: '))

        if (line <= len(svdAn) and line >= 1):
            print("\nRemove: {} - (episode: {}, season: {}".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"]))

            svdAn.pop(line-1)
            saveJson(svdAn)
        else:
            print('(^-^)b - "sorry, i can\'t make this."')

def main():
    print('Welcome, today is: {};'.format(theTime(1)))
    print('----------MENU----------')
    
    sOp = -1
    while sOp != 0:
        print('Select an option:\n1 - CREATE\n2 - READ\n3 - EDIT\n4 - DELETE\n0 - EXIT')
        sOp = int(input('\nEnter selected option: '))

        if sOp == 1:
            print('\n----------START CREATE ANIMES----------\n')
            name = input('Enter the name: ')
            ep = input('Enter the episode: ')
            sea = input('Enter the season: ')

            addAnimeJson(name, ep, sea)
            print('\n----------END CREATE ANIMES----------\n')
        if sOp == 2:
            print('\n----------START READ ANIMES----------\n')
            allAnimesJson()
            print('\n----------END READ ANIMES----------\n')
        if sOp == 3:
            print('\n----------START EDIT ANIMES----------\n')
            editAnimeJson()
            print('\n----------END EDIT ANIMES----------\n')
        if sOp == 4:
            print('\n----------START DELETE ANIMES----------\n')
            deleteAnimeJson()
            print('\n----------END DELETE ANIMES----------\n')
        if ((sOp < 1 and sOp != 0) or sOp > 4):
            print('(^-^)b - "sorry, i can\'t make this."')
        if sOp == 0:
            exit()
        # wait user press 'ENTER' key
        input("Press Enter to continue...")
main()