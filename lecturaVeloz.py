#!/usr/bin/env python3

from time import sleep
from termcolor import colored
import sys
import os


def openTxt(txt):
    with open(txt, 'r', encoding="utf-8") as t:
        text = t.read().split()
        return text


def displayWords(txt, wpm):

    space = ' '
    delay = round((60 / wpm), 2)

    for word in txt:

        print(f'\n{space*20}{colored(word, "green")}', end='\r')
        # print(end='\x1b[2K')

        sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')


txt = openTxt(sys.argv[1])

displayWords(txt, int(sys.argv[2]))
