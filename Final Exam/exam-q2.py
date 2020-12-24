"""
Prompt for filename (default warning)
import os
if filename not present
    print default warning
    set filename as lines.txt with read and open
else
    filename is input
stringsearch is string with space (not empty)
while loop stays open until user enters empty string
    string search is prompt
    if length of input is <=5
        if input is present
            print found
        else
            print not found
    else (where input >5)
        if input is present
            print found
        else
            print not found, search prefixes (iterative for loop until characters are less than 5)
            take last character off input
            for loop iterating through characters in input
                print search
                if input present
                    print found
                    break
                take last character off input
                if length of input is less than 5
                    print not found
                    break
print finished
"""
#file selection
fileName=input('Enter a file to operate on (default is lines.txt): ')
import os
if not os.path.isfile(fileName):
    print('File not found, defaulting to lines.txt')
    fileName=open('lines.txt','r').read()
else:
    fileName=open(fileName,'r').read()

#string selection
stringSearch=' '
while stringSearch!='':
    stringSearch=input('Enter a string (empty string to exit): ')

    #search for strings <=5, doesn't do prefix search if not found immediately
    if len(stringSearch)<=5:
        if stringSearch in fileName:
            print('The search string',stringSearch,'was found.')
        else:
            print('The search string',stringSearch,'was not found.')

    #search for strings >5, iterative prefix search if not found immediately
    else:
        if stringSearch in fileName:
            print('The search string',stringSearch,'or a prefix of it was found.')
        else:
            print('Didn\'t find',stringSearch+'. Now searching for prefixes...')
            stringSearch=stringSearch[:-1]

            #iterative prefix search (non-recursive)
            for char in stringSearch:
                print('Searching for:',stringSearch,'length of s:',len(stringSearch),'minlen: 5')
                if stringSearch in fileName:
                    print('The search string',stringSearch,'or a prefix of it was found.')
                    break
                stringSearch=stringSearch[:-1]
                if len(stringSearch)<5:
                    print('Neither the search string',stringSearch,'nor any of its prefixes of it was found.')
                    break
print('Finished!')
        