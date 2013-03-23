FitMc
===========

using
Technic-Launcher

NEWS
----

* *Version 1* <br/>
Start of project

Features
-----
* Autofetching of Technic-Launcher
* Switch window managers to a slim one (with redundancy just in case if it dosent start on the first try)
* Menu with: 'quit, log off, turn off, troubleshoot, install textures(NYI), and install mods(NYI)'
* Troubleshoot menu with: 'Re-Fetching of the launcher, Restart of launcher/game, Force game files to redownload, and a fix to stiky keys'

Reasoning of troubelshoot items
-----
* For the Re-fetching of the launcher is an old problem I used to have where it will hang even before it could download anything, deleting it and re-downloading it seemed to work.
* Restart of launcher: in oldish systems minecraft likes to freeze so this is a quick way to fix that. (granted if you can release the mouse of MineCraft)
* Force game files redownload: I run a server and sometimes the clients will give me a "mod missing or outdated" and this fixes it. it forces everything to redownload (not touching saves, statistics, lastlogin)
* Fix Stiky keys: this downloads an updated version of lwjgl and installs it to the game files, and seems to fix the stiky key situation.

-------
Feed back is greatly apreciated!

Notes to self
-----
To find the size of the folder:
du -sx --exclude DEBIAN FitMc/
