import firebase_simple.database_fire as db
import time, os, copy, hub

# Initialize connection
database = hub.database
PREFIX = "/"

def isAdmin(self):
    return self.user in database.load(self.path + "/consts").get()["admins"]

def serverMessage(self, message):
    self.sendMessage(message, server=True, svName="AutoMod")

def ban(self, message):
    new_banned = copy.deepcopy(database.load(self.path + "/consts/bans").get())
    new_banned.append(message.split(" ")[1])
    database.update(self.path,
                    {"consts": {
                        "date": False,
                        "time": True,
                        "msgCount": self.get_messageCount(),
                        "password": self.password,
                        "admins": database.load(self.path + "/consts/").get()["admins"],
                        "bans": new_banned,
                        "mutes": database.load(self.path + "/consts/").get()["mutes"]
                    }})
    print(message.split(" ")[1] + " is now banned from the chat room.")

def mute(self, message):
    new_muted = copy.deepcopy(database.load(self.path + "/consts/mutes").get())
    new_muted.append(message.split(" ")[1])
    database.update(self.path,
                    {"consts": {
                        "date": False,
                        "time": True,
                        "msgCount": self.get_messageCount(),
                        "password": self.password,
                        "admins": database.load(self.path + "/consts/").get()["admins"],
                        "bans": database.load(self.path + "/consts/").get()["bans"],
                        "mutes": new_muted
                    }})
    print(message.split(" ")[1] + " is now muted in the chat room.")

def mod(self, message):
    new_admins = copy.deepcopy(database.load(self.path + "/consts/admins").get())
    new_admins.append(message.split(" ")[1])
    database.update(self.path,
                    {"consts": {
                        "date": False,
                        "time": True,
                        "msgCount": self.get_messageCount(),
                        "password": self.password,
                        "admins": new_admins,
                        "bans": database.load(self.path + "/consts/").get()["bans"],
                        "mutes": database.load(self.path + "/consts/").get()["mutes"]
                    }})
    print(message.split(" ")[1] + " is now modded.")

def commandChoice(message, self):
    command = message.strip().split(" ")[0][1:]

    if command.lower() == "ban": ban(self, message)
    elif command.lower() == "mute": mute(self, message)
    elif command.lower() == "mod": mod(self, message)

    else:
        print("Invalid command.")