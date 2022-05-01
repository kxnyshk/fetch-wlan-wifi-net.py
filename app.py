# FUNCTION IMPORTS
from script import exportData

# MAIN
def main():
    TEMP = exportData()
    for x in range(len(TEMP)):
        print(TEMP[x])

# RUN
def run():
    main()

# EXECUTE
run()
