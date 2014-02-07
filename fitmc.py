#!/usr/bin/env python
import subprocess, glob, os, re, sys, ConfigParser, urllib2, datetime
from os.path import expanduser
from bs4 import BeautifulSoup
from urllib2 import urlopen
from gi.repository import Gtk
#Technic installation directory
thome=expanduser("~")+"/.technic/"
fhome=thome+"FitMc/"
config=ConfigParser.ConfigParser()
####==========================Version=Checker======================####
#Technic Launcher version finder
def tlv_finder():
	print("============VCHECK============")
	global tlv
	tldp="http://www.technicpack.net/download"
	try: 
		urllib2.urlopen(tldp, timeout=5)
	except urllib2.URLError:
		print("Can't read: "+tldp)
		print("Using Fallback Version")
		print(tlv)
	else:
		html=urlopen(tldp).read()
		soup=BeautifulSoup(html, "lxml")
		dirtytlv=soup.find("p", "download-subtext")
		cleantlv=dirtytlv.get_text()
		fattlv=re.sub('[^A-Za-z0-9]+', '', cleantlv)+"end"
		global ntlv
		ntlv=re.search('Build(.+?)end',fattlv).group(1)
		print("Current Version Number: "+tlv)
		print("Online Version Number: "+ntlv)
		if ntlv > tlv:
			global utl
			utl = "yes"
			print("Update Found")
		else:
			print("No Update Found")
		global LastVCheck
		LastVCheck = today
	print("===========VCHECK=END=========")
####========================Configuration=File=====================####
def init_settings():
	print("====INITIATING=CONFIG=FILE====")
	global tlv
	tlv = "389"
	global ntlv
	ntlv = "N-A"
	global utl
	utl = "no"
	global today
	today = datetime.date.today()
	global margin
	margin = datetime.timedelta(days = 1)
	global LastVCheck
	LastVCheck = datetime.date(2014, 1, 25)
	config.add_section('versions')
	config.set('versions','technic',tlv)
	config.set('versions', 'newtechnic', ntlv)
	config.set('versions', 'needupdate', utl)
	config.set('versions', 'LastVCheck', LastVCheck)
	print("==INITIATING=CONFIG=FILE=END==")
def save_settings():
	print("=============SAVE=============")
	print("Saving to settings.ini")
	with open("settings.ini", "w") as configfile:
		config.write(configfile)
	print("===========Save=END===========")
def load_settings():
	print("=============LOAD=============")
	global tlv
	config.read("settings.ini")
	print("Loaded Sections:")
	print(config.sections())
	tlv = config.get('versions', 'technic')
	ntlv = config.get('versions', 'newtechnic')
	utl = config.get('versions', 'needupdate')
	LastVCheck = config.get('versions', 'LastVCheck')
	print("Loaded Version:")
	print("Thechnic Launcher Current: "+tlv)
	print("Thechnic Launcher New: "+ntlv)
	print("Show Update Button: "+utl)
	
	print("============LOAD=END==========")
####============================Extras=========================####
#Remove logs to avoide clutter
def logrm():
	print("==========LOG=CLENER=========")
	os.chdir(thome+"logs")
	loglist = glob.glob("*.log")
	for f in loglist:
		os.remove(f)
	os.chdir(fhome)
	print("=======LOG=CLEANER=END=======")
####============================GUI=========================####
def main_window():
	print('=============GUI=============')
	win = FitMcWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()
class FitMcWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="FitMc")
		global grid
		grid = Gtk.Grid()
		#Widgets:
		label = Gtk.Label("menu")
		button1 = Gtk.Button(label="Textures & Mods")
		button2 = Gtk.Button(label="Technic Laucher Options")
		button3 = Gtk.Button(label="Extras Options")
		button4 = Gtk.Button(label="Exit Options")
		#Window architechture
		self.add(grid)
		grid.add(label)
		grid.attach_next_to(button1, label, Gtk.PositionType.BOTTOM, 1, 1)
		grid.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 1)
		grid.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 1, 1)
		grid.attach_next_to(button4, button3, Gtk.PositionType.BOTTOM, 1, 1)
		#connections to widgets		
		button1.connect("clicked", self.on_button1_clicked)
		button2.connect("clicked", self.on_button2_clicked)
		button3.connect("clicked", self.on_button3_clicked)
		button4.connect("clicked", self.on_button4_clicked)
		if utl == "yes":
			print("Showing Update Button")
			global button5
			button5 = Gtk.Button(label="Upgrade Launcher")
			grid.attach_next_to(button5, label, Gtk.PositionType.RIGHT, 1, 1)
			button5.connect("clicked", self.on_button5_clicked)
			button5.show()
	def on_button1_clicked(self, widget):
		print("tnm button pressed")
	def on_button2_clicked(self, widget):
		print("tlo button pressed")
	def on_button3_clicked(self, widget):
		print("exop button pressed")
	def on_button4_clicked(self, widget):
		print("exiop button Pressed")
	def on_button5_clicked(self, widget):
		print("Upgrade tlv")
		button5.destroy()
####=========================main=program=====================####
#Ini sequence also download TL if not found.
def start():
	print("----------FITMC----------")
	if not os.path.exists(fhome):
		print("Making FitMC folder")
		print(fhome)
		os.makedirs(fhome)
		os.chdir(fhome)
		init_settings()
	else:
		os.chdir(fhome)
		if not os.path.isfile("settings.ini"):
			print("Making Settings File")
			print("settings.ini")
			init_settings()
		else:
			load_settings()
	if today - margin >= LastVCheck:
		print('margin reached checking for updates')
		tlv_finder()
		save_settings()
start()
main_window()
