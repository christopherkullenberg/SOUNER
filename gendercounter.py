#!/usr/bin/env python3
#from sys import argv
import re

'''
A series of functions for counting gendered Swedish names in text.
Import this script along with the tsv files containing names and frequencies:

  female250.tsv
  male250.tsv

Then you can:

  import gendercouter

Then the following function will take text as input:

  gendercounter.textinput('Hej hen heter Lisa eller Kalle')

Wich will return the result as tuples and dictionaries like so:

  (({'Lisa': '31611'}, 1), ({'Kalle': '2903'}, 1), (1, 0, 0), (0, 0, 0), (0, 0, 0))

The output is explained here:

https://github.com/christopherkullenberg/gendercounter

The commented out lines can be used to convert this to a script that takes
files as input.
'''

#script, filename = argv
#thefile = open(filename, 'r')
#thetext = thefile.read()

def textinput(text):
    '''When used as a module, this function returns the results in tuples and
    dictionaries. See the printresultsterminal() function below.'''
    textsplit = text.split()
    text = []
    # This loop removes special chars from each word.
    for t in textsplit:
        tclean = re.sub(r'[.,\?!]+',r'',t)
        text.append(tclean)

    kvinnorslutresultat = raknakvinnor(loadkvinnodict(), text)
    maenslutresultat = raknamaen(loadmaendict(), text)
    henslutresultat = raknahen(text)
    honslutresultat = raknahon(text)
    hanslutresultat = raknahan(text)
    return(kvinnorslutresultat, maenslutresultat, henslutresultat,
    honslutresultat, hanslutresultat)

def loadkvinnodict():
    '''Open the name lists: [0] is freq and [1] is name. Return as dict.'''
    kvinnodict = {}
    with open('female250.tsv', 'r', encoding='utf-8') as kvinnofile:
        kvinnor = zip((line.strip().split('\t') for line in kvinnofile))
        for row in kvinnor:
            for r in row:
                kvinnodict[r[1]] = r[0]
        return(kvinnodict)

def loadmaendict():
    maendict = {}
    with open('male250.tsv', 'r', encoding='utf-8') as maenfile:
        maen = zip((line.strip().split('\t') for line in maenfile))
        for row in maen:
            for r in row:
                maendict[r[1]] = r[0]
    return(maendict)

def raknakvinnor(kvinnodict, text):
    kvinnocounter = 0 #counts absolute numbers of names
    kvinnonamnfrekvens = {} #counts unique names
    for t in text:
        if t in kvinnodict:
            kvinnonamnfrekvens[t] = kvinnodict[t]
            kvinnocounter += 1
    return(kvinnonamnfrekvens, kvinnocounter)

def raknamaen(maendict, text):
    maencounter = 0
    maennamnfrekvens = {}
    for t in text:
        if t in maendict:
            maennamnfrekvens[t] = maendict[t]
            maencounter += 1
    return(maennamnfrekvens, maencounter)

def raknahen(text):
    hen = 0
    henom = 0
    hens = 0
    for t in text:
        henregexp = re.findall(r'\bhen\b', t, flags = re.IGNORECASE)
        henomregexp = re.findall(r'\bhenom\b', t, flags = re.IGNORECASE)
        hensregexp = re.findall(r'\bhens\b', t, flags = re.IGNORECASE)
        if henregexp:
            hen += 1
        elif henomregexp:
            henom += 1
        elif hensregexp:
            hens += 1
        else:
            continue
    return(hen, henom, hens)

def raknahon(text):
    hon = 0
    henne = 0
    hennes = 0
    for t in text:
        honregexp = re.findall(r'\bhon\b', t, flags = re.IGNORECASE)
        henneregexp = re.findall(r'\bhenne\b', t, flags = re.IGNORECASE)
        hennesregexp = re.findall(r'\bhennes\b', t, flags = re.IGNORECASE)
        if honregexp:
            hon += 1
        elif henneregexp:
            henne += 1
        elif hennesregexp:
            hennes += 1
        else:
            continue
    return(hon, henne, hennes)

def raknahan(text):
    han = 0
    honom = 0
    hans = 0
    for t in text:
        hanregexp = re.findall(r'\bhan\b', t, flags = re.IGNORECASE)
        honomregexp = re.findall(r'\bhonom\b', t, flags = re.IGNORECASE)
        hansregexp = re.findall(r'\bhans\b', t, flags = re.IGNORECASE)
        if hanregexp:
            han += 1
        elif honomregexp:
            honom += 1
        elif hansregexp:
            hans += 1
        else:
            continue
    return(han, honom, hans)

'''
def printresultsterminal():
    #This function can be invoked to print out a clean terminal output
    print("Det finns " + str(len(result[0][0])) + " unika kvinnonamn i texten.")
    print("Det finns " + str(len(result[1][0])) + " unika mansnamn i texten.")
    print("Kvinnonamn: " + str(result[0]))
    print("Mansnamn: " + str(result[1]))
    print("Absoluta tal kvinnor: " + str(result[0][1]))
    print("Absoluta tal män: " + str(result[1][1]))
    print("Antalet hen, henom, hens : " + str(result[2]))
    print("Antalet hon, henne, hennes : " + str(result[3]))
    print("Antalet han*, honom, hans* : " + str(result[4]))
    print('Obs: "Han" och "Hans" kan också vara manliga förnamn.')
'''

#result = textinput(thetext)
#printresultsterminal()
