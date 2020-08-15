import firebase_simple.database_fire as db
import time, os, copy, admin_commands, hub

# Initialize connection
database = hub.database
PREFIX = "/"

class Connection:
    def __init__(self, room: str, user, password: str):
        self.room = room
        self.path = "/room/" + self.room

        self.user = user
        self.password = password
        self.messageCount = 0
        self.serverName = "Server"

        self.showDate = False
        self.ShowTime = True

        self.banned = database.load(self.path+"/consts/bans").get()
        self.admins = database.load(self.path + "/consts/admins").get()
        self.mutes = database.load(self.path + "/consts/mutes").get()

    def setupRoom(self):
        database.update(self.path, {
            "users": 0,
            "messages": [
                ["Welcome to Room: " + self.room + "!", self.serverName, self.get_time()]
            ],
            "cons": 0,
            "consts": {
                "date": False,
                "time": True,
                "msgCount": 1,
                "password": self.password,
                "admins": [self.user],
                "bans": ["*"],
                "mutes": ["*"]
            }
        })

    def isAdmin(self):
        return self.user in database.load(self.path + "/consts").get()["admins"]

    def isBanned(self):
        return self.user in database.load(self.path + "/consts").get()["bans"]

    def isMuted(self):
        return self.user in database.load(self.path + "/consts").get()["mutes"]

    def isCommand(self, message):
        return message.strip()[0] == PREFIX

    def sendMessage(self, message, server = False, svName="Server"):
        a, r = self.get_messages(), True
        if server:
            a.append([message, svName, self.get_time()])
        else:
            if self.isCommand(message):
                if self.isAdmin():
                    a.append([message, self.user, self.get_time()])
                    admin_commands.commandChoice(message, self)
                else:
                    print("You don't have permission to do that.")
                    r = False
            else:
                a.append([message, self.user, self.get_time()])

        if r:
            database.update(self.path, {
                "messages": a,
                "consts": {
                    "date": False,
                    "time": True,

                    "msgCount": self.get_messageCount() + 1,
                    "password": database.load(self.path+"/consts/").get()["password"],
                    
                    "admins": database.load(self.path+"/consts/").get()["admins"],
                    "bans": database.load(self.path+"/consts/").get()["bans"],
                    "mutes": database.load(self.path+"/consts/").get()["mutes"]
                }
            })

    @staticmethod
    def get_time():
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%d/%m/%Y %H:%M", named_tuple)

        return time_string

    def get_messages(self):
        return database.load(self.path+"/messages").get()

    def get_messageCount(self):
        return database.load(self.path+"/consts").get()["msgCount"]

def run():
    r = input("Room: ")
    p = input("Password (optional): ")
    u = input("Username: ")
    time.sleep(.5)
    c = Connection(r, u, p)
    try:
        if len(database.load(c.path + "/consts").get()["password"]) > 0:
            if p != database.load(c.path + "/consts").get()["password"]:
                os.system("color 4")
                print("Error: Password incorrect.")
                time.sleep(1)
                run()

    except:
        pass

    try:
        print("Connected.")
        c.sendMessage(c.user + " has connected to the chat!", server=True, svName="Server")
        time.sleep(1)
        os.system("cls")
        message = c.get_messages()[0]
        print(
            message[2], message[1], ">", message[0]
        )

    except:
        c.setupRoom()

    while True:
        x = input("> ")
        c.sendMessage(x)

run()