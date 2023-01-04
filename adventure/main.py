from room import Room
from player import Player
from item import Item
from monster import Monster
from etcetera import NPC
from etcetera import Narration
import os
import updater
import random


player = Player()

def createWorld():

    #rooms
    a = Room("current location: a random alleyway (in alleyways, sometimes our stray kitty friends can't find enough to eat...)")
    b = Room("current location: the pretty pretty park (in parks, sometimes it gets too cold for the smallest chicks...)")
    c = Room("current location: the intersection, rush hour edition (at intersections, sometimes the stupid humans drive too fast...)")
    d = Room("current location: a residential house like any other (in houses, sometimes age creeps up on us...)")
    e = Room("current location: the humans' hospital (in hospitals, sometimes it's a matter of life or death...)")
    f = Room("current location: the underworld aka grim hq (at grim hq, sometimes it's a matter of promotion or death...)")
    Room.connectRooms(a, "park", b, "alleyway")
    Room.connectRooms(b, "intersection", c, "park")
    Room.connectRooms(c, "house", d, "intersection")
    Room.connectRooms(d, "hospital", e, "house")
    Room.connectRooms(e, "underworld", f, "hospital")
    
    #items
    weapon1 = Item("sickle", "overseer: ooh! your first ever weapon. gives u +5 attack damage.", 5)
    weapon2 = Item("DOOM SCYTHE", "overseer: woah, look at you grimtern! that's a serious blade right there. gives u +10 attack damage.", 7)
    cloak = Item("edgy black cloak", "overseer: superior deathy look gives you extra protection against monsters.", 1)
    bandaid = Item("bandaid", "overseer: have a boo boo? this will give you +9 health points. not 10 bc get wrecked ig.", 0)
    skzSoul = Item("stray kitty's soul", "overseer: 1/5 souls you need to get promoted", 0)
    birdySoul = Item("birdy's soul", "overseer: 2/5 souls you need to get promoted", 0)
    opossumSoul = Item("opossum's soul", "overseer: 3/5 souls you need to get promoted", 0)
    doggoSoul = Item("fido's soul", "overseer: 4/5 souls you need to get promoted", 0)
    inpatientSoul = Item("inpatient's soul", "overseer: 5/5 souls you need to get promoted", 0)

    weapon1.putInRoom(b)
    weapon2.putInRoom(e)
    cloak.putInRoom(c)
    bandaid.putInRoom(c)
    bandaid.putInRoom(b)
    skzSoul.putInRoom(a)
    birdySoul.putInRoom(b)
    opossumSoul.putInRoom(c)
    doggoSoul.putInRoom(d)
    inpatientSoul.putInRoom(e)

    player.location = a
    
    #monster
    Monster("FINAL BOSS SOUL SNATCHER", 79, e)
    Monster("soul snatcher", 10, b)
    Monster("soul snatcher 2.0", 10, d)

    #characters
    NPC("THE GRIM REAPER", f)

    #narration
    Narration("overseer: welcome to your first day on the job! is what i, your very tired overseer, would say if i had coffee. you're a grimtern, you kill soul snatchers trying to steal souls you need to collect... blah blah blah. ugh, why did my keurig have to fail me now. (trigger warning: death)", a)
    Narration("overseer: omg your first ever soul snatcher. attack to kill it. and pls attack it... i need to get paid to fix my keurig.", b)
    Narration("overseer: i think that cloak is good. perfect corporate gear.", c)
    Narration("overseer: 2.0 looks... stronger than the other one. lol good luck.", d)
    Narration("overseer: well, welcome to your doom. since so many souls are lost here, the strongest of the strong soul snatchers lurk around here. they've also cursed this room to make it harder for us to do our jobs... your health is going to decrease slowly...", e)
    Narration("overseer: welcome to hq... finally. omg wait it's the boss man GOODBYE-", f)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # what the fuck

