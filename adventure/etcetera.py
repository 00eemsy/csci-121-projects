from room import Room

class NPC:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        room.addNPC(self)

class Narration:
    def __init__(self, narration, room):
        self.narration = narration
        self.room = room
        room.addNarration(self)