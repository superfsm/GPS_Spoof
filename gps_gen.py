#!/usr/bin/env python

import xml.etree.cElementTree as ET
import curses
import time,sys
import random

stdscr = curses.initscr()

def pprint(*args):
    stdscr.erase()
    for arg in args:
        stdscr.addstr(str(arg) + ' ')
    stdscr.addstr('\n')

def gen(keyPressed):

    STEP = 0.0001

    root = ET.parse("pokemonLocation.gpx").getroot()
    lat  = float(root[0].attrib['lat'])
    lon  = float(root[0].attrib['lon'])

    if keyPressed == 'KEY_UP':
        lat += STEP
    elif keyPressed == 'KEY_DOWN':
        lat -= STEP
    elif keyPressed == 'KEY_LEFT':
        lon -= STEP
    elif keyPressed == 'KEY_RIGHT':
        lon += STEP

    gpx = ET.Element("gpx", version="1.1", creator="Xcode")
    wpt = ET.SubElement(gpx, "wpt", lat=str(lat), lon=str(lon))
    ET.SubElement(wpt, "name").text = "PokemonLocation"
    ET.ElementTree(gpx).write("pokemonLocation.gpx")
    try:
        pprint ('{:9s}'.format(keyPressed), "latitude:", lat, "longitude:" ,lon)
    except:
        pass

def main():
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    while True:
        keyPressed = stdscr.getkey()
        if keyPressed == 's':
            break
        gen(keyPressed)

    curses.endwin()


if __name__ == "__main__":
    main()