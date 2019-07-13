import os, sys, subprocess

class Launch:
    def __init__(self):
        self.f = 1

    def main(self):
        failT = False
        failO = False
        self.resize(80,24)
        try:
            tkn = open("token.txt","r").readline()
        except:
            failT = True
        try:
            f = open("owner.txt", "r").readline().split(",")
        except:
            failO = True
        if failT or failO is not False:
            self.head("First boot or missing files!")
            print("")
            if failT == True:
                self.token()
            if failO == True:
                self.id()
        self.menu()
        
    def menu(self):
        self.head("Boot Menu")
        print("")
        print("1. Boot bot")
        print("2. Maintenance menu")
        print("3. Exit")
        x = input("Type number: ")
        if x == "1":
            self.boot()
        elif x == "2":
            self.cls()
            self.maintenance()
        elif x == "3":
            exit()
        else:
            print("Invalid option!")
            self.menu()

    def maintenance(self):
        self.head("Maintenance Menu", False)
        print("")
        print("1. Update bot")
        print("2. Update requirements")
        print("3. Update all")
        print("4. Delete database")
        print("5. Factory reset")
        print("6. Go back")
        x = input("Type number: ")
        if x == "1":
            self.update()
            self.maintenance()
        elif x == "2":
            self.req()
            self.maintenance()
        elif x == "3":
            self.update()
            self.req(False)
            self.maintenance()
        elif x == "4":
            self.delete()
            self.maintenance()
        elif x == "5":
            self.factory()
            self.maintenance()
        elif x == "6":
            self.menu()
        else:
            print("Invalid option!")
            self.maintenance()

    def factory(self):
        print("Are you sure you want to do this?")
        print("All bot data will be wiped, and the latest reinstalled!")
        print("THIS ACTION IS IRREVERSABLE!")
        x = input("y/n: ")
        if x == "y":
            os.system("git fetch origin")
            os.system("git reset --hard origin/master")
            self.maintenance()
        elif x == "n":
            self.maintenance()
        else:
            self.factory()

    def delete(self):
        print("Are you sure you want to do this?")
        print("THIS ACTION IS IRREVERSABLE!")
        x = input("y/n: ")
        if x == "y":
            if os.path.exists("demofile.txt"): 
                os.remove("higgsbot.db")     
                print("Database deleted.")
            else:
                print("The file does not exist")
            self.maintenance()
        elif x == "n":
            self.maintenance()
        else:
            self.delete()

    def req(self, wipe = True):
        if wipe == True:
            self.cls()
        r = open("requirements.txt","r").read().replace('\n', ' ').replace('\r', '')
        print("r = {}".format(r))
        os.system("{} -m pip install {}".format(sys.executable, r))

    def update(self):
        self.cls()
        try:
            code = subprocess.call(("git", "pull", "--ff-only"))
        except FileNotFoundError:
            print("\nError: Git not found. It's either not installed or not in PATH.")
        return
        if code == 0:
            print("\nUpdated successfully.")
        else:
            print("\nUpdate failed. Did you tinker around with the code?")
    
    def boot(self):
        self.cls()
        os.system('{} bot.py'.format(sys.executable))

    def id(self):
        self.cls()
        print("Enter the user ID of the bot owner.")
        print("Multiple IDs can be seperated by commas, eg. 1234,1222,1238")
        id = input("")
        f = open("owner.txt","w+")
        f.write(id)
        f.close()

    def token(self):
        self.cls()
        print("Enter the bot token you got from the Discord developer site.")
        token = input("")
        if "." in token:
            f = open("token.txt","w+")
            f.write(token)
            f.close()
        else:
            print("That doesn't look like a valid token!")
            self.token()

    def head(self, text = None, clear = True, width = 55): # From CorpNewt's utils.py
        if clear == True:
            self.cls()
        print("  {}".format("#"*width))
        mid_len = int(round(width/2-len(text)/2)-2)
        middle = " #{}{}{}#".format(" "*mid_len, text, " "*((width - mid_len - len(text))-2))
        if len(middle) > width+1:
            # Get the difference
            di = len(middle) - width
            # Add the padding for the ...#
            di += 3
            # Trim the string
            middle = middle[:-di] + "...#"
        print(middle)
        print("#"*width)

    def resize(self, width, height): # From CorpNewt's utils.py
        print('\033[8;{};{}t'.format(height, width))

    def cls(self): # From CorpNewt's utils.py
    	os.system('cls' if os.name=='nt' else 'clear')

while True:
    Launch().main()
