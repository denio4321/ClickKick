import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage
from g_python.hpacket import HPacket
from g_python.htools import RoomUsers



extension_info = {
    "title": "Click Kick",
    "description": "Application kick users by clicking them.",
    "author": "denio4321",
    "version": "1.0"
}

def show_them(users):
    for user in users:
        user_list.update({user.id: user.name})

ext = Extension(extension_info, args=sys.argv)
ext.start()
room_users = RoomUsers(ext)
room_users.on_new_users(show_them)

user_list = dict()

def kick_user(message: HMessage):
    user_id = message.packet.read_int()
    nickname = str()
    for id in user_list:
        if id == user_id:
            nickname = user_list[id]
    ext.send_to_client(HPacket('Whisper', -1, "Kicked user: " + nickname, 0, 30, 0, -1))
    ext.send_to_server(HPacket('KickUser', user_id))

ext.intercept(Direction.TO_SERVER, kick_user, 'GetSelectedBadges')