def printSituation():
    clear()
    print(player.location.desc)
    print()
    
    #DIALOGUEEEEEE
    if player.location.hasNarration():
        for i in player.location.narration:
            print(i.narration)
        print()
    
    if player.location.hasMonsters():
        print("look, some monsters lmao:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("hey look this room has some shiny stuff:")
        for i in player.location.items:
            print(i.name)
        print()
    if player.location.hasNPCs():
        print("and golly! ppl who want to talk to you...")
        for i in player.location.npcs:
            print(i.name)
        print()


    print("where are u heading next lil one?")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("overseer: alrighty, you need help? here you go stupid:")
    print()
    print("go <direction> -- ur moving in that direction")
    print("inventory -- check up on ur lil trinkets")
    print("pickup <item> -- pick it up. duh.")
    print("me -- check on ur mediocre stats")
    print("inspect <item> -- tells u what a thing does. gosh, dummy.")
    print("drop <item> -- adios to the item.")
    print("heal <item> -- save urself.")
    print("chat <npc> -- talk to ppl who are actually interested in talking to you. honestly, i'm surprised there are any.")
    print("craft -- with a special combo of items in your inventory, you can make the most glorious of armors.. but not coffee :(")

    print()
    input("Press enter to continue...")



createWorld()
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("overseer: what u up to lil intern fellow? ")
        commandWords = command.split()

        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            possession = False
            for i in player.items:
                if i.name == "grim hq swipe access":
                    possession = True
            if commandWords[1] == "underworld" and not possession:
                print("overseer: hey, you know this is high security stuff right? grimterny, wait until you get swipe access into hq.")
                print()
                input("Press enter to continue...")
            else:
                player.goDirection(commandWords[1]) 
                timePasses = True
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
                timePasses = True
            else:
                print("overseer: nope, u can't pick this up. the audacity.") # lmao nope (cal's suggestion)
                commandSuccess = False   
        elif commandWords[0].lower() == "inventory":
            player.showInventory()       
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "me":
            player.me()
        elif commandWords[0].lower() == "inspect":
            # if in room or in inventory
            print(player.items)
            tally1 = False
            tally2 = False
            for i in player.location.items:
                print(i.name)
                if commandWords[1] in i.name:
                    tally2 = True
                    something = i
            for i in player.items:
                print(i.name)
                if commandWords[1] in i.name:
                    thing = i
                    tally1 = True
            if tally1 == True:
                thing.describe()
                timePasses = True
            elif tally2 == True: 
                something.describe()
                timePasses = True
            else:
                print("overseer: um... this is awkward. you don't have the right to inspect that.")
        elif commandWords[0].lower() == "drop":
            count = 0
            tally = 0
            while count < len(player.items):
                if player.items[count].name == commandWords[1]:
                    tally = count
                count += 1
            player.location.addItem(player.items[tally])
            del player.items[tally]
            timePasses = True
        elif commandWords[0].lower() == "heal":
            item = commandWords[1]
            tally = False
            for i in player.items:
                if i.name == "bandaid":
                    tally = True
            if item == "bandaid" and tally == True:
                player.heal(item)
                print("overseer: healed or something... you're currently at " + str(player.health) + " health points.")
                print()
                input("Press enter to continue...")
                
                # and drop 
                count = 0
                tally = 0
                while count < len(player.items):
                    if player.items[count].name == "bandaid":
                        tally = count
                    count += 1
                del player.items[tally]
                timePasses = True
            else:
                if item == "bandaid" and tally == False:
                    print("overseer: silly, you don't have that object...")
                    print()
                    input("Press enter to continue...")
                elif item != "bandaid" and tally == True:
                    print("overseer: silly, that's not a healing object. do better.")
                    print()
                    input("Press enter to continue...")
                else:
                    print("overseer: what... what even are you doing. invalid, try again.")
                    print()
                    input("Press enter to continue...")
                commandSuccess = False    
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
                timePasses = True
            else:
                print("overseer: that monster doesn't exist dummy.")
                commandSuccess = False
        elif commandWords[0].lower() == "chat":
            tally = False

            for i in player.location.npcs:
                if i.name == "THE GRIM REAPER":
                    tally = True
                    target = "THE GRIM REAPER"

            if tally == True:
                clear()
                player.chatUp(target)
                if player.stopTheGame:
                    playing = False
                timePasses = True
            else:
                print("overseer: who are you even trying to talk to, weirdo? you know the dead souls tell no tales..")
                commandSuccess = False
        elif commandWords[0].lower() == "craft":
            tunaTally = False
            tapeTally = False
            tunaCount = 0
            tapeCount = 0
            count = 0

            while count < len(player.items):
                if player.items[count].name == "canned tuna":
                    tunaTally = True
                    tunaCount = count
                elif player.items[count].name == "duct tape":
                    tapeTally = True
                    if tunaCount == 0:
                        tapeCount = count
                    if tunaCount < tapeCount:
                        tapeCount = count - 1
                    else:
                        tapeCount = count 
                count += 1
            
            if tunaTally and tapeTally:
                del player.items[tunaCount]
                del player.items[tapeCount]
            
                ultArmor = Item("ULTIMATE ARMOR", "overseer: the most op armor in game. it reeks of tuna though...", 0)
                player.location.addItem(ultArmor)
            
                timePasses = True

        else:
            print("overseer: what sort of witchcraft are u trying to do, huh? that command doesn't exist.")
            commandSuccess = False
    
    if timePasses == True:
        if player.location.desc == "current location: the humans' hospital":
            player.health -= 5
        else:
            x = random.random()
            if x < .5:
                player.health += 1