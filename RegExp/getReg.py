# MODE
MODE = 'r'

# GET REGULAR EXPRESIONS
def getProfiles():
    PATH = './RegExp/profiles.txt'
    f = open(PATH, MODE)
    return f.read()

def getAbsentKey():
    PATH = './RegExp/keyAbsent.txt'
    f = open(PATH, MODE)
    return f.read()

def getKeyContent():
    PATH = './RegExp/keyContent.txt'
    f = open(PATH, MODE)
    return f.read()