import sys
from time import sleep
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

ext = Extension(extension_info, args=sys.argv)
ext.start()

def kick_user(message: HMessage):
    user_id = message.packet.read_int()
    ext.send_to_client(HPacket('Whisper', -1, "Kicked user with ID: " + str(user_id), 0, 30, 0, -1))
    ext.send_to_server(HPacket('KickUser', user_id))

ext.intercept(Direction.TO_SERVER, kick_user, 'GetSelectedBadges')
