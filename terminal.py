import cmd
import socket
import getpass
import subprocess
import sys
import os

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
################## class color End ##############
################## init Start ##############
allCommands = [
'read',
'echo',
'if',
'help',
'exit',
'clear',
'else',
'history',
'cd'
]
main_color = color()

historyFile = open('.history','a+')

if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')
################## init End ##############
################## Main Loop Start ##############
class Shell(cmd.Cmd):
    prompt=main_color.printGG(getpass.getuser()+"@"+socket.gethostname()+": ")+main_color.printBB(os.getcwd()+" $ ")
    def do_cd(self,args):
        RealCommands=list()
        if ';' in args:
            args=args.split(';')
            RealCommands=['cd '+args[0].strip()]
            args.remove(args[0])
            RealCommands+=list(map(str.strip, args))
        else:
            historyFile.write('cd '+str(args))
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>1:
            args = ''
            for args in RealCommands:
                if len(args) == 0:
                    continue
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    eval("self.default('"+' '.join(args)+"')")
        else:
            try:
                os.chdir(args)
                self.prompt=main_color.printGG(getpass.getuser()+"@"+socket.gethostname()+": ")+main_color.printBB(os.getcwd()+" $ ")
            except:
                print(main_color.printYY("An error occured while trying to change directory\nCheck if that directory exists!"))
    def do_echo(self, args):
        RealCommands=list()
        if ';' in args:
            args=args.split(';')
            RealCommands=['echo '+args[0].strip()]
            args.remove(args[0])
            RealCommands+=list(map(str.strip, args))
        else:
            historyFile.write('echo '+str(args))
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>1:
            args = ''
            for args in RealCommands:
                if len(args) == 0:
                    continue
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    eval("self.default('"+' '.join(args)+"')")
        else:
            if args[0] == '$':
                try:
                    print(globals()[args[1:]])
                except:
                    print('')
            else:
                print(args)
    def do_exit(self,args):
        historyFile.write('exit')
        historyFile.write('\n')
        historyFile.flush()
        raise Exception('Exit')
    def do_read(self,args):
        RealCommands=list()
        if ';' in args:
            args=args.split(';')
            RealCommands=['read '+args[0].strip()]
            args.remove(args[0])
            RealCommands+=list(map(str.strip, args))
        else:
            historyFile.write("read "+str(args))
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>1:
            args = ''
            for args in RealCommands:
                if len(args) == 0:
                    continue
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    eval("self.default('"+' '.join(args)+"')")
        else:
            args=args.split(' ')[0]
            globals()[args]=input()
    def do_history(self,args):
        RealCommands = ['history']
        if ';' in args:
            args=args.split(';')
            RealCommands+=list(map(str.strip, args))
        else:
            historyFile.write("history "+str(args))
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>1:
            args = ''
            for args in RealCommands:
                if len(args) == 0:
                    continue
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    eval("self.default('"+' '.join(args)+"')")
        else:
            historyFile.seek(0)
            for num, TEMP in enumerate(historyFile, start=1):
                print('{}  {}'.format(num, TEMP.strip()))
    def do_help(self,args):
        RealCommands = ['help']
        if ';' in args:
            args=args.split(';')
            RealCommands+=list(map(str.strip, args))
        else:
            historyFile.write('help')
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>1:
            args = ''
            for args in RealCommands:
                if len(args) == 0:
                    continue
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    eval("self.default('"+' '.join(args)+"')")
        else:
            print(main_color.printC("echo: for printing a text \nclear: for clear terminal \nexit: for exiting terminal \nhelp: for show the commands \n"))
    def do_if(self,args):
        historyFile.write('if '+str(args))
        historyFile.write('\n')
        historyFile.flush()
        commandsToRun=list()
        if ';' in args:
            if 'fi' in args:
                commandsToRun=args.split(';')
                commandsToRun=list(map(str.strip, commandsToRun))
                commandsToRun.remove(commandsToRun[0])
                args=args.split(' ')
            else:
                commandsToRun=args.split(';')
                commandsToRun.remove(commandsToRun[0])
                args=args.split(' ')
                while True:
                    TEMP=input("> ")
                    if ';' in TEMP:
                        commandsToRun+=TEMP.split(';')
                        if 'fi' in list(map(str.strip,TEMP.split(';'))):
                            break
                    else:
                        commandsToRun.append(TEMP)
                        if TEMP == "fi":
                            break
                commandsToRun=list(map(str.strip, commandsToRun))
        else:
            args=args.split(' ')
            while True:
                TEMP=input("> ")
                if ';' in TEMP:
                    commandsToRun+=TEMP.split(';')
                    if 'fi' in list(map(str.strip,TEMP.split(';'))):
                        break
                else:
                    commandsToRun.append(TEMP)
                    if TEMP == "fi":
                        break
            commandsToRun=list(map(str.strip, commandsToRun))
        TEMP=[s for s in args if "$" in s]
        for s in TEMP:
            args[args.index(s)]=globals()[s[1:]]
        if args[1] == '==':
            if args[0] == args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if args[1] == '>':
            if args[0] > args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if args[1] == '<':
            if args[0] < args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if args[1] == '>=':
            if args[0] >= args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if args[1] == '<=':
            if args[0] <= args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if args[1] == '!=':
            if args[0] != args[2]:
                try:
                    for TEMP in commandsToRun[:commandsToRun.index('else')]:
                        if str(TEMP.split(' ')[0]) in allCommands:
                            eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+' '.join(TEMP)+"')")
                except:
                    for TEMP in range(len(commandsToRun[:commandsToRun.index('fi')])):
                        if str(commandsToRun[TEMP].split(' ')[0]) in allCommands:
                            eval("self.do_"+str(commandsToRun[TEMP].split(' ')[0])+"('"+' '.join(commandsToRun[TEMP].split(' ')[1:])+"')")
                        else:
                            eval("self.default('"+str(commandsToRun[TEMP])+"')")
            elif 'else' in commandsToRun:
                for TEMP in commandsToRun[commandsToRun.index('else')+1:commandsToRun.index('fi')]:
                    if str(TEMP.split(' ')[0]) in allCommands:
                        eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                    else:
                        eval("self.default('"+' '.join(TEMP)+"')")

        if len(commandsToRun[commandsToRun.index('fi'):]) > 1:
            for TEMP in commandsToRun[commandsToRun.index('fi')+1:]:
                if str(TEMP.split(' ')[0]) in allCommands:
                    eval("self.do_"+str(TEMP.split(' ')[0])+"('"+' '.join(TEMP.split(' ')[1:])+"')")
                else:
                    eval("self.default('"+' '.join(TEMP)+"')")

    def default(self,args):
        RealCommands = list()
        if ';' in args:
            args=args.split(';')
            RealCommands=list(map(str.strip, args))
        else:
            historyFile.write(args)
            historyFile.write('\n')
            historyFile.flush()
        if len(RealCommands)>0:
            args = ''
            for args in RealCommands:
                args=args.split(' ')
                if args[0] in allCommands:
                    eval("self.do_"+str(args[0])+"('"+' '.join(args[1:])+"')")
                else:
                    if os.name == "nt" and args[0]=='clear':
                        os.system('cls')
                    else:
                        try:
                            rc = subprocess.call(args, stdout=sys.stdout, stderr=subprocess.STDOUT)
                            print('Command returned '+str(rc))
                        except:
                             print(main_color.printRR('An error occured while running that command!'))
                             print(main_color.printR('Double check your command for any typo'))
        else:
            args=args.split(' ')
            if os.name == "nt" and args[0]=='clear':
                os.system('cls')
            else:
                try:
                    rc = subprocess.call(args, stdout=sys.stdout, stderr=subprocess.STDOUT)
                    print('Command returned '+str(rc))
                except:
                    print(main_color.printRR('An error occured while running that command!'))
                    print(main_color.printR('Double check your command for any typo'))

################## Main Loop End ##############
################## Final ##############
try:
    Shell().cmdloop()
except Exception:
    historyFile.close()
################## Final ##############
