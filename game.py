import random

class Player:
        classes = ["healer", "tank", "swordsmaster", "wizard"]
        players = []

        def __init__(self, name, character_class="swordsmaster"):
                if name not in Player.players:
                        self.name = name
                else: 
                        print("the name already exists, you will be assigned an auto generated name")
                        print(f"your name is now: {id(self)}")
                        self.name = id(self)

                self.character_class = character_class.lower()
                if character_class == "healer":
                        self.health = 800
                        self.max_health = 800
                        self.strength = 50
                        self.defense = 55
                        self.max_mana = 200
                        self.mana = 200
                elif character_class == "tank":
                        self.health = 200
                        self.max_health = 200
                        self.strength = 180
                        self.defense = 250
                        self.max_mana = 120
                        self.mana = 120
                elif character_class == "swordsmaster":
                        self.health = 250
                        self.max_health = 250
                        self.strength = 400
                        self.defense = 100
                        self.energy = 0
                elif character_class == "wizard":
                        self.health = 100
                        self.max_health = 100
                        self.strength = 250
                        self.defense = 75
                        self.max_mana = 200
                        self.mana = 200
                elif character_class not in Player.classes:
                        print(f"the chosen class does not exist, so by default, you, {self.name} will be a swordsmaster!")
                        self.character_class = "swordsmaster"
                        self.health = 250
                        self.max_health = 250
                        self.strength = 400
                        self.defense = 100
                        self.energy = 0
                Player.players.append(self)
        
        def replenish():
                for player in Player.players:
                        if player.character_class == "healer" or player.character_class == "wizard":
                                if player.mana < player.max_mana:
                                        player.mana += 25
                                        if player.mana > player.max_mana : player.mana = player.max_mana
                        elif player.character_class == "swordsmaster":
                                if player.energy < 100:
                                        player.energy += 15
                                        if player.energy > 100 : player.energy = 100

        def show(self):
                print(f"Hello adventurer {self.name}!")
                print(f"you have chosen the path of the {self.character_class}, and your current stats are as follows:")
                print(f"    health: {self.health}/{self.max_health}")
                print(f"    strength: {self.strength}")
                print(f"    defense: {self.defense}")
                if self.character_class == "wizard" or self.character_class == "healer" or self.character_class == "tank":
                        print(f"    mana: {self.mana}/{self.max_mana}")
                elif self.character_class == "swordsmaster":
                        print(f"    energy: {self.energy}/100")
        #mana and energy gets replenished a bit at every turn of every player for all players

        #########################################################################  MOVES  ##########################################################################################
        def attack(self, foe):   #everyone can attack
                if foe.health > 0 and self != foe and self.health > 0:
                        dmg = (self.strength*random.random()*10) // (2*foe.defense*0.3)
                        foe.health -= dmg
                        print(f"{self.name} attacked {foe.name}!!! they dealt {dmg}!!")
                elif foe.health <= 0:
                        print(f"{foe.name} is already dead!")
                elif self == foe:
                        print(f"unfortunately, you cannot commit self harm or suicide here, {self.name}")    
                Player.replenish()
                
        def heal(self, ally):    #healers class only, the healing amount is random and scales off healer's max health, gets a healing bonus according to her current hp, costs mana
                if self.character_class == "healer" and self.health > 0:
                        if ally.max_health > ally.health and ally.health > 0:
                                healed_hp = ((self.max_health*0.2*random.random()*10) + self.health*0.5 )* random.random()
                                ally.health += healed_hp
                                if ally.health > ally.max_health: ally.health = ally.max_health
                                print(f"{self.name} healed {ally.name}!!! they replenished {healed_hp} hp!!")
                        elif ally.health <= 0:
                                print(f"good or bad news first?\nwell the good news is that you are still alive! what an amazing player you are {self.name}.\noh and bad news is that your buddy {ally.name} is finito...\nlast time I checked you were just a healer not god so...")
                else: print(f"{self.name}, your class is {self.character_class}, this move is a healer only move, you cannot perform 'heal'")

                Player.replenish()
        
        def buff(self, ally):    #healers and wizards can buff, healers buff max health and defense, and wizards can buff strength, costs mana
                if self.character_class == "healer" and ally.health > 0 and self.health > 0:
                        ally.max_health += self.health * 0.02 * random.random() * 2
                        ally.defense += self.health * 0.015 * random.random() * 2
                        if self.mana > 0 and self.mana >= 100:
                                self.mana -= 100
                        print(f"{self.name} buffed {ally.name}'s max hp and defense!")
                elif self.character_class == "wizard" and ally.health > 0 and self.health > 0:
                        ally.strength += self.strength * 0.07 * random.random() * 2
                        if self.mana > 0 and self.mana >= 60:
                                self.mana -= 60
                        print(f"{self.name} buffed {ally.name}'s strength!")
                elif ally.health <= 0: print(f"{ally.name} is already dead!")
                else: print(f"{self.name}, your class is {self.character_class}, this move is a healer and wizard only move, you cannot perform 'buff'")
                
                Player.replenish()
        
        def debuff(self, foe):   #wizards can debuff foe strength, tanks can debuff foes defense, costs mana
                if self.character_class == "wizard" and foe.health > 0 and self.health > 0:
                        foe.strength -= self.strength * 0.05 * random.random() * 2
                        if self.mana > 0 and self.mana >= 60:
                                self.mana -= 60
                        print(f"{self.name} debuffed {foe.name}'s strength!")
                elif self.character_class == "tank" and foe.health > 0 and self.health > 0:
                        foe.defense -= self.defense * 0.1 * random.random() * 2
                        if self.mana > 0 and self.mana >= 70:
                                self.mana -= 70
                        print(f"{self.name} debuffed {foe.name}'s defense!")
                elif foe.health <= 0: print(f"{foe.name} is already dead!")
                else: print(f"{self.name}, your class is {self.character_class}, this move is a wizard and tank only move, you cannot perform 'debuff'")
                
                Player.replenish()
        
        def shield(self, ally):  #tanks class only: creates a shield scaled off the defense of the caster
                if self.character_class == "tank" and ally.health > 0 and self.health > 0:
                        ally.health += self.defense*0.15* random.random() * 2
                        if self.mana > 0 and self.mana >= 100:
                                self.mana -= 100
                        print(f"{self.name} shielded and healed up {ally.name}!")
                elif ally.health <= 0 : print(f"{ally.name} is already dead!")
                else: print(f"{self.name}, your class is {self.character_class}, this move is a tank only move, you cannot perform 'shield'")
                
                Player.replenish()
        
        def ultimate(self, foes): #swordsmaster class only: does great damage on at most 3 random foes, costs energy
                if self.character_class == "swordsmaster" and self.energy >= 80 and self.health > 0:
                        if len(foes) > 3:
                                for i in range (3):
                                        if foes[i].health > 0:
                                                dmg = (self.strength*random.random()*50) // (foes[i].defense*0.3)
                                                foes[i].health -= dmg
                                                print(f"{self.name} dealt great damage on {foes[i].name}!! they recieved {dmg}")
                                        else: print(f"{foe.name} is already dead!")
                        else: 
                                for foe in foes:
                                        if foe.health > 0:
                                                dmg = (self.strength*random.random()*50) // (foe.defense*0.3)
                                                foe.health -= dmg
                                                print(f"{self.name} dealt great damage on {foe.name}!! they recieved {dmg}")
                                        else: print(f"{foe.name} is already dead!")
                        self.energy -= 80                        

                else: print(f"{self.name}, your class is {self.character_class}, this move is a swordsmaster only move, you cannot perform 'shield'")
                
                Player.replenish()
