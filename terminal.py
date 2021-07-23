import cmd
import socket
import getpass
import subprocess
import sys

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
        return(self.cyan+string+self.end)
    def printB(self,string):
        return(self.blue+string+self.end)
    def printG(self,string):
        return(self.green+string+self.end)
    def printY(self,string):
        return(self.yellow+string+self.end)
    def printR(self,string):
        return(self.red+string+self.end)
    ##################### ----- #####################
    def printCC(self,string):
        return(self.cyann+string+self.end)
    def printBB(self,string):
        return(self.bluee+string+self.end)
    def printGG(self,string):
        return(self.greenn+string+self.end)
    def printYY(self,string):
        return(self.yelloww+string+self.end)
    def printRR(self,string):
        return(self.redd+string+self.end)

allCommands = [
'read',
'echo',
'if',
'help',
'exit',
'clear',
]
main_color = color()
cls = lambda: print('\n' * 100)
try:
    historyFile = open('.history','a+')
except:
    historyFile = open('.history','w+')
class Shell(cmd.Cmd):
    prompt=main_color.printBB(getpass.getuser())+main_color.printGG("@"+socket.gethostname()+" $ ")
    def do_echo(self, args):
        historyFile.write('echo '+str(args))
        historyFile.write('\n')
        historyFile.flush()
        if args[0] == '$':
            print(globals()[args[1:]])
        else:
            print(''.join(args))
    def do_exit(self,args):
        historyFile.write('exit')
        historyFile.write('\n')
        historyFile.flush()
        return True
    def do_clear(self,args):
        historyFile.write("clear")
        historyFile.write('\n')
        historyFile.flush()
        cls()
    def do_read(self,args):
        historyFile.write("read "+str(args))
        historyFile.write('\n')
        historyFile.flush()
        args=args.split(' ')[0]
        globals()[args]=input()
    def do_help(self,args):
        historyFile.write('help')
        historyFile.write('\n')
        historyFile.flush()
        print(main_color.printC("echo: for printing a text \nclear: for clear terminal \nexit: for exiting terminal \nhelp: for show the commands \n"))
    def do_if(self,args):
        historyFile.write('if '+str(args))
        historyFile.write('\n')
        historyFile.flush()
        args=args.split(' ')
        commandsToRun=list()
        while True:
            TEMP=input("> ")
            if TEMP == "fi":
                break
            commandsToRun.append(TEMP)
        if args[0][0]=="$":
            try:
                args[0]=globals()[args[0][1:]]
            except:
                args[0]=""
        if args[2][0]=="$":
            try:
                args[2]=globals()[args[2][1:]]
            except:
                args[2]=""
        if args[1] == '==':
            if args[0] == args[2]:
                for TEMP in range(len(commandsToRun)):
                    if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                        eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"("+str(commandsToRun[TEMP].split(' ')[1:])+")")
                    else:
                        eval("self.default('"+str(commandsToRun[TEMP])+"')")
    def default(self,args):
        historyFile.write(args)
        historyFile.write('\n')
        historyFile.flush()
        args=args.split(' ')
        try:
            rc = subprocess.call(args, stdout=sys.stdout, stderr=subprocess.STDOUT)
            print('Command returned '+str(rc))
        except:
             print(main_color.printRR('An error occured while running that command!'))
             print(main_color.printR('Double check your command for any typo'))


Shell().cmdloop()
historyFile.close()
