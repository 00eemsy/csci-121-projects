from room import Room

class NPC:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        room.addNPC(self)

