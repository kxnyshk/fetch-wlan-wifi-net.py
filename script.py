# LIB IMPORTS
import re
import subprocess
import sys

# TIME MOD
from time import sleep

# IMPORTING REGULAR EXPRESSIONS
from RegExp.getReg import getProfiles
from RegExp.getReg import getAbsentKey
from RegExp.getReg import getKeyContent

# IMPORTING STATIC TXT
from Static.getStatic import getFetch
from Static.getStatic import getSuccess
from Static.getStatic import getParse
from Static.getStatic import getNotFound
from Static.getStatic import getExit

# RUNNING SUBPROCESS
PROFILES_DATA = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

# SATURATING DATA
PROFILES = (re.findall(f'{getProfiles()}(.*)\r', PROFILES_DATA))

# FETCHING WLAN DATA
WLANS = []

def fetchData():
    if (len(PROFILES) != 0):
        for P in PROFILES:
            WLAN_PROFILE = {}
            WLAN_DATA = subprocess.run(["netsh", "wlan", "show", "profiles", P], capture_output=True).stdout.decode()

            if re.search(getAbsentKey(), WLAN_DATA):
                continue
            else:
                WLAN_PROFILE["Network"] = P
                WLAN_PWD_DATA = subprocess.run(["netsh", "wlan", "show", "profiles", P, "key=clear"], capture_output=True).stdout.decode()
                WLAN_PWD = re.search(f'{getKeyContent()}(.*)\r', WLAN_PWD_DATA)

                if WLAN_PWD == None:
                    WLAN_PROFILE["Password"] = None
                else:
                    WLAN_PROFILE["password"] = WLAN_PWD[1]
                
                WLANS.append(WLAN_PROFILE)
    
    return WLANS

# INITIALIZING
def init():
    print(getFetch())
    sleep(2)
    print(getSuccess())
    sleep(2)
    print(getParse())
    sleep(2)

# EXPORTING DATA
def exportData():
    TEMP = fetchData()
    # TEMP = []
    if(len(TEMP) != 0):
        init()
        return TEMP
    else:
        print(getNotFound())
        sleep(1)
        print(getExit())
        sleep(1)
        sys.exit(0)
