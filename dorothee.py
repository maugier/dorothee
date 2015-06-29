#!/usr/bin/env python3

import random
import re
from irc.bot import SingleServerIRCBot

chansons = [
    "ALLEZ LES BLEUS, ON EST TOUS ENSEEEEEMBLE",
    "AH QUE LE MONDE EST PETIT, AH QUE LE MONDE EST PETIT",
    "BISOOUUU BISOOUUU, GENTIL BISOUNOURS",
    "HEEEEY MACARENA",
    "IT'S FRIDAY FRIDAY",
    "IT'S THE FINAL COUUUNTDOOOWN",
    "I'M BLUUUE, DA BA DEE DA BA DAAA",
    "I'M THE SCAAATMAAAN - SKIBIDIBIDIBELELEBELDELOPDOP",
    "LA LA LA SCHTROUMPF LA LA",
    "LE PAPA PINGOUIN, LE PAPA PINGOUIN",
    "LE PETIT BONHOMME EN MOUUUSEUH",
    "JE SUIS SANS FAMIIIIILEUUH, JE M'APPELLE REMIIIII",
    "NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN",
    "NUMA NUMA IEI, NUMA NUMA IEI, NUMA NUMA NUMA IEI",
    "OOOOOOOOOH, BABOOSCHKA BABOOSCHKA",
    "PAPILLON DE LUMIEREUH",
    "SCHNII SCHNAA SCHNAPPY, SCHNAPPY SCHNAPPY SCHNAP",
    "THIS IS THE CRAZY FROG"
]

game_re = re.compile('g+[a@]+m+[e3]+|j+e+u+', re.I)

class Dorothee(SingleServerIRCBot):
    def __init__(self, servers, nick, real, channel, **kw):
        self.channel = channel
        super().__init__(servers, nick, real, **kw)

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        msg = e.arguments[0]
        if game_re.search(msg):
            c.privmsg(e.target, random.choice(chansons))
            
