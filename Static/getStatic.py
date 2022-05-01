# MODE
MODE = 'r'

# GET STATIC TXT
def getFetch():
    PATH = './Static/fetch.txt'
    f = open(PATH, MODE)
    return f.read()

def getSuccess():
    PATH = './Static/success.txt'
    f = open(PATH, MODE)
    return f.read()

def getParse():
    PATH = './Static/parse.txt'
    f = open(PATH, MODE)
    return f.read()

def getNotFound():
    PATH = './Static/notfound.txt'
    f = open(PATH, MODE)
    return f.read()

def getExit():
    PATH = './Static/exit.txt'
    f = open(PATH, MODE)
    return f.read()