#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# __version__ = '0.1'
# __author__ = 'mIcHyAmRaNe'
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
\t\t      ╔═╗╔╦╗┬┌─┐┌─┐┬─┐
\t\t      ╠╣ ║║║│┌─┘├┤ ├┬┘
\t\t      ╚  ╩ ╩┴└─┘└─┘┴└─"""+Fore.RESET)

	Virgin = "http://mp3lg4.tdf-cdn.com/9243/lag_164753.mp3"
	Skyrock = "http://icecast.skyrock.net/s/natio_mp3_128k?type=.mp3"
	Nrj = "http://cdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3?origine=fluxradios"
	Europe1 = "http://audio.scdn.arkena.com/12541/europe1_64.mp3"
	RMC = "http://rmcinfo.cdn.dvmr.fr/rmcinfo"
	Franceinter = "http://direct.franceinter.fr/live/franceinter-midfi.mp3"
	Tonic = "http://vr-wr6-mp3-128.scdn.arkena.com/virginradio.mp3"

	print(Fore.CYAN+'┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╼['+Fore.YELLOW+'Radio Disponibles:'+Fore.CYAN+']╾┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'├╼[1]-'+Fore.GREEN+' Virgin radio                         RMC radio '+Fore.CYAN+'-[5]╾┤')
	print(Fore.CYAN+'├╼[2]-'+Fore.GREEN+' Skyrock radio                     France inter '+Fore.CYAN+'-[6]╾┤')
	print(Fore.CYAN+'├╼[3]-'+Fore.GREEN+' Nrj radio                         Virgin Tonic '+Fore.CYAN+'-[7]╾┤')
	print(Fore.CYAN+'├╼[4]-'+Fore.GREEN+' Europe1 radio                                       '+Fore.CYAN+'┊')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'┊                                                          ┊')
	print(Fore.CYAN+'└┄┄┄┄┄┄┄┄┄┄┄┄┄╼['+Fore.RED+' Developed by mIcHyAmRaNe '+Fore.CYAN+']╾┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘')

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
		    play = subprocess.Popen(['mplayer', Virgin, Skyrock, Nrj, Europe1, RMC, Franceinter, Tonic,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '2' or choice.lower() == "skyrock":
		    play = subprocess.Popen(['mplayer', Skyrock, Nrj, Europe1, RMC, Franceinter, Tonic, Virgin,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '3' or choice.lower() == "nrj":
		    play = subprocess.Popen(['mplayer', Nrj, Europe1, RMC, Franceinter, Tonic, Virgin, Skyrock,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '4' or choice.lower() == "europe1":
		    play = subprocess.Popen(['mplayer', Europe1, RMC, Franceinter, Tonic, Virgin, Skyrock, Nrj,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '5' or choice.lower() == "rmc":
		    play = subprocess.Popen(['mplayer', RMC , Franceinter, Tonic, Virgin, Skyrock, Nrj, Europe1,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '6' or choice.lower() == "franceinter":
		    play = subprocess.Popen(['mplayer', Franceinter, Tonic, Virgin, Skyrock, Nrj, Europe1, RMC,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '7' or choice.lower() == "tonic":
		    play = subprocess.Popen(['mplayer', Tonic, Virgin, Skyrock, Nrj, Europe1, RMC ,Franceinter,])
		    print(Fore.GREEN+"\n  [<] : précédent \t[enter or >] : suivant \t[p or space] : pause \t[escap or q] : quitter\n"+Fore.RESET)
		    pwait()
		elif choice == '0' or choice.lower() == "exit" or choice.lower() == "quitter" or choice.lower() == "q":
		    exit(Fore.YELLOW+"\n\t[x] Bye Bye! et à la prochaine ^^ "+Fore.RESET)
		    continue
		else: 
			print(Fore.RED+'\n\t\n[!] Veuillez entrer un chiffre/nom de la liste!'+Fore.WHITE)


except (KeyboardInterrupt, SystemExit):
    print(Fore.RED+'\n\t\n[!] Session Cancelled'+Fore.WHITE)
