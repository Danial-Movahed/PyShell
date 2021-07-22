import cmd
import socket
import getpass

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
main_color = color()
cls = lambda: print('\n' * 100)
class Shell(cmd.Cmd):
    prompt=main_color.printBB(getpass.getuser())+main_color.printGG("@"+socket.gethostname()+" $ ")
    def do_echo(self, args):
        if args[0] == '$':
            print(globals()[args.split(' ')[0]])
        else:
            print(args)
    def do_exit(self):
        return True
    def do_clear(self):
        cls()
    def do_read(self,arg):
        arg=arg.split(' ')[0]
        globals()[arg]=input()



Shell().cmdloop()
