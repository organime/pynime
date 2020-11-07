#!/usr/bin/env python3
import os
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

def getLen():
    try:
        with open('assets/list.txt', 'r', encoding = 'utf-8') as file:
            # returns a list of remaining lines of the entire file
            qSa = file.readlines()

            # return quantity of animes in file
            return len(qSa)
    except:
        return -1

def addAnime(tAnime):
    try:
        with open('assets/list.txt', 'a', encoding = 'utf-8') as file:
            # add new anime at the EOF - <anime> (ep: <episode>, season: <season>)
            file.write('{}'.format(tAnime))
        print('You added a new anime to the list.')
        
    except:
        print('We have any error while opening the file.')

def allAnimes():
    try:
        with open('assets/list.txt', 'r', encoding = 'utf-8') as file:
            # bring file cursor to initial position
            file.seek(0)
            allLines = file.readlines()

            for i, line in enumerate(allLines):
                print("{} - {}".format(i+1, line.strip()))
            print("\nYou have {} animes in list.".format(getLen()))
    except:
        print('We have any error while opening the file.')

def updateEpSe():
    try:
        allLines = []
        with open('assets/list.txt', 'r', encoding = 'utf-8') as file:
            allAnimes()
            sLine = int(input('What is the line you want to change: '))

            sEp = input('Okay, enter the new episode: ')
            sSe = input('Okay, enter the new season: ')

            # returns a list of remaining lines of the entire file
            allLines = file.readlines()

            spline = allLines[sLine-1].split(" (")

            # .strip() removes any leading (spaces at the beginning) and trailing (spaces at the end)
            print('Edit "{}" to: {} (ep: {}, season: {})\n'.format(allLines[sLine-1].strip(), spline[0].strip(), sEp, sSe))
            allLines[sLine - 1] = '{} (ep: {}, season: {})\n'.format(spline[0].strip(), sEp, sSe)

        with open('assets/list.txt', 'w', encoding = 'utf-8') as file:
            for nLines in allLines:
                file.write(nLines)
        print('Your anime are edited with success.')
    except:
        print('We have any error while opening the file.')

def delete():
    try:
        allLines = []

        allAnimes()
        sLine = int(input('What is the line you want to delete: '))

        if sLine <= getLen() and sLine >= 1:
            with open('assets/list.txt', 'r', encoding = 'utf-8') as file:
                # .pop() removes the element at the specified position
                allLines = file.readlines()
                allLines.pop(sLine - 1)

                with open('assets/list.txt', 'w', encoding = 'utf-8') as file:
                    for nLines in allLines:
                        file.write(nLines)
            print('Your anime are deleted with success.')
        else:
            print("Invalid line.")
    except:
        print('We have any error while opening the file.')

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

            dAnime = '{} (ep: {}, season: {})\n'.format(name, ep, sea)
            addAnime(dAnime)
            print('\n----------END CREATE ANIMES----------\n')
        if sOp == 2:
            print('\n----------START READ ANIMES----------\nEx: <line> - <anime> (ep: <episode>, season: <season>)\n')
            allAnimes()
            print('\n----------END READ ANIMES----------\n')
        if sOp == 3:
            print('\n----------START EDIT ANIMES----------\n')
            updateEpSe()
            print('\n----------END EDIT ANIMES----------\n')
        if sOp == 4:
            print('\n----------START DELETE ANIMES----------\n')
            delete()
            print('\n----------END DELETE ANIMES----------\n')
        if ((sOp < 1 and sOp != 0) or sOp > 4):
            print('(^-^)b - "sorry, i can\'t make this."')
        if sOp == 0:
            exit()
        # wait user press 'ENTER' key
        input("Press Enter to continue...")
main()