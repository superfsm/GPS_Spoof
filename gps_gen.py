#!/usr/bin/env python

import xml.etree.cElementTree as ET
import curses
import time,sys

# def generateXML():
# 	global lastLat, lastLng
# 	geo = getPokemonLocation()
# 	if geo != None:
# 		if geo["lat"] != lastLat or geo["lng"] != lastLng:
# 			lastLat = geo["lat"]
# 			lastLng = geo["lng"]
# 			gpx = ET.Element("gpx", version="1.1", creator="Xcode")
# 			wpt = ET.SubElement(gpx, "wpt", lat=geo["lat"], lon=geo["lng"])
# 			ET.SubElement(wpt, "name").text = "PokemonLocation"
# 			ET.ElementTree(gpx).write("pokemonLocation.gpx")
# 			print "Location Updated!", "latitude:", geo["lat"], "longitude:" ,geo["lng"]

def main():

	win = curses.initscr()
	curses.cbreak()

	while True:
		print '>'
	    keyPress = win.getch()
	    #if key != -1:
	    print sys.stdout.write('*'+str(keyPress)+'*\n')


if __name__ == "__main__":
	main()