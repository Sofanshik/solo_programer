from termcolor import colored
import random

class Hero(object):
    mana = 100
    hp = 100
    strength = 10
    agility = 10
    intelligence = 10
    speed = 320


    def lose_hp(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(colored("Game Over", 'green'))
        return self.hp

    def lose_mana(self, mana):
        self.mana -= mana


    def attack(self, creep):
        if hasattr(self, "weapon"):
            damage = random.randint(self.weapon.minimal_damage, self.weapon.maximal_damage)
            if damage == self.weapon.maximal_damage:
                damage *= 1.5
            creep_hp = creep.lose_hp(damage)
            print(colored("It's a damage which take your hero - " + str(damage) + ".", 'blue'))
            if creep_hp <= 0:
                print(colored("Creep's Dead", 'yellow'))
        else:
            print("Error, self didn't have this atribute!")



class Creep(object):
    strength = 7
    agility = 7

    def __init__(self, hp):
        self.hp = hp
        self.attack_speed = self.agility / 2.5

    def lose_hp(self, damage):
        self.hp -= damage
        return self.hp

    def attack(self, hero):
        min_damage = self.strength * 2
        max_damage = self.strength * 3
        damage = random.randint(min_damage, max_damage)
        hero.lose_hp(damage)
        print(colored("It's a damage which take your creep - " + str(damage) + ".", 'red'))


class Magic(object):
        mana_cost = 10

        def __init__(self):
            self.mana_cost *= self.power
            self.damage = self.power * 5

class Ice(Magic):
    power = 3

    def __str__(self):
        return "Ice spell, with damage:{}, mana cost: {}".format(self.damage, self.mana_cost)

class Fire(Magic):
    power = 4

    def __str__(self):
        return "Fire spell, with damage:{}, mana cost: {}".format(self.damage, self.mana_cost)

class Arcane(Magic):
    power = 5

    def __str__(self):
        return "Arcane spell, with damage:{}, mana cost: {}".format(self.damage, self.mana_cost)

class Weapon(object):

    def __init__(self, strength, agility):
        self.minimal_damage = (strength + agility) / 2.5
        self.maximal_damage = strength + agility
        self.attack_speed = agility / 3.5


class Warrior(Hero):

    def __init__(self):
        self.strength = self.strength * 1.5
        self.hp = self.hp * (self.strength / 12)
        self.weapon = Weapon(self.strength, self.agility)
        self.attack_speed = self.agility / 2.5
        self.spells = {"Fire":Fire()}

class Archer(Hero):

    def __init__(self):
        self.agility = self.agility * 1.5
        self.weapon = Weapon(self.strength, self.agility)
        self.attack_speed = self.agility / 2
        self.spells = {"Ice":Ice()}

class Mage(Hero):
    def __init__(self):
        self.intelliegence = self.intelligence * 1.5
        self.mana = self.mana * (self.intelligence / 10)
        self.weapon = Weapon(self.strength, self.agility)
        self.attack_speed = self.agility / 2.5
        self.spells = {"Fire":Fire(), "Ice":Ice(), "Arcane":Arcane()}


class Battle(object):
    def __init__(self, hero):
        self.creep = Creep(random.randint(50, 60))
        self.hero = hero

    def fight(self):
        while self.hero.hp > 0 and self.creep.hp > 0:
            method_attack = input("Chose method attack - Weapon or Magic spell: ")
            print(method_attack)
            if method_attack == "Weapon":
                if self.hero.attack_speed > 0:
                    self.hero.attack(self.creep)
                    print(colored("Your hero have " + str(self.hero.hp) + "hp!", 'red'))

            if method_attack == "Magic":
                print("Your hero have that spells: {}".format(self.hero.spells.keys()))
                select_skill = input("Select skill your hero: ")
                if select_skill in self.hero.spells.keys():
                    spell = self.hero.spells.get(select_skill)

                    if self.hero.mana > spell.mana_cost:
                        self.creep.hp = self.creep.lose_hp(spell.damage)
                        self.hero.lose_mana(spell.mana_cost)
                        print(colored("Your hero have " + str(self.hero.hp) + "hp and " + str(self.hero.mana) + " mana!", 'red'))
                    else:
                        self.hero.attack(self.creep)

                else:
                    while select_skill not in self.hero.spells.keys():
                        select_skill = input("Error, try again! {}".format(self.hero.spells.keys()) + colored("Select skill your hero: ", 'blue'))
                        print(select_skill)

                        if select_skill in self.hero.spells.keys():
                            spell = self.hero.spells.get(select_skill)

                            if self.hero.mana > spell.mana_cost:
                                self.creep.hp = self.creep.lose_hp(spell.damage)
                                self.hero.lose_mana(spell.mana_cost)
                                print(colored(
                                    "Your hero have " + str(self.hero.hp) + "hp and " + str(self.hero.mana) + " mana!", 'red'))
                            else:
                                self.hero.attack(self.creep)

            if self.creep.attack_speed > 0:
                self.creep.attack(self.hero)
                print(colored("Creep have " + str(self.creep.hp) + "hp!", 'blue'))


class WarOfHeroes(object):
    heroes = {"Warrior":Warrior(), "Archer":Archer(), "Mage":Mage()}

    def run(self):
        print(colored("Game Started", 'cyan'))
        heroe = input("Chose hero! Warrior, Archer or Mage: ")
        if heroe in self.heroes.keys():
            if heroe == "Warrior" or heroe == "Archer" or heroe == "Mage":
                battle = Battle(self.heroes.get(heroe))


        else:
            while heroe not in self.heroes:
                heroe = input("Try choose again: ")
                print(heroe)
                if heroe == "Warrior" or heroe == "Archer" or heroe == "Mage":
                    battle = Battle(self.heroes.get(heroe))


        print(colored(heroe, 'green'))
        if hasattr(battle, "fight"):
            battle.fight()
        print(colored("Game end", 'magenta'))


war_of_hero = WarOfHeroes()
war_of_hero.run()
