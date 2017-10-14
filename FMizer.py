#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# __version__ = '0.1'
# __author__ = 'Ghostboy-287'
# __Greetz to__ = 'boatsnbros & D0tix & ecouter-en-direct.com'

try:
	from colorama import Fore, Back, Style
	import subprocess
	from sys import platform
except():
    exit(Fore.RED+"\n\t[x] Session Annulée; Probléme avec un module ou module manquant"+Fore.RESET) 

if platform == "linux" or platform == "linux2" or platform == "darwin":
	pass
else:
	exit(Fore.RED+"\n\t[x] Marche uniquement sur Linux/MacOS, du moins pour le moment :)"+Fore.RESET)

try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen('mplayer', stdout=null, stderr=null)
    null.close()

except OSError:
    exit(Fore.RED+"\n\t[x] mplayer not installed! Merci de l'installer en utilisant la commande:"+Fore.YELLOW+" apt install mplayer\n"+Fore.RESET) 


try:

	print(Fore.MAGENTA+"""
           _   .-')               .-') _   ('-.  _  .-')  
          ( '.( OO )_            (  OO) )_(  OO)( \( -O ) 
   ,------.,--.   ,--.) ,-.-') ,(_)----.(,------.,------. 
('-| _.---'|   `.'   |  |  |OO)|       | |  .---'|   /`. '
(OO|(_\    |         |  |  |  \'--.   /  |  |    |  /  | |
/  |  '--. |  |'.'|  |  |  |(_/(_/   /  (|  '--. |  |_.' |
\_)|  .--' |  |   |  | ,|  |_.' /   /___ |  .--' |  .  '.'
  \|  |_)  |  |   |  |(_|  |   |        ||  `---.|  |\  \ 
   `--'    `--'   `--'  `--'   `--------'`------'`--' '--'
	      \n"""+Fore.RESET)



	Virgin = "http://mp3lg4.tdf-cdn.com/9243/lag_164753.mp3"
	Skyrock = "http://icecast.skyrock.net/s/natio_mp3_128k?type=.mp3"
	Nrj = "http://cdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3?origine=fluxradios"
	Europe1 = "http://audio.scdn.arkena.com/12541/europe1_64.mp3"
	RMC = "http://rmcinfo.cdn.dvmr.fr/rmcinfo"
	Franceinter = "http://direct.franceinter.fr/live/franceinter-midfi.mp3"

	print(Fore.CYAN+'┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╼['+Fore.YELLOW+'Radio Disponibles:'+Fore.CYAN+']╾┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'├╼[1]-'+Fore.GREEN+' Virgin radio                     Europe1 radio '+Fore.CYAN+'-[4]╾┤')
	print(Fore.CYAN+'├╼[2]-'+Fore.GREEN+' Skyrock radio                        RMC radio '+Fore.CYAN+'-[5]╾┤')
	print(Fore.CYAN+'├╼[3]-'+Fore.GREEN+' Nrj radio                         France inter '+Fore.CYAN+'-[6]╾┤')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'└┄┄┄┄┄┄┄┄┄┄┄┄┄╼['+Fore.RED+' Developed by Ghostboy-287 '+Fore.CYAN+']╾┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘')

	def pwait():
		try:
		    play.wait()
		except KeyboardInterrupt:
		    try:
		       play.terminate()
		    except OSError:
		       pass
		    play.wait()


	while True: 
		choice = input(Fore.BLUE+'\n\nVeuillez choisir une radio [example: 1 ; ou virgin] : ~$ '+Fore.RESET)
		if choice == '1' or choice.lower() == "virgin":
		    play = subprocess.Popen(['mplayer',Virgin])
		    pwait()
		elif choice == '2' or choice.lower() == "skyrock":
		    play = subprocess.Popen(['mplayer',Skyrock])
		    pwait()
		elif choice == '3' or choice.lower() == "nrj":
		    play = subprocess.Popen(['mplayer',Nrj])
		    pwait()
		elif choice == '4' or choice.lower() == "europe1":
		    play = subprocess.Popen(['mplayer',Europe1])
		    pwait()
		elif choice == '5' or choice.lower() == "rmc":
		    play = subprocess.Popen(['mplayer',RMC])
		    pwait()
		elif choice == '6' or choice.lower() == "franceinter":
		    play = subprocess.Popen(['mplayer',Franceinter])
		    pwait()
		else: 
			print(Fore.RED+'\n\t\n[!] Veuillez entrer un chiffre/nom de la liste!'+Fore.WHITE)


except (KeyboardInterrupt, SystemExit):
    print(Fore.RED+'\n\t\n[!] Session Cancelled'+Fore.WHITE)
