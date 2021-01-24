#!/usr/bin/env python3
import os
import json
from datetime import datetime

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

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
        return {}

def saveJson(data):
    try:
        with open("assets/list.json", "w") as file:
            json.dump(data, file, indent = 4)
    except:
        print('Have any error while we are saving new anime.')

def addAnimeJson(sName, sEp, sSea):
    # loads json data in array
    svdAn = loadJson()

    # have animes with the episode 0
    if (int(sEp) >= 0 and int(sSea) > 0 and (sName != "" or sName != " ")):
        # new object with the anime's information
        sAn = {"name": sName, "episode": int(sEp), "season": int(sSea)}
        if not svdAn:
            # add new anime in the end of array
            svdAn = [sAn]
        else:
            svdAn.append(sAn)
        # save the content in json
        saveJson(svdAn)
        print("You added a new anime to the list.")
    else:
        print("Invalid name, episode or season.")

def allAnimesJson():
    # loads json data in array
    svdAn = loadJson()

    if svdAn:
        print("Ex: <line> - <anime> (ep: <episode>, season: <season>)\n")
        for i, line in enumerate(svdAn):
            print("{} - {} (episode: {}, season: {})".format(i+1, svdAn[i]["name"], svdAn[i]["episode"], svdAn[i]["season"]))
        print("\nYou have {} animes in the list.".format(len(svdAn)))
    else:
        print("You don\'t have saved animes.")

def editAnimeJson():
    # loads json data in array
    svdAn = loadJson()

    if svdAn:
        allAnimesJson()

        line = int(input('Which line you want to delete: '))

        if (line <= len(svdAn) and line >= 1):
            print("\nYou want change: \n1 - name, episode and season\n2 - episode and season\n3 - only name\n4 - only episode\n5 - only season\n\nEditing: {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"]))
            op = int(input("\nOption: "))

            acName = svdAn[line-1]["name"]
            acEp = svdAn[line-1]["episode"]
            acSea = svdAn[line-1]["season"]
            if (op == 1):
                nName = input('Enter the name: ')
                nEp = int(input('Enter the episode: '))
                nSea = int(input('Enter the season: '))

                if (nEp >= 0 and nSea > 0 and (nName != "" or nName != " ")):
                    print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], nName, nEp, nSea))
                    svdAn[line-1] = {"name": nName, "episode": int(nEp), "season": int(nSea)}
                else:
                    print("Invalid selected name, episode or season.")
            if (op == 2):
                nEp = int(input('Enter the episode: '))
                nSea = int(input('Enter the season: '))

                if (nEp >= 0 and nSea > 0):
                    print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], acName, nEp, nSea))
                    svdAn[line-1] = {"name": acName, "episode": int(nEp), "season": int(nSea)}
                else:
                    print("Invalid selected episode or season.")
            if (op == 3):
                nName = input('Enter the name: ')

                if (nName != "" and nName != " "):
                    print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], nName, acEp, acSea))
                    svdAn[line-1] = {"name": nName, "episode": acEp, "season": acSea}
                else:
                    print("Invalid selected name.")
            if (op == 4):
                nEp = int(input('Enter the episode: '))

                if (nEp >= 0):
                    print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], acName, nEp, acSea))
                    svdAn[line-1] = {"name": acName, "episode": int(nEp), "season": acSea}
                else:
                    print("Invalid selected episode.")
            if (op == 5):
                nSea = int(input('Enter the season: '))

                if (nSea > 0):
                    print("\nEdit: {} - (episode: {}, season: {}) to {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"], acName, acEp, nSea))
                    svdAn[line-1] = {"name": acName, "episode": acEp, "season": int(nSea)}
                else:
                    print("Invalid selected season.")
            if (op > 5 or op < 1):
                print('Invalid selected option.')
            saveJson(svdAn)
        else:
            print('Invalid selected line.')
    else:
        print("You don\'t have saved animes.")

def deleteAnimeJson():
    # loads json data in array
    svdAn = loadJson()

    if svdAn:
        allAnimesJson()

        line = int(input('Which line you want to delete: '))

        if (line <= len(svdAn) and line >= 1):
            print("\nRemoved: {} - (episode: {}, season: {})".format(svdAn[line-1]["name"], svdAn[line-1]["episode"], svdAn[line-1]["season"]))

            svdAn.pop(line-1)
            saveJson(svdAn)
        else:
            print('Invalid selected line.')
    else:
        print("You don\'t have saved animes.")

def convertToTxt():
    # loads json data in array
    svdAn = loadJson()

    if svdAn:
        try:
            with open('assets/list.txt', 'w', encoding = 'utf-8') as file:
                for i, line in enumerate(svdAn):
                    fAnimes = "{} (episode: {}, season: {})\n".format(svdAn[i]["name"], svdAn[i]["episode"], svdAn[i]["season"])
                    # add new anime at the EOF - <anime> (ep: <episode>, season: <season>)
                    file.write(fAnimes)
        except:
            print('Have any error in .txt conversion of file.')

def main():
    print('Welcome, today is: {};'.format(theTime(1)))
    
    sOp = -1
    while sOp != 0:
        print('----------MENU----------')
        print('Select an option:\n1 - CREATE\n2 - VIEW\n3 - EDIT\n4 - DELETE\n0 - EXIT')
        sOp = int(input('\nEnter selected option: '))

        if sOp == 1:
            print('\n----------START CREATE ANIMES----------\n')
            name = input('Enter the name: ')
            ep = input('Enter the episode: ')
            sea = input('Enter the season: ')

            addAnimeJson(name, ep, sea)
            print('\n----------END CREATE ANIMES----------\n')
        if sOp == 2:
            print('\n----------START VIEW ANIMES----------\n')
            allAnimesJson()
            print('\n----------END VIEW ANIMES----------\n')
        if sOp == 3:
            print('\n----------START EDIT ANIMES----------\n')
            editAnimeJson()
            print('\n----------END EDIT ANIMES----------\n')
        if sOp == 4:
            print('\n----------START DELETE ANIMES----------\n')
            deleteAnimeJson()
            print('\n----------END DELETE ANIMES----------\n')
        if ((sOp < 1 and sOp != 0) or sOp > 5):
            print('(^-^)b - "sorry, i can\'t make this."')
        if sOp == 0:
            exit()
        convertToTxt()
        # wait user press 'ENTER' key
        input("Press Enter to continue...")

        # clear console
        clear()
main()