import firebase_simple.database_fire as db
import time, os

# Initialize connection
database = db.Db("https://chatroom-multiuser.firebaseio.com/", "key.json")
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
                "admins": [self.user[0]],
                "bans": [],
                "mutes": []
            }
        })

    def sendMessage(self, message):
        a = c.get_messages()
        a.append([message, self.user[0], self.get_time()])

        if self.user[0] in database.load(self.path+"consts").get()["admins"]:
            if message[0] == PREFIX:
                if message.split(" ")[0][1:] == "ban":
                    database.update(self.path, {"consts": {"bans": [message.split(" ")[1]]}})
                elif message.split(" ")[0][1:] == "mute":
                    database.update(self.path, {"consts": {"mutes": [message.split(" ")[1]]}})
                elif message.split(" ")[0][1:] == "mod":
                    database.update(self.path, {"consts": {"admins": [message.split(" ")[1]]}})
                else:
                    print("Incorrect Command. (Mod, Mute & Ban Only)")

        database.update(self.path, {
            "messages": a,
            "consts": {
                "msgCount": self.get_messageCount() + 1
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

r = input("Room: ")
p = input("Password (optional): ")
u = input("Username: ")

time.sleep(.5)
c = Connection(r, [u], p)

try:
    if len(database.load(c.path + "/consts").get()["password"]) > 0:
        if p != database.load(c.path + "/consts").get()["password"]:
            os.system("color 4")
            print("Error: Password incorrect.")
            time.sleep(10)
            quit(0)

except:
    pass

try:
    print("Connected.")
    time.sleep(.5)
    os.system("cls")
    message = c.get_messages()[0]
    print(
        message[2], message[1], ">", message[0]
    )

except:
    c.setupRoom()

msgC = c.get_messageCount()

while True:
    newCount = c.get_messageCount()
    if newCount > msgC:
        message = c.get_messages()[c.get_messageCount() - 1]
        print(
            message[2], message[1], ">", message[0]
        )
        msgC = newCount

    else:
        pass