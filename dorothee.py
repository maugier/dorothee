#!/usr/bin/env python3

import random
import rate
import re
import time
from irc.bot import SingleServerIRCBot

chansons = [
    "ALLEZ LES BLEUS, ON EST TOUS ENSEEEEEMBLE",
    "AH QUE LE MONDE EST PETIT, AH QUE LE MONDE EST PETIT",
    "BISOOUUU BISOOUUU, GENTIL BISOUNOURS",
    "BIG BISOUUU ! BIG BISOUUU !",
    "C'EST LA DANSE DES CANARDS",
    "CHAUD CHAUD CHAUD, CACAO",
    "HEEEEY MACARENA",
    "HEY I JUST MET YOU, AND THIS IS CRAZY",
    "IT'S FRIDAY FRIDAY",
    "IT'S THE FINAL COUUUNTDOOOWN",
    "I'M BLUUUE, DA BA DEE DA BA DAAA",
    "I'M THE SCAAATMAAAN - SKIBIDIBIDIBELELEBELDELOPDOP",
    "LA LA LA SCHTROUMPF LA LA",
    "LE PAPA PINGOUIN, LE PAPA PINGOUIN",
    "LE PETIT BONHOMME EN MOUUUSEUH",
    "JE SUIS SANS FAMIIIIILEUUH, JE M'APPELLE REMIIIII",
    "JESUS REVIENT, JESUS REVIENT",
    "NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN",
    "NUMA NUMA IEI, NUMA NUMA IEI, NUMA NUMA NUMA IEI",
    "OOOOOOOOOH, BABOOSCHKA BABOOSCHKA",
    "OHÉ, OHÉ, CAPITAINE ABANDONNNÉÉÉÉ",
    "OUTAI, PAPAOUTAI, OUTÉ PAPAOUTAIII",
    "PAPILLON DE LUMIEREUH",
    "PAPAYOUUU, PAPAYOUUUUU; PAPAYOU, PAPAYOU-LÉLÉ",
    "SCHNII SCHNAA SCHNAPPY, SCHNAPPY SCHNAPPY SCHNAP",
    "TIRELIPIMPON SUR LE CHIHUAHUA",
    "THIS IS THE CRAZY FROG",
    "UN PEU PLUS PRÈS DES ÉTOIIIIILES",
    "VIENS, JE T'EMMEEEENE SUR MON BAAATEAU BLANC",
    "VOIS SUR TON CHEMIN, GAMINS OUBLIÉS EGARÉS"
]

game_re = re.compile('g+[a@]+m+[e3]+|j+e+u+|p+e+r+d+(r+e+|e+z+|u+)', re.I)

class Dorothee(SingleServerIRCBot):
    def __init__(self, servers, nick, real, channel, grace=3600, **kw):
        self.channel = channel
        self.rate = rate.RateLimiter(grace)
        super().__init__(servers, nick, real, **kw)

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        msg = e.arguments[0]
        if game_re.search(msg):
            if not self.rate(e.target):
                c.privmsg(e.target, "♬ {0} ♬".format(random.choice(chansons)))
            
