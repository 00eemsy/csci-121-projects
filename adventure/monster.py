import random
from room import Room
from item import Item

class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        room.addMonster(self)
    
    def die(self):
        self.room.removeMonster(self)
        if self.name == "FINAL BOSS SOUL SNATCHER":
            keyLoot = Item("grim hq swipe access", "overseer: WOAH? IS THAT THE HQ? go get that raise my dear grimtern.", 0)
            keyLoot.putInRoom(self.room)
        else:
            x = random.random()
            if x <= .4:
                Loot = Item("duct tape", "overseer: a soul snatcher loot item. but that raises questions: are soul snatchers made of tape? do they love duct tape? are they secretly duct tape mummies?", 1)
            else:
                Loot = Item("can of tuna", "overseer: a soul snatcher loot item. but that raises questions: are soul snatchers made of tuna? do they love canned tuna? are they secretly cats?", 1)
            Loot.putInRoom(self.room)