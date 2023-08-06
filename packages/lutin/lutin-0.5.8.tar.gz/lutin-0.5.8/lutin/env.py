#!/usr/bin/python
##
## @author Edouard DUPIN
##
## @copyright 2012, Edouard DUPIN, all right reserved
##
## @license APACHE v2.0 (see license file)
##

# Local import
from . import debug



forceMode=False

def set_force_mode(val):
	global forceMode
	if val==1:
		forceMode = 1
	else:
		forceMode = 0

def get_force_mode():
	global forceMode
	return forceMode


printPrettyMode=False

def set_print_pretty_mode(val):
	global printPrettyMode
	if val == True:
		printPrettyMode = True
	else:
		printPrettyMode = False

def get_print_pretty_mode():
	global printPrettyMode
	return printPrettyMode

def print_pretty(myString, force=False):
	global printPrettyMode
	if    printPrettyMode == True \
	   or force == True:
		if myString[len(myString)-1]==' ' : 
			tmpcmdLine = myString[:len(myString)-1]
		else :
			tmpcmdLine = myString
		tmpcmdLine = tmpcmdLine.replace(' ', '\n\t')
		tmpcmdLine = tmpcmdLine.replace('\n\t\n\t', '\n\t')
		tmpcmdLine = tmpcmdLine.replace('\n\t\n\t', '\n\t')
		tmpcmdLine = tmpcmdLine.replace('\n\t\n\t', '\n\t')
		baseElementList = ["-o",
		                   "-D",
		                   "-I",
		                   "-L",
		                   "g++",
		                   "gcc",
		                   "clang",
		                   "clang++",
		                   "ar",
		                   "ld",
		                   "ranlib",
		                   "-framework",
		                   "-isysroot",
		                   "-arch",
		                   "-keystore",
		                   "-sigalg",
		                   "-digestalg",
		                   "<",
		                   "<<",
		                   ">",
		                   ">>"]
		for element in baseElementList:
			tmpcmdLine = tmpcmdLine.replace(element+'\n\t', element+' ')
		baseElementList = ["g++", "gcc", "clang", "clang++", "ar", "ld", "ranlib"]
		for element in baseElementList:
			tmpcmdLine = tmpcmdLine.replace('/'+element+' ', '/'+element+'\n\t')
		tmpcmdLine = tmpcmdLine.replace('\n\t', ' \\\n\t')
		
		return tmpcmdLine
	else:
		return myString

forceStripMode=False

def set_force_strip_mode(val):
	global forceStripMode
	if val==True:
		forceStripMode = True
	else:
		forceStripMode = False

def get_force_strip_mode():
	global forceStripMode
	return forceStripMode

