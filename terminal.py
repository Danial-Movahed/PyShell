import getpass
import socket
import os
import sys
import subprocess
cls = lambda: print('\n' * 100)
################## class color Start ##############
class color:
    def __init__(self):
        self.cyan='\033[96m'
        self.blue='\033[94m'
        self.green='\033[92m'
        self.yellow='\033[93m'
        self.red='\033[91m'
        ##################### ----- #####################
        self.redd='\033[31m'
        self.cyann='\033[36m'
        self.bluee='\033[34m'
        self.greenn='\033[32m'
        self.yelloww='\033[33m'

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
    ##################### ----- #####################
    def printCC(self,string):
        print(self.cyann+string+self.end,end="")
    def printBB(self,string):
        print(self.bluee+string+self.end,end="")
    def printGG(self,string):
        print(self.greenn+string+self.end,end="")
    def printYY(self,string):
        print(self.yelloww+string+self.end,end="")
    def printRR(self,string):
        print(self.redd+string+self.end,end="")
################## class color End ##############
color_main=color()
################## While Start ##################
while True:
    color_main.printB(getpass.getuser())
    color_main.printG("@"+str(socket.gethostname())+" $ ")
    command = input()
    try:
        commandName = command.split(' ')[0]
        commandArg = command.split(' ')[1:]
    except:
        commandName = command
        commandArg = ''
    if commandName == 'exit':
        break
    elif commandName == 'echo':
        if commandArg[0][0]=='$':
            try:
                print(globals()[commandArg[0][1:]])
            except:
                print("")
        else:
            for i in range(len(commandArg)):
                print(commandArg[i],end=' ')
            print('')
    elif commandName == 'clear':
        cls()
    elif commandName == 'help':
        color_main.printC("echo: for printing a text \nclear: for clear terminal \nexit: for exiting terminal \nhelp: for show the commands \n")
    elif commandName == 'read':
        globals()[commandArg[0]]=input()
    elif command:
        cmd=list()
        cmd.append(commandName)
        cmd+=commandArg
        try:
            rc = subprocess.call(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT)
            print('Command returned '+str(rc))
        except:
             color_main.printR('An error occured while running that command!')
             print('')
             color_main.printY('Double check your command for any typo')
             print('')
################## While End ##################
