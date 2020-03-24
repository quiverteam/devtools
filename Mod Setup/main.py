import setup

helpScreens = {"syntax":"""Command example:
testcommand \"teststring\"""",
"commands":"""Command list:
mod create <path to create mod>
help <subject>""","help":
"""List of topics:
syntax
commands"""}

#turns the input into a readable list
def console_input_parse(input):
    paramList = []
    quoteActive = False
    temp01 = ""
    for x in input:
        if (x == " " and quoteActive == False):#checks for spaces and if we are in a quote
            paramList.append(temp01)
            temp01 = ""
        elif (x == "\"" or x == "\'"):#checks if we are in a quote, handles quotes
            if (quoteActive):
                quoteActive = False
                if (temp01 == ""):
                    paramList.append(temp01)#makes sure that if there is nothing, it is counted
            else:
                quoteActive = True
        else:
            temp01 = temp01 + x
    if (len(temp01) != 0):#checks to make sure we aren't copying a blank
        paramList.append(temp01)#does a final copy to makes sure we got everything
    return paramList

#compares the command parameters from the user agains the command tree
def console_input_execute(paramList):
    if (len(paramList) > 0):
        if (paramList[0] == "mod"):
            if (paramList[1] == "setup"):
                setupmod = setup.mod(paramList[2],"E:\Quiver\Quiver-Mod-Setup\resource\createmod.zip")
                setupmod.mod_extract()
                del setupmod
                return True
        elif (paramList[0] == "help"):
            print("================================================================")
            print(shared_ui_help(paramList[1],helpScreens))
            print("================================================================")
            return True
        else:
            return False  
    else:
        return False     
#gets the help screen from a dictionary of help
def shared_ui_help(screentype,screens):
    for x in screens:
        if (x == screentype):
            return screens.get(x)

#print commands
print("HELP:")
print("================================================================")
print(shared_ui_help("syntax",helpScreens))
print("================================================================")
print(shared_ui_help("commands",helpScreens))
print("================================================================")
print(shared_ui_help("help",helpScreens))
print("================================================================")
#main program loop
while True:
    userInput = input("USER: ")
    userParams = console_input_parse(userInput)
    if (console_input_execute(userParams)):
        #print("command successful")
        pass
    else:
        print("Invalid command")