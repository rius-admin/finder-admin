#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Script by DarkVairous
#Editor recode Mr.Rius
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

print "===================================================================== "
print "                _                                        "
print "               | | ___   __ _       ___  ___ __ _ _ __   "
print "               | |/ _ \ / _` |-----/ __|/ __/ _` | '_  \ "
print "               | | (_) | (_| |-----\__ \ (_| (_| | | | | "
print "               |_|\___/ \__, |-----|___/\___\__,_|_| |_| "
print "                           | | "
print "                        __/_/  "
print "		"           
print "===================================================================== "
def findAdmin():
	f = open("target.txt","r");
	link = raw_input("contoh ; target.co  \n bot-robots(scan) : ")
	print "   "
	print "   "
	print "\n\nbot-robots(scan) : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "hasil  => ",req_link

def Credit():
	Space(9); print "  ------------------------"
	Space(9); print "[•] Cyber Sederhana Team [•]"
	Space(9); print "  ------------------------"
	Space(9); print " "

Credit()
findAdmin()
