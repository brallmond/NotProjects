import random as random
import numpy as np
import pprint as pp
import sys
from termcolor import colored
from time import sleep
# [1A moves up one line, [2K clears the line
# print() always tacks on a new line, so if you use any escape characters to erase a line, you have to add [1A or [2A on the end to ensure you end on the line above
# [J clears from current line to the bottom of the screen
print_delay = 0.35 

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)

class baseballcard:

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
                'q','r','s','t','u','v','w','x','y','z'] 
    sep = ''

    display = []

    # generate name and base stats. overwritten if args given
    def __init__(self,
            name = '',
            base_health = 0,
            base_damage = 0,
            base_speed = 0):

        if name == '' or base_health == 0 or base_damage == 0 or base_speed == 0:
            name = ''.join(random.sample(baseballcard.alphabet, 5))
            base_health = random.randint(20, 30)
            base_damage = random.randint(5, 10)
            base_speed = random.randint(1, 5)

        elif name == 'Hard':
            name = 'Devil'
            base_health = 100
            base_damage = 40
            base_speed = 20

        self.name = name.capitalize()
        self.base_health = base_health
        self.health = base_health
        self.base_damage = base_damage
        self.base_speed = base_speed

    def update_display_append(self, info = []):
        display = baseballcard.display
        add_length = len(info)
        for i in range(add_length):
            display.append(info[i])

    def update_display_element(self, update, name = None, index = None):
        display = baseballcard.display
        if (len(display) > 0) & (index == None):
            match_index = [i for i, item in enumerate(display) if name in item]
            display[match_index[0]] = update
        elif index != None:
            display[index] = update
        else: pass

    def print_display(self, add_time = 0, STAY = False):
        display = baseballcard.display
        length = len(display)
        for i in range(length):
            print(display[i])
        sleep(print_delay + add_time)
        if STAY: #don't erase
            pass
        else:
            num = str(length)
            print('\x1b[' + num + 'A' + '\x1b[J\x1b[1A')

    def healthbar(self, add = 0, no_print = False):
        bar = colored('#'*self.health, 'red')
        nonbar = colored('#'*(self.base_health-self.health), 'grey')
        info = colored("{} ({}/{}): ".format(self.name, self.health, self.base_health), 'blue')
        healthbar = info + bar + nonbar
        if (add == 0) & (not no_print):
            self.update_display_element(healthbar, name = self.name)
            self.print_display()
        elif abs(add) > 0:
            sign = np.sign(add)
            while True:
                if add == 0 or self.health == 0:
                    self.healthbar()
                    break
                else:
                    self.healthbar()
                    self.health += sign
                add += -1*sign
        elif no_print:
            return healthbar
        else: pass

    def list_stats(self):
        border = colored("---------------", 'yellow')
        text_healthbar = self.healthbar(no_print = True)
        text_damage = "Base Damage: " + str(self.base_damage)
        text_speed = "Base Speed: " + str(self.base_speed)
        self.update_display_append([border, text_healthbar, text_damage, text_speed, border])
        self.print_display()

    def action(self, text):
        display = baseballcard.display
        border = colored(((len(text)+1)/2)*'- ', 'grey')
        piece = colored('Action ', 'red')
        first = piece + border
        match_index = [i for i, item in enumerate(display) if piece in item]
        if len(match_index) == 0:
            self.update_display_append([first, text, border])
        else:
            index = match_index[0] + 1
            self.update_display_element(text, index = index)

    def attack(self, opp):
        if self.health > 0 and opp.health > 0:
            attack_text = "{} attacks for {} damage".format(self.name, self.base_damage)
            self.action(attack_text)
            opp.healthbar(-self.base_damage)
            if opp.health > 0:
                pass
            else:
                opp.health = 0
                self.healthbar()
                opp.healthbar()
                win_text = "{} took fatal damage. {} wins!".format(opp.name, self.name)
                self.action(win_text)
                self.print_display(STAY = True)
        else: pass

    def first_strike(self, opp):
        if self.base_speed > opp.base_speed:
            first = self
            not_first = opp
        else:
            first = opp
            not_first = self
        strike_text = "{} attacks first".format(first.name)
        self.action(strike_text)
        self.print_display(add_time = 0.5)
        return first, not_first

    def versus(self, opp): #self vs opponent
        self.list_stats()
        opp.list_stats()
        first, not_first = self.first_strike(opp)
        while (self.health > 0 and opp.health > 0):
            first.attack(not_first)
            not_first.attack(first)

        if self.health == 0:
            winner = False
        else:
            winner = True

        return winner


# make two rands and vs them
def twofer(name = '', base_health = 0, base_damage = 0, base_speed = 0):
    if name != '':
        one = baseballcard(name, base_health, base_damage, base_speed)
        two = baseballcard()
    else:
        one = baseballcard()
        two = baseballcard()
    one.versus(two)

def tourney():
    i = 0
    while True:
        print(i)
        i += 1
        twofer()

if __name__ == "__main__":
        #record and overwrite last log file
        f = open('logfile', 'a')
        backup = sys.stdout
        sys.stdout = Tee(sys.stdout, f)

        #parse future input
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--phrase', '-p', required=True, action='store', help='Say something and I\'ll say it back!')
       
        tourney()
