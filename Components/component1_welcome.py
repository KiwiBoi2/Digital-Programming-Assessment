#import random lib for name randomiser
from random import randint
#name library for random name picker
names = ["Olivia","James","Charlotte","Ethan","Amelia","Liam","Sophie","Benjamin","Isla","Noah","Emily","Lucas","Ava","Oliver","Grace"]

#welcome function
def welcome():
    #Welcome banner for shop
    banner = """ _____                                                                                                  _____ 
( ___ )------------------------------------------------------------------------------------------------( ___ )
 |   |                                                                                                  |   | 
 |   |   ██████  ██░ ██  ▄▄▄       ██▀███   ██▓███     ▄▄▄█████▓ ██░ ██  ██▓ ███▄    █   ▄████  ██████  |   | 
 |   | ▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒██    ▒  |   | 
 |   | ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▓██░ ██▓▒   ▒ ▓██░ ▒░▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░ ▓██▄    |   | 
 |   |   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▄█▓▒ ▒   ░ ▓██▓ ░ ░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓ ▒   ██▒ |   | 
 |   | ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██▒ ░  ░     ▒██▒ ░ ░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒██████▒▒ |   | 
 |   | ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▓▒░ ░  ░     ▒ ░░    ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒▒ ▒▓▒ ▒ ░ |   | 
 |   | ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░▒ ░            ░     ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░░ ░▒  ░ ░ |   | 
 |   | ░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░ ░░            ░       ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░░  ░  ░   |   | 
 |   |       ░   ░  ░  ░      ░  ░   ░                           ░  ░  ░ ░           ░       ░      ░   |   | 
 |___|                                                                                                  |___| 
(_____)------------------------------------------------------------------------------------------------(_____)
"""
    #name randomiser
    num = randint(0,14)
    botname = names[num]
    #print welcome message
    print(banner)
    print(f"\nWelcome to Sharp Things, my name is", botname)
    print("I shall be assisting you in selecting and purchasing your blade\n")

welcome()
