import sys
from textwrap import dedent
import subprocess as sp
import os
from pydub import AudioSegment
# custom function to suppress output while playing music
from pydub.playback_suppress import play


class Map(object):
    """docstring for Map."""
    def __init__(self, arg):
        super(Map, self).__init__()
        self.room = arg
        self.color = "Blue"

    #returns the roomname to be passed into the dictionary
    def enter_room(self):
        return self.room


    def initialize():
        pass


class Room(object):
    """docstring for Room."""
    def __init__(self):
        super(Room, self).__init__()
        # self.whatever = arg
        self.connector = "default"
        self.villain = "Snagglepuss"
        self.roomname = "Rabbit_Hole"


    def announce(self):
        print(f"You have entered the {self.roomname} room with the deadly {self.villain}")


class Evil_Wizard(Room):
    """Description of room with the Evil Wizard"""
    def __init__(self, arg):
        super(Evil_Wizard, self).__init__()
        self.villain = arg
        self.answer = "Avada Kedavra"
        self.bypass = "Mayweather"
        self.connector = "Barbarian"
        self.roomname = "Mordorous"
        os.system('clear')
        self.ten_seconds = 3 * 1000
        #changed to 3 seconds temporarily
        self.song = AudioSegment.from_mp3("Hypnotize.mp3")
        self.first_10_seconds = self.song[:self.ten_seconds]
        os.system('clear')
        print(f"You have entered the {self.roomname} room with the deadly {self.villain}")


    def enter(self):

        print(dedent("""\n\n\t\tSTORYLINE\t\n\nOne does not simply walk into Mordor. Its black gates are guarded by more than
just Orcs.There is evil there that does not sleep. The great Eye is ever watchful.
It is a barren wasteland, riddled with fire, ash, and dust. The very air you
breathe is a poisonous fume.


****Oblor the Evil Wizard is going to obliterate you
Type in the secret spell to banish him ****)"""))

        #playing the song intro
        play(self.first_10_seconds)

        self.user_answer = input("Enter the magic word! NOW!")

        #checking to see if the user's answer matches the word
        if self.user_answer == self.answer:
            print(f"""You have defeated {self.villain} with you magical powers!!
            {self.villain} has been sucked into a dark hole!
            Now beware of the {self.connector} """)
            return self.connector

        #creating a backdoor to go straight to the main boxx
        elif self.user_answer == self.bypass:
            return("boss")


        else:
            print(f"""You have been obliterated and annihiled by {self.villain}. Die fool!""")
            exit(0)










class Barbarian(Room):
    """docstring for Barbarian."""
    def __init__(self, arg):
        super(Barbarian, self).__init__()
        self.villain = arg
        self.connector = "Queen_Of_Darkness"
        os.system('clear')
        print(f"You have entered the {self.roomname} room with the deadly {self.villain}")







class Queen_Of_Darkness(object):
    """Description of room with the Queen of Darkness"""
    def __init__(self, arg):
        from random import randint
        super(Queen_Of_Darkness, self).__init__()
        self.villain = arg
        self.answer = randint(1, 5)
        self.bypass = "Mayweather"
        self.connector = "Barbarian"
        self.roomname = "Darkness"
        os.system('clear')
        self.five_seconds = 5 * 1000
        #changed to 3 seconds temporarily
        self.song = AudioSegment.from_mp3("Gasolina.mp3")
        self.first_5_seconds = self.song[:self.five_seconds]
        os.system('clear')
        print(f"You have entered the {self.roomname} room with the deadly {self.villain}")


    def enter(self):
        #Storyline starts here

        print(dedent("""\n\n\t\tSTORYLINE\t\n\nI AM {self.villain} - THE QUEEN OF DARKNESS!!!
        You will fear my wrath you wretched mortal.

        ***{self.villain} SHOOTS LIGHTING AT YOU****

        ***YOU HIDE UNDER A TABLE AND FEEL THE SINGE OF LIGHTING GRAZE YOUR HAIR***

        ***You then notice a small control box in the corner asking you to enter a number****

        *** A NUMBER BETWEEN 1 to 5 ***

        WHAT WILL IT BE HUMAN?!

Type in the secret number to enter in the control panel ****)"""))

        #playing the song intro
        play(self.first_5_seconds)

        self.user_answer = input("Enter the magic word! NOW!    :")

        #checking to see if the user's answer matches the word
        if int(self.user_answer) == int(self.answer):
            print(f"""You have defeated {self.villain} with you magical powers!!
                        {self.villain} has been chopped to pieces with a guillotine from the ceiling!
                        Now beware of the {self.connector} """)
            return self.connector

        #creating a backdoor to go straight to the main boxx
        elif self.user_answer == self.bypass:
            return("boss")


        else:
            print(f"""You have been electrocuted by {self.villain}. Die fool! You should have typed in {self.answer}""")
            exit(0)








class Engine(object):
    """docstring for Engine."""
    def __init__(self, arg):
        super(Engine, self).__init__()
        self.arg = arg

        #creating dictionary
        scenes = {'Evil Wizard': enter(),
                'Barbarian': enter(),
                'Queen Of Darkness': enter(),
                'Rabbit Hole': enter()
                }


if __name__ == '__main__':

    obj = Queen_Of_Darkness("D'LIVIA")
    obj.enter()
