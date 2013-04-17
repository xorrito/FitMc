FitMc
===========

using
Technic-Launcher

Be Advices!!!
----
I've writen this in Ubuntu and I am using tools already available to me in this environment. so some things might not work in other distros.
Also if you happen to have a window manager other than compiz just use the "log on" part of it. with it logs you off when the thin window manager closes.

NEWS
----

* *Version 1* <br/>
  * Start of project

* *Version 1.5* <br/>
  * finished option to install texture pack
  * changed direction where user level files reside (.technic/FitMc)
  * fixed main starting program not pointing to the right logo
  * fixed "force re-download for game files to be able to work with all modpacks

* *Version 1.6* <br/>
  * Fixed .log cleaning
  * Changed starting prosses in hopes to speed up loading
  * Fixed finishing wd to avoid isues
  * Moved .deb file to ppa:xorrito/fitmc

Future
-----
  * All images are place holders and will be changed to nicer ones
  * option to add individual mods will be added, it will only add per mod pack, due to compatibility.
  * will change gui method to buttons instead of radio list
  * Unity integration
  * Option to load without Window Manager change
  * Clock display
  * Rearragement of all options

Features
-----
* Autofetching of Technic-Launcher
* Switch window managers to a slim one (with redundancy just in case if it dosent start on the first try)
* Menu with: 'quit, log off, turn off, troubleshoot, install textures, and install mods(NYI)'
* aided texture pack installation, will only add one and link from the other modpacks to lower space used
* Troubleshoot menu with: 'Re-Fetching of the launcher, Restart of launcher/game, Force game files to redownload, and a fix to stiky keys'

Reasoning of troubelshoot items
-----
* For the Re-fetching of the launcher is an old problem I used to have where it will hang even before it could download anything, deleting it and re-downloading it seemed to work.
* Restart of launcher: in oldish systems minecraft likes to freeze so this is a quick way to fix that. (granted if you can release the mouse of MineCraft)
* Force game files redownload: I run a server and sometimes the clients will give me a "mod missing or outdated" and this fixes it. it forces everything to redownload (not touching saves, statistics, lastlogin)
* Fix Stiky keys: this downloads an updated version of lwjgl and installs it to the game files, and seems to fix the stiky key situation.

-------
Feed back is greatly apreciated!
