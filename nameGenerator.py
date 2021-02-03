import sys
import names

def getHelp():
    print("\tusage example  (nameGenerator.py -n 10 -full)")
    print("\n\t-h" + "\t\tprovides help page")
    print("\t-n" + "\t\tloops program specified amount of times")
    print("\t-full" + "\t\tprovides full name")
    print("\t-fullm" + "\t\tprovides male full name")
    print("\t-fullf" + "\t\tprovides female full name")
    print("\t-first" + "\t\tprovides first name")
    print("\t-firstm" + "\t\tprovides male first name")
    print("\t-firstf" + "\t\tprovides female first name")
    print("\t-last" + "\t\tprovides last name")

def getFullName():
    print(names.get_full_name())
    
def getFullNameMale():
    print(names.get_full_name(gender='male'))
    
def getFullNameFemale():
    print(names.get_full_name(gender='female'))
    
def getFirstName():
    print(names.get_first_name())
    
def getFirstNameMale():
    print(names.get_full_name(gender='male'))
    
def getFirstNameFemale():
    print(names.get_full_name(gender='female'))
    
def getLastName():
    print(names.get_last_name())
    
lengthSysArg = int(len(sys.argv))
if (lengthSysArg < 2):
    sys.stderr.write("E: usage: no argument specified\t-h for help")
    exit(2)


n = 0
nLoop = 1
ignore = 0
for x in range(1, len(sys.argv)):
    if sys.argv[x] == "-n":
        nLoop = int(sys.argv[x+1])
        ignore = sys.argv[x+1]
    while n < nLoop:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "-n":
                continue
            elif sys.argv[i] == ignore:
                continue
            elif sys.argv[i] == "-h":
                getHelp()
            elif sys.argv[i] == "-full":
                getFullName()
            elif sys.argv[i] == "-fullm":
                getFullNameMale()
            elif sys.argv[i] == "-fullf":
                getFullNameFemale()
            elif sys.argv[i] == "-first":
                getFirstName()
            elif sys.argv[i] == "-firstm":
                getFirstNameMale()
            elif sys.argv[i] == "-firstf":
                getFirstNameFemale()
            elif sys.argv[i] == "-last":
                getLastName()
            else:
                sys.stderr.write("E: usage: argument not found\t-h for help")
                exit(2)
        n += 1
