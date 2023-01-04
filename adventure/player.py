import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 50
        self.alive = True
        self.inventoryWeight = 0
        self.stopTheGame = False
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)  
    def pickup(self, item):
        if self.inventoryWeight + item.weight <= 30:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            self.inventoryWeight += item.weight
        else:
            print("overseer: aw, grimtern dearest, you're far too materialistic... your inventory's over the weight limit. drop something or let it go, honey.")
            print()
            input("Press enter to continue...")
    def showInventory(self):
        # item stacking
        count = 0
        while count < len(self.items):
            toAddTo = []
            toDelete = []
            tallyList = []
            tally = 1
            count1 = 0
            
            while count1 < len(self.items):
                if self.items[count].name == self.items[count1].name and count != count1:
                    toAddTo.append(count)
                    toDelete.append(count1)
                    tally += 1
                count1 += 1
            
            if tally > 1:
                tallyList.append(tally)
            
            count += 1

        count = 0
        if len(toAddTo) > 0:
            while count < len(toAddTo):
                self.items[toAddTo[count]].name += " (x" + str(tallyList[count]) + ")"
                del self.items[toDelete[count]]
                for i in toDelete:
                    i -= 1
                for i in toAddTo:
                    i -= 1
                count += 1
        clear()
        print("ur stuff rn:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def me(self):
        clear()
        print("overseer: oh? so you were curious about your stats. lol fine, here u go:")
        print()
        print("ur health: " + str(self.health))
        input("Press enter to continue...")  
    def attackMonster(self, mon):
        clear()
        print("overseer: let's kick " + mon.name + "'s butt.")
        print()
        
        message = "overseer: oh, and ur health rn is " + str(self.health) + "."
        scytheDamage = 10
        sickleDamage = 5
        armorPoints = 0
        toHurtOrNotToHurt = False
        sickleExists = False
        scytheExists = False
        ultArmorExists = False

        for i in self.items:
            if i.name == "sickle":
                sickleExists = True
            if i.name == "DOOM SCYTHE":
                scytheExists = True
            if i.name == "ULTIMATE ARMOR":
                ultArmorExists = True
            if i.name == "edgy black cloak":
                armorPoints = 5

        if sickleExists and scytheExists:
            attackDamage = scytheDamage
            message += " you also have a very sexy " + str(scytheDamage) + " attack points."
            toHurtOrNotToHurt = True
        elif sickleExists:
            attackDamage = sickleDamage
            message += " you also have a sexy " + str(sickleDamage) + " attack points."
            toHurtOrNotToHurt = True
        elif scytheExists:
            attackDamage = scytheDamage
            message += " you also have a sexy " + str(scytheDamage) + " attack points."
            toHurtOrNotToHurt = True
            
        print(message)
        print("overseer: and " + mon.name + "'s health is " + str(mon.health) + " rn.")
        print()

        if toHurtOrNotToHurt:
            if self.health + attackDamage + armorPoints >= mon.health:
                self.health = self.health - mon.health + attackDamage + armorPoints
                print("overseer: VICTORYYYYYY!!!! *ahem* i mean, good job ig intern. ur health is " + str(self.health) + " rn.")
                mon.die()
            else:
                if ultArmorExists:
                    print("overseer: you were about to die???? but smelly armor comes to save the day <3. i call hacks.")
                else:
                    print("overseer: you lost lollllllllll.")
                    self.alive = False

        elif not toHurtOrNotToHurt:
            if self.health + armorPoints >= mon.health:
                self.health = self.health - mon.health + armorPoints
                print("overseer: VICTORYYYYYY!!!! *ahem* i mean, good job ig intern. ur health is " + str(self.health) + " rn.")
                mon.die()
            else:
                if ultArmorExists:
                    print("overseer: you were about to die???? but smelly armor comes to save the day <3. i call hacks.")
                else:
                    print("overseer: you lost lollllllllll.")
                    self.alive = False
        print()
        input("Press enter to continue...")  
    def heal(self, item):
        if item == "bandaid":
            self.health += 9
    def chatUp(self, NPC):
        if NPC == "THE GRIM REAPER":
            soulTally = 0
            for i in self.items:
                if i.name == "stray kitty's soul" or i.name == "birdy's soul" or i.name == "opossum's soul" or i.name == "fido's soul" or i.name == "inpatient's soul":
                    soulTally += 1
            
            print("THE GRIM REAPER: i hear you wanted a promotion, small grimtern?")
            print("a. yes!")
            print("b. i don't think i'm ready for that yet, sir...")
            choice = input("WHAT IS YOUR RESPONSE? (a/b): ")
            
            if choice == "a":
                print()
                if soulTally == 5:
                    print("THE GRIM REAPER: well, i think you've earned it, haven't you? grimtern, you've worked on your skillset so much. YOU'RE HIRED :D")
                    print()
                    victory = input("YOU HAVE COMPLETED THE GAME. WOULD YOU LIKE TO END THE GAME OR CONTINUE? (end/continue): ")
                    if victory == "continue":
                        clear()
                    elif victory == "end":
                        self.stopTheGame = True
                        return self.stopTheGame
                else:
                    print("THE GRIM REAPER: it seems like you need to find more souls, grimterm.")
                    input("Press enter to continue...")
            elif choice == "b":
                print("THE GRIM REAPER: wow, what dedication to your craft. i will await your development, grimtern.")
                input("Press enter to continue...")
            else:
                print("overseer: be real rn. it's literally just end or continue.")
