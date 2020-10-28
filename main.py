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

            # return notes lenght in file
            return len(qSa)
    except:
        return -1

def addAnime(tAnime):
    with open('assets/list.txt', 'a', encoding = 'utf-8') as file:
        # write new note at the EOF line - <note> on <MM/DD/YYYY>
        file.write('{}'.format(tAnime))
    print('You added a new anime to the list.')

def main():
    print('Welcome, today is: {};'.format(theTime(1)))
    print('----------MENU----------')
    
    sOp = -1
    while sOp != 0:
        print('Select an option:\n1 - CREATE\n0 - EXIT')
        sOp = int(input('\nEnter selected option: '))

        if sOp == 1:
            print('\n----------START CREATE ANIMES----------\n')
            name = input('Enter the name: ')
            ep = input('Enter the episode: ')
            sea = input('Enter the season: ')

            dAnime = '{} (ep: {}, season: {})\n'.format(name, ep, sea)
            addAnime(dAnime)
            print('\n----------END CREATE ANIMES----------\n')
        if ((sOp < 1 and sOp != 0) or sOp > 4):
            print('(^∇^)b - "sorry, i can\'t make this."')
        if sOp == 0:
            exit()
        # wait user press 'ENTER' key
        input("Press Enter to continue...")
main()