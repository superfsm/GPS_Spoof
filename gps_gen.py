#!/usr/bin/env python

import xml.etree.cElementTree as ET
import curses
import time,sys
import random

stdscr = curses.initscr()

def pprint(*args):
    for arg in args:
        stdscr.addstr(str(arg) + ' ')
    stdscr.addstr('\n')

def gen(keyPressed):

    STEP = 0.0001

    root = ET.parse("pokemonLocation.gpx").getroot()
    lat  = float(root[0].attrib['lat'])
    lon  = float(root[0].attrib['lon'])

    if keyPressed == 259: #up
        lat += STEP
    elif keyPressed == 258:   #down
        lat -= STEP
    elif keyPressed == 260:   #left
        lon -= STEP
    elif keyPressed == 261:   #right
        lon += STEP

    gpx = ET.Element("gpx", version="1.1", creator="Xcode")
    wpt = ET.SubElement(gpx, "wpt", lat=str(lat), lon=str(lon))
    ET.SubElement(wpt, "name").text = "PokemonLocation"
    ET.ElementTree(gpx).write("pokemonLocation.gpx")
    try:
        pprint (keyPressed, "latitude:", lat, "longitude:" ,lon)
    except:
        pass

def main():
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    while True:
        keyPressed = stdscr.getch()
        if keyPressed == ord('s'):
            break
        gen(keyPressed)

    curses.endwin()


if __name__ == "__main__":
    main()