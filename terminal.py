import getpass
import socket
import os
import sys
import subprocess
#cls = lambda: print('\n' * 100)
os.system('cls')
################## class color Start ##################
class color:
    def __init__(self):
        self.cyan='\033[96m'
        self.blue='\033[94m'
        self.green='\033[92m'
        self.yellow='\033[93m'
        self.red='\033[91m'
        self.end='\033[0m'
    def printC(self,string):
        print(self.cyan+string+self.end,end="")
    def printB(self,string):
        print(self.blue+string+self.end,end="")
    def printG(self,string):
        print(self.green+string+self.end,end="")
    def printY(self,string):
        print(self.yellow+string+self.end,end="")
    def printR(self,string):
        print(self.red+string+self.end,end="")
################## class color End ##################
color_main=color()
commands_main=['echo','exit','clear','help']
################## While Start ##################
while True:
    #color_main.printB(getpass.getuser())
    color_main.printB("Hex")
    color_main.printG("@"+str(socket.gethostname())+" $ ")
    command = input()
    try:
        commandName = command.split(' ')[0]
        commandArg = command.split(' ')[1]
    except:
        try:
            commandName = command.split(' ')[0]
        except:
            commandName = command
            commandArg = ''
    if command == 'exit':
        break
    elif commandName == 'echo':
        print(commandArg)
    elif command == 'clear':
        os.system('cls')
    elif command == 'help':
        color_main.printC("echo: for printing a text \nclear: for clear terminal \nexit: for exiting terminal \nhelp: for show the commands \n")
    #elif commandName not in commands_main:
    #    color_main.printR(commandName+": command not found\n")
    else:
        
    subprocess.Popen([commandName,commandArg])
################## While End ##################
