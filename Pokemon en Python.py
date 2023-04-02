# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from random import randint
from time import sleep

if __name__ == '__main__':
	# *********************************************INICIO DEL PROGRMA*****************************************
	i = int()
	cont = int()
	opc = int()
	opc1 = int()
	opc2 = int()
	opc3 = int()
	opc4 = int()
	opc5 = int()
	opc6 = int()
	win = int()
	opcmipoke = int()
	cantidadpoke = int()
	lvl = int()
	nombre = str()
	jugador1 = str()
	enemigo = str()
	enemigo1 = str()
	saliropc = str()
	salir = bool()
	# Comienzo del juego
	nombre = [str() for ind0 in range(4)]
	enemigo = [str() for ind0 in range(8)]
	cont = 1
	win = 0
	nombre[0] = "GUALDO"
	nombre[1] = "ASH"
	nombre[2] = "JAIME"
	enemigo[7] = "AZUL"
	enemigo[0] = "GARY"
	enemigo[1] = "JUAN"
	enemigo[3] = "BENJAMIN"
	enemigo[4] = "EQUIPO XxX"
	enemigo[5] = "ANONIMO"
	enemigo[6] = "CARLOS"
	# *****************************************************************************************
	# *************************************ELEECION DE POKEMONES*******************************
	# *****************************************************************************************
	nombrepokemon = str()
	pokemon = str()
	p = int()
	z = int()
	# USUARIO PARTE X
	mipoke = str()
	mipoket1 = str()
	mipoket2 = str()
	mipoket3 = str()
	mipoket4 = str()
	mipoket5 = str()
	mipoket6 = str()
	# USUARIO PARTE X
	mipokeh1 = float()
	mipokeh2 = float()
	mipokeh3 = float()
	mipokeh4 = float()
	mipokeh5 = float()
	mipokeh6 = float()
	error = float()
	err = float()
	# CPU PARTE XI
	enepoke = str()
	enepoket1 = str()
	enepoket2 = str()
	enepoket3 = str()
	enepoket4 = str()
	enepoket5 = str()
	enepoket6 = str()
	# CPU PARTE XI
	enepokeh1 = float()
	enepokeh2 = float()
	enepokeh3 = float()
	enepokeh4 = float()
	enepokeh5 = float()
	enepokeh6 = float()
	eleccionpoke = float()
	error2 = float()
	minivel = float()
	enenivel = float()
	minivel = [int() for ind0 in range(6)]
	enenivel = [int() for ind0 in range(6)]
	# CPU PARTE XI
	enepoke = [str() for ind0 in range(6)]
	enepoket1 = [str() for ind0 in range(2)]
	enepokeh1 = [int() for ind0 in range(5)]
	enepoket2 = [str() for ind0 in range(2)]
	enepokeh2 = [int() for ind0 in range(5)]
	enepoket3 = [str() for ind0 in range(2)]
	enepokeh3 = [int() for ind0 in range(5)]
	enepoket4 = [str() for ind0 in range(2)]
	enepokeh4 = [int() for ind0 in range(5)]
	enepoket5 = [str() for ind0 in range(2)]
	enepokeh5 = [int() for ind0 in range(5)]
	enepoket6 = [str() for ind0 in range(2)]
	enepokeh6 = [int() for ind0 in range(5)]
	# USUARIO PARTE X
	mipoke = [str() for ind0 in range(6)]
	mipoket1 = [str() for ind0 in range(2)]
	mipokeh1 = [int() for ind0 in range(5)]
	mipoket2 = [str() for ind0 in range(2)]
	mipokeh2 = [int() for ind0 in range(5)]
	mipoket3 = [str() for ind0 in range(2)]
	mipokeh3 = [int() for ind0 in range(5)]
	mipoket4 = [str() for ind0 in range(2)]
	mipokeh4 = [int() for ind0 in range(5)]
	mipoket5 = [str() for ind0 in range(2)]
	mipokeh5 = [int() for ind0 in range(5)]
	mipoket6 = [str() for ind0 in range(2)]
	mipokeh6 = [int() for ind0 in range(5)]
	nombrepokemon = [str() for ind0 in range(80)]
	pokemon = [str() for ind0 in range(7)]
	error = [int() for ind0 in range(6)]
	error2 = [int() for ind0 in range(6)]
	# Asignar pokemon vacio
	mipoke[0] = ""
	# ELECCION DE POKEMON usuario
	error[5] = 0
	error[0] = 0
	error[1] = 0
	error[2] = 0
	error[3] = 0
	error[4] = 0
	# ELECCION DE POKEMON cpu
	error2[5] = 0
	error2[0] = 0
	error2[1] = 0
	error2[2] = 0
	error2[3] = 0
	error2[4] = 0
	# NO EXISTE ESTA POSICION DE POKEMON
	nombrepokemon[0] = ""
	# *************************************************************FIN ELECCION DE POKEMON**************************
	# **************************************************OPCION 2***************************************************
	# *********************************************** opcion1 1v1 *************************************************
	# descripcion: eleccion de pokemon que se enfrenta al 1vs1
	# USUARIO 
	misaludpoke = float()
	misalud = float()
	miataquepoke = float()
	midefensapoke = float()
	mivelocidadpoke = float()
	miespecialpoke = float()
	minombrepoke = str()
	mitipo = str()
	mitipo = [str() for ind0 in range(2)]
	misalud = [int() for ind0 in range(6)]
	# CPU
	enesaludpoke = float()
	enesalud = float()
	eneataquepoke = float()
	enedefensapoke = float()
	enevelocidadpoke = float()
	eneespecialpoke = float()
	eneazar = float()
	enenombrepoke = str()
	enetipo = str()
	enetipo = [str() for ind0 in range(2)]
	enesalud = [int() for ind0 in range(6)]
	# ************************************************************************************************************
	# ************************************BATALLA ASIGNACION******************************************************
	nombreataque = str()
	tipoataque = str()
	pp = str()
	efectivo = str()
	dano = str()
	nombreataque = [str() for ind0 in range(4)]
	tipoataque = [str() for ind0 in range(4)]
	pp = [str() for ind0 in range(4)]
	efectivo = [str() for ind0 in range(4)]
	dano = [str() for ind0 in range(4)]
	nombrea1 = str()
	tipoa1 = str()
	nombrea2 = str()
	tipoa2 = str()
	nombrea3 = str()
	tipoa3 = str()
	nombrea4 = str()
	tipoa4 = str()
	nombrea5 = str()
	tipoa5 = str()
	nombrea6 = str()
	tipoa6 = str()
	ppa1 = float()
	efectivoa1 = float()
	danoa1 = float()
	ppa2 = float()
	efectivoa2 = float()
	danoa2 = float()
	ppa3 = float()
	efectivoa3 = float()
	danoa3 = float()
	ppa4 = float()
	efectivoa4 = float()
	danoa4 = float()
	ppa5 = float()
	efectivoa5 = float()
	danoa5 = float()
	ppa6 = float()
	efectivoa6 = float()
	danoa6 = float()
	contx = float()
	nombrea1 = [str() for ind0 in range(4)]
	tipoa1 = [str() for ind0 in range(4)]
	nombrea2 = [str() for ind0 in range(4)]
	tipoa2 = [str() for ind0 in range(4)]
	nombrea3 = [str() for ind0 in range(4)]
	tipoa3 = [str() for ind0 in range(4)]
	nombrea4 = [str() for ind0 in range(4)]
	tipoa4 = [str() for ind0 in range(4)]
	nombrea5 = [str() for ind0 in range(4)]
	tipoa5 = [str() for ind0 in range(4)]
	nombrea6 = [str() for ind0 in range(4)]
	tipoa6 = [str() for ind0 in range(4)]
	ppa1 = [float() for ind0 in range(4)]
	efectivoa1 = [float() for ind0 in range(4)]
	danoa1 = [float() for ind0 in range(4)]
	ppa2 = [float() for ind0 in range(4)]
	efectivoa2 = [float() for ind0 in range(4)]
	danoa2 = [float() for ind0 in range(4)]
	ppa3 = [float() for ind0 in range(4)]
	efectivoa3 = [float() for ind0 in range(4)]
	danoa3 = [float() for ind0 in range(4)]
	ppa4 = [float() for ind0 in range(4)]
	efectivoa4 = [float() for ind0 in range(4)]
	danoa4 = [float() for ind0 in range(4)]
	ppa5 = [float() for ind0 in range(4)]
	efectivoa5 = [float() for ind0 in range(4)]
	danoa5 = [float() for ind0 in range(4)]
	ppa6 = [float() for ind0 in range(4)]
	efectivoa6 = [float() for ind0 in range(4)]
	danoa6 = [float() for ind0 in range(4)]
	nombree1 = str()
	tipoe1 = str()
	nombree2 = str()
	tipoe2 = str()
	nombree3 = str()
	tipoe3 = str()
	nombree4 = str()
	tipoe4 = str()
	nombree5 = str()
	tipoe5 = str()
	nombree6 = str()
	tipoe6 = str()
	ppe1 = float()
	efectivoe1 = float()
	danoe1 = float()
	ppe2 = float()
	efectivoe2 = float()
	danoe2 = float()
	ppe3 = float()
	efectivoe3 = float()
	danoe3 = float()
	ppe4 = float()
	efectivoe4 = float()
	danoe4 = float()
	ppe5 = float()
	efectivoe5 = float()
	danoe5 = float()
	ppe6 = float()
	efectivoe6 = float()
	danoe6 = float()
	nombree1 = [str() for ind0 in range(4)]
	tipoe1 = [str() for ind0 in range(4)]
	nombree2 = [str() for ind0 in range(4)]
	tipoe2 = [str() for ind0 in range(4)]
	nombree3 = [str() for ind0 in range(4)]
	tipoe3 = [str() for ind0 in range(4)]
	nombree4 = [str() for ind0 in range(4)]
	tipoe4 = [str() for ind0 in range(4)]
	nombree5 = [str() for ind0 in range(4)]
	tipoe5 = [str() for ind0 in range(4)]
	nombree6 = [str() for ind0 in range(4)]
	tipoe6 = [str() for ind0 in range(4)]
	ppe1 = [float() for ind0 in range(4)]
	efectivoe1 = [float() for ind0 in range(4)]
	danoe1 = [float() for ind0 in range(4)]
	ppe2 = [float() for ind0 in range(4)]
	efectivoe2 = [float() for ind0 in range(4)]
	danoe2 = [float() for ind0 in range(4)]
	ppe3 = [float() for ind0 in range(4)]
	efectivoe3 = [float() for ind0 in range(4)]
	danoe3 = [float() for ind0 in range(4)]
	ppe4 = [float() for ind0 in range(4)]
	efectivoe4 = [float() for ind0 in range(4)]
	danoe4 = [float() for ind0 in range(4)]
	ppe5 = [float() for ind0 in range(4)]
	efectivoe5 = [float() for ind0 in range(4)]
	danoe5 = [float() for ind0 in range(4)]
	ppe6 = [float() for ind0 in range(4)]
	efectivoe6 = [float() for ind0 in range(4)]
	danoe6 = [float() for ind0 in range(4)]
	pos = int()
	misaludfija = int()
	mifijopp = int()
	enefijopp = int()
	enesaludfija = int()
	mifijopp = [int() for ind0 in range(4)]
	enefijopp = [int() for ind0 in range(4)]
	# Atques
	mipp = float()
	enepp = float()
	midano = float()
	enedano = float()
	opcionataque = float()
	eneaumento = float()
	miaumento = float()
	minombreataque = str()
	enenombreataque = str()
	mitipoa = str()
	enetipoa = str()
	tipoe = str()
	tipox = str()
	miestado = str()
	miest = str()
	eneest = str()
	eneestado = str()
	minombreataque = [str() for ind0 in range(4)]
	enenombreataque = [str() for ind0 in range(4)]
	mipp = [float() for ind0 in range(4)]
	enepp = [float() for ind0 in range(4)]
	mitipoa = [str() for ind0 in range(4)]
	enetipoa = [str() for ind0 in range(4)]
	enedano = [float() for ind0 in range(4)]
	midano = [float() for ind0 in range(4)]
	milvl = float()
	enelvl = float()
	mihp = bool()
	enehp = bool()
	mitotaldano = float()
	enetotaldano = float()
	mipoderataque = float()
	enepoderataque = float()
	ataquepoke = float()
	enev = float()
	miv = float()
	totalsalud = float()
	enetotalsalud = float()
	b = float()
	v = float()
	e = float()
	mie = float()
	miataque = str()
	eneataque = str()
	# ***** pp Fijo y  salud Fija
	ppfa1 = float()
	ppfa2 = float()
	ppfa3 = float()
	ppfa4 = float()
	ppfa5 = float()
	ppfa6 = float()
	ppfe1 = float()
	ppfe2 = float()
	ppfe3 = float()
	ppfe4 = float()
	ppfe5 = float()
	ppfe6 = float()
	ppfa1 = [float() for ind0 in range(4)]
	ppfa2 = [float() for ind0 in range(4)]
	ppfa3 = [float() for ind0 in range(4)]
	ppfa4 = [float() for ind0 in range(4)]
	ppfa5 = [float() for ind0 in range(4)]
	ppfa6 = [float() for ind0 in range(4)]
	ppfe1 = [float() for ind0 in range(4)]
	ppfe2 = [float() for ind0 in range(4)]
	ppfe3 = [float() for ind0 in range(4)]
	ppfe4 = [float() for ind0 in range(4)]
	ppfe5 = [float() for ind0 in range(4)]
	ppfe6 = [float() for ind0 in range(4)]
	# ************************************************************************************************************
	# RESTANTES
	paralizadoa = bool()
	paralizadoe = bool()
	start = bool()
	paralizadoa = False
	paralizadoe = False
	start = False
	estadoa = str()
	estadoe = str()
	estadofe = str()
	estadofa = str()
	life = str()
	k_o = float()
	suerte = float()
	micontwin = float()
	enecontwin = float()
	drenado = float()
	life = [str() for ind0 in range(12)]
	micontwin = 0
	enecontwin = 0
	estadoa = ""
	estadofe = ""
	estadofa = ""
	estadoe = ""
	# ************************************************************************************************************
	# ************************************************************************************************************
	print("")
	print("  D U O C  2 0 1 6               .::. ")
	print("                               .;:** ")
	print("                               `")
	print("   .:XHHHHk.              db.   .;;.     dH  MX  ")
	print("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN")
	print("QMMMMMb   MMX       MMMMMMP  MX   M~   MMM MMM  .oo. XMMM   ´MMM")
	print("  `MMMM.  )M> :X!Hk. MMMM   XMM.o   .  MMMMMMM X?XMMM MMM> !MMP")
	print("   ´MMMb.dM! XM M´?M MMMMMX.`MMMMMMMM~ MM M MM XM `  MX MMX XMM")
	print("    ~MMMMM~ XMM. .XM XM` MMMb.~~MMMM~.MMX M  t MMbooMM XM MMMMP")
	print("     ?MMM>  YMMMMMM! MM   `?MMRb.    `       !L MMMMM XM  IMMM")
	print("      MMMX    MMMM   MM       ~%:            !Mh.  dMI     IMMP")
	print("      ´MMM.                                                IMX")
	print("       ~M!M                                                 BMT")
	print("                      A M A R I L L O ")
	print("")
	input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
	print("") # no hay forma directa de borrar la pantalla con Python estandar
	for i in range(1,3):
		print("_¶___________¶¶¶")
		print("_¶¶__________¶__¶")
		print("¶__¶_________¶___¶")
		print("¶___¶________¶___¶")
		print("¶____¶_______¶____¶¶¶¶¶¶")
		print("¶_____¶______¶__________¶¶")
		print("¶______¶¶¶__¶_¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶")
		print("¶_____¶___¶¶_¶¶¶¶________________¶¶¶¶")
		print("_¶___¶___¶¶___¶¶___________¶¶¶¶¶¶")
		print("__¶__¶__¶___¶_____¶___¶¶¶¶_¶")
		print("___¶_¶_¶______________¶¶¶¶_¶")
		print("¶¶¶__¶¶_________¶¶¶¶______¶")
		print("¶___¶__¶_________@¶____¶__¶")
		print("_¶___¶_¶_________________¶")
		print("__¶__¶_¶________________¶¶")
		print("___¶_¶¶___________________¶¶")
		print("____¶¶_________________¶¶___¶")
		print("____¶_________________¶__¶___¶")
		print("___¶_________________¶____¶¶¶¶")
		print("__¶___________________¶")
		print("__¶____________________¶")
		print("__¶_____¶¶¶¶¶¶¶¶_______¶")
		print("___¶__¶¶________¶¶____¶")
		print("___¶__¶___________¶____¶¶")
		print("__¶¶¶¶_____________¶¶¶¶¶¶¶¶")
		print("Mantenga presionado cualquier boton hasta que carga completo")
		print("")
		print("                     CARGANDO ",cont,"%")
		cont = cont+5
		sleep(1)
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("_¶___________¶¶¶")
		print("_¶¶__________¶__¶")
		print("¶__¶_________¶___¶")
		print("¶___¶________¶___¶")
		print("¶____¶_______¶____¶¶¶¶¶¶")
		print("¶_____¶______¶__________¶¶")
		print("¶______¶¶¶__¶_¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶")
		print("¶_____¶___¶¶_@¶¶¶________________¶¶¶¶")
		print("_¶___¶___¶¶___¶¶___________¶¶¶¶¶¶")
		print("__¶__¶__¶___¶_____¶___¶¶@¶_¶")
		print("___¶_¶_¶______________¶@¶¶_¶")
		print("¶¶¶__¶¶_________¶¶¶¶______¶")
		print("¶___¶__¶_________¶¶____¶__¶___¶¶¶¶")
		print("_¶___¶_¶_________________¶__¶¶__¶")
		print("__¶__¶_¶________________¶¶¶¶__¶")
		print("___¶_¶¶_____________________¶¶ ")
		print("____¶¶_________________¶¶¶¶¶")
		print("____¶_________________¶")
		print("___¶_________________¶")
		print("__¶___________________¶")
		print("__¶____________________¶")
		print("__¶_____¶¶¶¶¶¶¶¶_______¶")
		print("___¶__¶¶________¶¶____¶")
		print("___¶__¶___________¶____¶¶")
		print("__¶¶¶¶_____________¶¶¶¶¶¶¶¶")
		print("Mantenga presionado cualquier boton hasta que carga completo")
		print("")
		print("                     CARGANDO ",cont,"%")
		cont = cont+30
		sleep(50/1000.0)
		print("") # no hay forma directa de borrar la pantalla con Python estandar
	while True:# no hay 'repetir' en python
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  1.-  J U E G O    N U E V O                 |")
		print(" |                                              |")
		print(" |  2.-  S A L I R                              |")
		print(" |                                              |")
		print(" @----------------------------------------------@")
		print("Eliga una opción : ", end="")
		opc = int(input())
		if opc==1 or opc==2 or opc==4 or opc==5 or opc==6: break
	if opc==1 or opc==4 or opc==5 or opc==6:
		if opc==4:
			jugador1 = "Benjamin"
			enemigo1 = "Carlos"
		if opc==5:
			jugador1 = "Carlos"
			enemigo1 = "Gary"
			opc = 4
			win = 100002312381283
		if opc==6:
			jugador1 = "Ñe"
			enemigo1 = "Chanchiwagui"
			opc = 4
			win = 0
		salir = False
	if opc==2:
		salir = True
	# Saludos del maestro
	if opc==1:
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                    >MVM")
		print("                    M~ ~M ")
		print("                   °| _ |")
		print("                 __- \\_/-__")
		print("                |   ____   \\ ")
		print("                | |_|>  |  | |")
		print("                |___>___|| |")
		print("                  /  _  |<_|")
		print("                 |  / \\ \\ ")
		print("                 |__| |__\\ ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡H o l a    a    t o d o s!                 |")
		print(" |                                              |")
		print(" |  ¡Bienvenidos al  mundo de POKéMON!          |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                    >MVM")
		print("                    M~ ~M ")
		print("                   °| o |")
		print("                 __- \\_/-__")
		print("                |    ____   \\ ")
		print("                | |_|>  |  | |")
		print("                |___>___|| |")
		print("                  /  _  |<_|")
		print("                 |  / \\ \\ ")
		print("                 |__| |__\\ ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡Me llamo AOK!                              |")
		print(" |                                              |")
		print(" |  ¡Pero la gente me llama el PROFESOR POKéMon!|")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡Este mundo está habitado por unas          |")
		print(" |                                              |")
		print(" |  criaturas llamadas POKéMon!                 |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  Para algunos, los POKéMON son mascotas.     |")
		print(" |                                              |")
		print(" |  Pero otros los usan para pelear.            |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  En cuanto a mí...                           |")
		print(" |                                              |")
		print(" |                                              |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  Estudio a los POKéMON como profesión.       |")
		print(" |                                              |")
		print(" |                                              |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		# ASHH CAMBIAR IMAGEN
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("    __ _              ")
		print("   /___\\_\\            ")
		print("   l___l__l          ")
		print("  /___/  \\            ")
		print("   l + ~/_/           ")
		print("   \\___/_/\\           ")
		print("   /l l l l\\          ")
		print("  / l l l l\\/\\        ")
		print(" / +l l l l \\ \\       ")
		print(" \\/\\l~__l l / /       ")
		print("  \\/l l l l l_l       ")
		print("    l_l l_l           ")
		print("    /_/ \\_\\           ")
		print("                      ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  Pero primero dime cómo te llamas.           |")
		print(" |                                              |")
		print(" |                                              |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		while True:# no hay 'repetir' en python
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("                     ")
			print(" @----NOMBRE-------@ ")
			print(" |                 | ")
			print(" |   1.- NUEVO N.  | ")
			print(" |                 | ")
			print(" |   2.- GUALDO    | ")
			print(" |                 | ")
			print(" |   3.- ASH       | ")
			print(" |                 | ")
			print(" |   4.- JAIME     | ")
			print(" |                 | ")
			print(" @-----------------@")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			print(" |  Estudio a los POKéMON como profesión.       |")
			print(" |                                              |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			print("Elegir la opción", end="")
			opc1 = int(input())
			if opc1==1 or opc1==2 or opc1==3 or opc1==4: break
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		if opc1==1:
			print(" @----------------------------------------------@")
			print(" |                                              |")
			print(" |  ¿ TU NOMBRE                                 |")
			print(" |                _____________________         |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			print("Escribe tu nombre: ", end="")
			nombre[3] = input()
			jugador1 = nombre[3]
		if opc1==2:
			jugador1 = nombre[0]
		if opc1==3:
			jugador1 = nombre[1]
		if opc1==4:
			jugador1 = nombre[2]
		# siguiente parte
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("    __ _              ")
		print("   /___\\_\\            ")
		print("   l___l__l          ")
		print("  /___/  \\            ")
		print("   l + ~/_/           ")
		print("   \\___/_/\\           ")
		print("   /l l l l\\          ")
		print("  / l l l l\\/\\        ")
		print(" / +l l l l \\ \\       ")
		print(" \\/\\l~__l l / /       ")
		print("  \\/l l l l l_l       ")
		print("    l_l l_l           ")
		print("    /_/ \\_\\           ")
		print("                      ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡Bien!  ¡Tu nombre es ",jugador1,"!        |")
		print(" |                                              |")
		print(" |                                              |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                  __\\__        ")
		print("                 /     \\/\\_ _  ")
		print("                / __/\\/\\l /_/")
		print("                \\/l~ ~l/  l_l ")
		print("                  \\_u_/\\__\\ \\ ")
		print("                 /l   Q ___\\_\\ ")
		print("                 ll    l      ")
		print("                /_l  __l      ")
		print("                l_l__l__l     ")
		print("                  l l ~ l     ")
		print("                  l l l l     ")
		print("                  l l l l     ")
		print("                  /_/ \\_\\     ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  Este es mi nieto. él ha sido tu rival desde |")
		print(" |                                              |")
		print(" |  que eras un niño.                           |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		while True:# no hay 'repetir' en python
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("                     ")
			print(" @----NOMBRE-------@ ")
			print(" |                 | ")
			print(" |   1.- NUEVO N.  | ")
			print(" |                 | ")
			print(" |   2.- AZUL      | ")
			print(" |                 | ")
			print(" |   3.- GARY      | ")
			print(" |                 | ")
			print(" |   4.- JUAN      | ")
			print(" |                 | ")
			print(" @-----------------@")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			print(" |  ...Mmm, ¿podrías decirme cómo se llama?     |")
			print(" |                                              |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			print("Elegir la opción", end="")
			opc2 = int(input())
			if opc2==1 or opc2==2 or opc2==3 or opc2==4: break
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		if opc2==1:
			print(" @----------------------------------------------@")
			print(" |                                              |")
			print(" |  ¿NOMBRE RIVAL?                                |")
			print(" |                _____________________         |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			print("Escribe tu nombre: ", end="")
			enemigo[3] = input()
			enemigo1 = enemigo[3]
		if opc2==2:
			enemigo1 = enemigo[7]
		if opc2==3:
			enemigo1 = enemigo[0]
		if opc2==4:
			enemigo1 = enemigo[1]
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                  __\\__        ")
		print("                 /     \\/\\_ _  ")
		print("                / __/\\/\\l /_/")
		print("                \\/l~ ~l/  l_l ")
		print("                  \\_u_/\\__\\ \\ ")
		print("                 /l   Q ___\\_\\ ")
		print("                 ll    l      ")
		print("                /_l  __l      ")
		print("                l_l__l__l     ")
		print("                  l l ~ l     ")
		print("                  l l l l     ")
		print("                  l l l l     ")
		print("                  /_/ \\_\\     ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡Ah, sí!  !Ahora lo recuerdo!               |")
		print(" |                                              |")
		print(" |         ¡Se llama ",enemigo1,"!      |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		# Volver a la imagene de ASH
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡",jugador1,"!   ¡Tu propia leyenda POKéMON |")
		print(" |                                              |")
		print(" |  está a punto de comenzar!                   |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("                           ")
		print("                 ")
		print("                  __________")
		print("                 (Pika pika!) ")
		print("                 (/      ")
		print("         /\\_.._(\\   /z ")
		print("         (O^__^O) Z__7 ")
		print("         (v____v)Z 7    ")
		print("           v  v         ")
		print("   _____________________")
		print("              ")
		print("")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" |  ¡Te espera un mundo de sueños y aventuras   |")
		print(" |                                              |")
		print(" |  con los POKéMON!                            |")
		print(" |                                         \\/   |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		while True:# no hay 'repetir' en python
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("                     | v  v|                    ")
			print("                     |  v  |                    ")
			print("                     |   v |                    ")
			print("                     |     |                    ")
			print("°°°°°°°°°°°°°°°°°°°°°° [4] °°°°°°°°°°°°°°°°°°°°°")
			print("°         ______             _________         °")
			print("°        /------\\           /---------\\        °")
			print("°       | [_][_] |         | [__] _[_] |       °")
			print("°   [1] |_||_____|     [2] !_____| |___!       °")
			print("°                                              °")
			print("°                                              °")
			print("°    °°°°°°°[0]          _____________         °")
			print("°    ~v~v~v~    O       /             \\        °")
			print("°    v!v!v!v   -|-     /|_ _ _ _ _ _ _|\\       °")
			print("°              /l      \\/[][][] [][][]\\/       °")
			print("°                       | - - - - - - |        °")
			print("°     _______           |_RRRR_| |_RRR|        °")
			print("°°°°°°///////°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			print(" |  !VE RAPIDO A UNA PELEA!                     |")
			print(" |                        (OPCIÓN 4)            |")
			print(" |                                              |")
			print(" |                                              |")
			print(" @----------------------------------------------@")
			opc3 = int(input())
			if opc3==1 or opc3==2 or opc3==3:
				print("")
				print("")
				print("No puedes entrar, necesitas completar la historia")
				sleep(2)
			if opc3==4: break
		if opc3==4:
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("                     | v  v|                    ")
			print("                     |  v  |                    ")
			print("                     |  v  |                    ")
			print("                     |     |                    ")
			print("°°°°°°°°°°°°°°°°°°°°°°     °°°°°°°°°°°°°°°°°°°°°")
			print("°         ______             _________         °")
			print("°        /------\\           /---------\\        °")
			print("°       | [_][_] |         | [__] _[_] |       °")
			print("°       |_||_____|         !_____| |___!       °")
			print("°                                              °")
			print("°                                              °")
			print("°    °°°°°°°             _____________         °")
			print("°    ~v~v~v~            /             \\        °")
			print("°    v!v!v!v           /|_ _ _ _ _ _ _|\\       °")
			print("°                      \\/[][][] [][][]\\/       °")
			print("°                       | - - - - - - |        °")
			print("°     _______           |_RRRR_| |_RRR|        °")
			print("°°°°°°///////°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
			print(" @----------------------------------------------@")
			print(" |  OAK: ¡HEY ALTO NO VAYAS!                    |")
			sleep(1)
			print(" |           ¡Ufff! ¡Estuvo cerca!              |")
			sleep(1)
			print(" |    ¡En la hierba viven POKéMON salvajes!     |")
			print(" |                                              |")
			print(" |                                              |")
			print(" @----------------------------------------------@")
			sleep(3)
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			# PONER A PIkACHU CON ASH DE ESPALDA
			print("                           ")
			print("                 ")
			print("                  __________")
			print("                 (Pika pika!) ")
			print("                 (/      ")
			print("         /\\_.._(\\   /z ")
			print("         (O^__^O) Z__7 ")
			print("         (v____v)Z 7    ")
			print("           v  v         ")
			print("   _____________________")
			print("              ")
			print("")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" |  ¡Un PIKACHU salvaje aparecio!               |")
			print(" |                                              |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			# PONER A PIkACHU CON ASH DE ESPALDA
			print("                           ")
			print("                 ")
			print("                  __________")
			print("                 (Pika pika!) ")
			print("                 (/      ")
			print("         /\\_.._(\\   /z ")
			print("         (O^__^O) Z__7 ")
			print("         (v____v)Z 7    ")
			print("           v  v         ")
			print("   _____________________")
			print("              ")
			print("")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" |  ¡El profesor ocupo pokeball!                |")
			print(" |                                              |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			sleep(2)
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			# PONER A PIkACHU CON ASH DE ESPALDA
			print("                           ")
			print("  PIKACHU                                ")
			print("      :N5                     ° °      ")
			print(" | Ps:----------            °     °     ")
			print(" |______________\\          °-------° ")
			print("                            °     °  ")
			print("                              ° ° ")
			print("             ")
			print("                 ")
			print("                   ")
			print("              ")
			print("")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | ¡Muy bien! ¡PIKACHU fue atrapado!            |")
			print(" |                                              |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | OAK: Vaya...                                 |")
			sleep(1)
			print(" |  ¡Necesitas a tu propio POKéMON como         |")
			print(" |                         protección           |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | ¿Yo lo sé!                                   |")
			sleep(1)
			print(" |  ¡Ven conmigo!                               |")
			print(" |                                              |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
			print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
			print("XXXXXXXXXX|[___][____]       |--|--|--|XXXXXXXXXX")
			print("XXXXXXXXXX|                  |__|__|__|XXXXXXXXXX")
			print("XXXXXXXXXX|              P            |XXXXXXXXXX")
			print("XXXXXXXXXX|                           |XXXXXXXXXX")
			print("XXXXXXXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
			print("XXXXXXXXXX|                           |XXXXXXXXXX")
			print("XXXXXXXXXX|                           |XXXXXXXXXX")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | ",enemigo1,": ¡Abuelo! ¡Estoy harto de   |")
			sleep(1)
			print(" |  esperar!                                    |")
			print(" |  OAK: ¿",enemigo1,"?                      |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
			print("XXXXX@-------------------------------@XXXXXXXXXX")
			print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
			print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
			print("XXXXX|              (OAK)            |XXXXXXXXXX")
			print("XXXXX|                               |XXXXXXXXXX")
			print("XXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
			print("XXXXX|                   |---------| |XXXXXXXXXX")
			print("XXXXX|                   |      O  | |XXXXXXXXXX")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | OAK: ¿Hum? ¿Qué haces aquí ya?               |")
			sleep(1)
			print(" |  Te dije que vinieras más  tarde...          |")
			sleep(1)
			print(" |  ¡No importa!    Espera ahí.                 |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
			print("XXXXX@-------------------------------@XXXXXXXXXX")
			print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
			print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
			print("XXXXX|              (OAK)            |XXXXXXXXXX")
			print("XXXXX|                               |XXXXXXXXXX")
			print("XXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
			print("XXXXX|                   |---------| |XXXXXXXXXX")
			print("XXXXX|                   |      O  | |XXXXXXXXXX")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | OAK: ¡Mira, ",jugador1,"! ¿Ves la bola que    |")
			sleep(1)
			print(" |  está en la mesa? Se llama POKéBALL.                           |")
			sleep(1)
			print(" |  Contiene un POKéMON en su interior.         |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
			print("XXXXX@-------------------------------@XXXXXXXXXX")
			print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
			print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
			print("XXXXX|              (OAK)            |XXXXXXXXXX")
			print("XXXXX|                               |XXXXXXXXXX")
			print("XXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
			print("XXXXX|                   |---------| |XXXXXXXXXX")
			print("XXXXX|                   |      O  | |XXXXXXXXXX")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | OAK: ¡Puedes cogerla!                        |")
			sleep(1)
			print(" |  ¡Es para ti!                                |")
			sleep(1)
			print(" |  ",enemigo1,": ¡Oye abuelo!                  |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
			print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
			print("XXXXX@-------------------------------@XXXXXXXXXX")
			print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
			print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
			print("XXXXX|              (OAK)            |XXXXXXXXXX")
			print("XXXXX|                               |XXXXXXXXXX")
			print("XXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
			print("XXXXX|                   |---------| |XXXXXXXXXX")
			print("XXXXX|                   |      O  | |XXXXXXXXXX")
			print(" @----------------------------------------------@")
			print(" |                                              |")
			sleep(2)
			print(" | ",enemigo1,": ¡Y yo! ¿qué?                  |")
			sleep(1)
			print(" |  OAK: ¡Tranquilo ",enemigo1,"! Te dare otro |                       |")
			sleep(1)
			print(" |  a ti mas tarde!                             |")
			print(" |                                         \\/   |")
			print(" @----------------------------------------------@")
			input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			while True:# no hay 'repetir' en python
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@-------------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|                               |XXXXXXXXXX")
				print("XXXXX|    (",enemigo1,")  (",jugador1,")          |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print(" @----------------------------------------------@")
				print(" |                                              |")
				sleep(2)
				print(" | OAK: ¡Adelante! ¡Es tuyo!                  |")
				print(" |                                              |")
				print(" |  (presiona 0 para obtener tu pokemon)        |")
				print(" |                                         \\/   |")
				print(" @----------------------------------------------@")
				opc4 = int(input())
				if opc4==0: break
			if opc4==0:
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@-------------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|       [!]                     |XXXXXXXXXX")
				print("XXXXX|    (",enemigo1,")           |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   (",jugador1," ) |XXXXXXXX")
				print(" @----------------------------------------------@")
				sleep(3)
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@---------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|                               |XXXXXXXXXX")
				print("XXXXX|                 (",jugador1,") |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                  (",enemigo1,")    |XXXXXXXX")
				print(" @----------------------------------------------@")
				print(" |                                              |")
				sleep(2)
				print(" | ",jugador1," ¡NO! ¡",enemigo1,", quiero a ese|")
				print(" |                                              |")
				print(" |  POKéMON!                                    |")
				print(" |           ",enemigo1," !Ha cogido el POKéMON!|")
				print(" @----------------------------------------------@")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@---------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|                               |XXXXXXXXXX")
				print("XXXXX|                 (",jugador1,") |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                  (",enemigo1,")    |XXXXXXXX")
				print(" @----------------------------------------------@")
				print(" |                                              |")
				print(" | OAK: ¡",enemigo1,"! ¿Que haces?       |")
				print(" | ",enemigo1," ¡Abuelo, yo quiero éste!        |")
				sleep(1)
				print(" | OAK: Pero... Bueno. Vale.                    |")
				print(" |           Ese POKéMON es tuyo.               |")
				print(" @----------------------------------------------@")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@---------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|                               |XXXXXXXXXX")
				print("XXXXX|                 (",jugador1,") |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                  (",enemigo1,")    |XXXXXXXX")
				print(" @----------------------------------------------@")
				print(" |                                              |")
				print(" | OAK: Te iba a dar uno de todos modos...      |")
				sleep(1)
				print(" |  ",jugador1,", ven aquí.                   |")
				print(" |                                              |")
				print(" |                                              |")
				print(" @----------------------------------------------@")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				print("XXXXXXXXXX     L A B O R A T O R I O  XXXXXXXXXXX")
				print("XXXXX@---------------------------@XXXXXXXXXX")
				print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
				print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
				print("XXXXX|              (OAK)            |XXXXXXXXXX")
				print("XXXXX|            (",jugador1,")    |XXXXXXXXXX")
				print("XXXXX|                               |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                   |      O  | |XXXXXXXXXX")
				print("XXXXX|                   |---------| |XXXXXXXXXX")
				print("XXXXX|                  (",enemigo1,")    |XXXXXXXX")
				print(" @----------------------------------------------@")
				print(" |                                              |")
				print(" | OAK: ",jugador1,", éste es el POKéMON que  |")
				print(" |  atrapé antes. Puedes tenerlo.               |")
				print(" |  Lo cogí en estado salvaje, asi que no es    |")
				print(" |  manso todavía.                              |")
				print(" @----------------------------------------------@")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
	if opc!=2:
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXX   L A B O R A T O R I O XXXXXXXXXXXXXXX")
		print("XXXXX@-------------------------------@XXXXXXXXXX")
		print("XXXXX|[___][____]        |--|--|--|--|XXXXXXXXXX")
		print("XXXXX|                   |__|__|__|__|XXXXXXXXXX")
		print("XXXXX|              (OAK)            |XXXXXXXXXX")
		print("XXXXX|            (",jugador1,")         |XXXXXXXXXX")
		print("XXXXX|                               |XXXXXXXXXX")
		print("XXXXX|                   |---------| |XXXXXXXXXX")
		print("XXXXX|                   |         | |XXXXXXXXXX")
		print("XXXXX|                   |---------| |XXXXXXXXXX")
		print("XXXXX|                  (",enemigo1,")O    |XXXXXXXX")
		print(" @----------------------------------------------@")
		print(" |                                              |")
		print(" | ",jugador1," !Has adquerido a PIKACHU!       |")
		print(" @----------------------------------------------@")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		# ***************************************************************
		# *******POKEMONES POR DEFECTO **********************************
		# ***************************************************************
		cantidadpoke = 1
		# USUARIO SE LE ASIGNA PIKACHU
		nombrepokemon[10] = "PIKACHU"
		pokemon[0] = "ELECTRICO"
		pokemon[1] = ""
		# Salud
		pokemon[2] = "35"
		pokemon[3] = "55"
		pokemon[4] = "30"
		pokemon[5] = "90"
		pokemon[6] = "50"
		# Guarda el nombre del pokemon 1 que voy a ocupar
		mipoke[0] = "PIKACHU"
		# TIPO DEL POKE
		# Guarda el Tipo 1 del pokemon
		mipoket1[0] = "ELECTRICO"
		# Guarda el Tipo 2
		mipoket1[1] = ""
		# Habilidad del poke 1
		# SALUD
		mipokeh1[0] = 35
		# ATAQUE
		mipokeh1[1] = 55
		# DEFENSA
		mipokeh1[2] = 30
		# VELOCIDAD
		mipokeh1[3] = 90
		# ESPECIAL  
		mipokeh1[4] = 50
		misalud[0] = mipokeh1[0]
		nombreataque[0] = "Puño Trueno"
		tipoataque[0] = mipoket1[0]
		pp[0] = "15"
		efectivo[0] = "100"
		dano[0] = "75"
		nombreataque[1] = "Trueno"
		tipoataque[1] = mipoket1[0]
		pp[1] = "15"
		efectivo[1] = "70"
		dano[1] = "120"
		nombreataque[2] = "Impactrueno"
		tipoataque[2] = mipoket1[0]
		pp[2] = "30"
		efectivo[2] = "100"
		dano[2] = "40"
		nombreataque[3] = "Rayo"
		tipoataque[3] = mipoket1[0]
		pp[3] = "15"
		efectivo[3] = "100"
		dano[3] = "95"
		# Guarda el pokemon 1 antes
		for contx in range(4):
			nombrea1[contx] = nombreataque[contx]
			tipoa1[contx] = tipoataque[contx]
			ppa1[contx] = float(pp[contx])
			ppfa1[contx] = float(pp[contx])
			efectivoa1[contx] = float(efectivo[contx])
			danoa1[contx] = float(dano[contx])
		# ***************************CPU SE LE ASIGNA EEVEE
		# Guarda el nombre del pokemon 1 que voy a ocupar
		enepoke[0] = "EEVEE"
		# TIPO DEL POKE
		# Guarda el Tipo 1 del pokemon
		enepoket1[0] = "NORMAL"
		# Guarda el Tipo 2
		enepoket1[1] = ""
		# Habilidad del poke 1
		# SALUD
		enepokeh1[0] = 55
		# ATAQUE
		enepokeh1[1] = 55
		# DEFENSA
		enepokeh1[2] = 50
		# VELOCIDAD
		enepokeh1[3] = 55
		# ESPECIAL 
		enepokeh1[4] = 65
		enesalud[0] = enepokeh1[0]
		nombreataque[0] = "Destructor"
		tipoataque[0] = pokemon[0]
		pp[0] = "35"
		efectivo[0] = "100"
		dano[0] = "40"
		nombreataque[1] = "Ataque Arena"
		tipoataque[1] = "TIERRA"
		pp[1] = "15"
		efectivo[1] = "100"
		dano[1] = "0"
		nombreataque[2] = "Doble Bofeton"
		tipoataque[2] = pokemon[0]
		pp[2] = "10"
		efectivo[2] = "85"
		dano[2] = "15"
		nombreataque[3] = "Placaje"
		tipoataque[3] = pokemon[0]
		pp[3] = "15"
		efectivo[3] = "100"
		dano[3] = "95"
		# Guarda el pokemon 1 antes
		for contx in range(4):
			nombree1[contx] = nombreataque[contx]
			tipoe1[contx] = tipoataque[contx]
			ppe1[contx] = float(pp[contx])
			ppfe1[contx] = float(pp[contx])
			efectivoe1[contx] = float(efectivo[contx])
			danoe1[contx] = float(dano[contx])
		# Niveles de los pokemones 
		while True:# no hay 'repetir' en python
			minivel[0] = randint(0,30)
			if minivel[0]>=25: break
		while True:# no hay 'repetir' en python
			enenivel[0] = randint(0,30)
			if enenivel[0]>=25: break
		# ***************************************************************
		# ********************JUEGO**************************************
		# ***************************************************************
		# Menu Principal
	if opc==1 or opc==4:
		while salir==False:
			while True:# no hay 'repetir' en python
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print("                       Exit                     ")
				print("°°°°°°°°°°°°°°°°°°°°°° [4] °°°°°°°°°°°°°°°°°°°°°")
				print("°         ______             _________         °")
				print("°        /------\\           /---------\\        °")
				print("°       | [_][_] |         | [__] _[_] |       °")
				print("°   [1] |_||_____|     [2] !_____| |___!       °")
				print("°                                              °")
				print("°                                              °")
				print("°    °°°°°°°[0]          _____________         °")
				print("°    ~v~v~v~    O       /             \\        °")
				print("°    v!v!v!v   -|-     /|_ _ _ _ _ _ _|\\       °")
				print("°           zO /l      \\/[][][] [][][]\\/       °")
				print("°                       | - - - - - - |        °")
				print("°     _______           |_RRRR_| |_RRR|        °")
				print("°    |///////|                                 °")
				print("°    |///////|          °°°°°°°°[3]°°°°        °")
				print("°°   |///////|°         v~~v~i~~v~i~v~         °")
				print("°°°°°°///////°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
				print(" @----------------------------------------------@")
				print(" |  0.- PUEBLO PALETA                           |")
				print(" |  1.- Casa de ",jugador1,"                         |")
				print(" |  2.- Casa de ",enemigo1,"                        |")
				print(" |  3.- LABORATORIO DE INVESTIGACIÓN  de POKéMON|")
				print(" |             del PROFESOR OAK                 |")
				print(" |  99.- Ayuda ¿?                               |")
				print(" @----------------------------------------------@")
				opc3 = int(input())
				if opc3==1 or opc3==2 or opc3==3 or opc3==4 or opc3==0 or opc3==99: break
			if opc3==0:
				print(" Pueblo Paleta ¡Un lienzo en blanco de tu viaje!")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			if opc3==99:
				print("") # no hay forma directa de borrar la pantalla con Python estandar
				print(" @----------------------------------------------@")
				print(" |  Ayuda                                       |")
				print(" |                                              |")
				print(" |                 Opcion 1                      |")
				print(" |        - Curar a todos tus pokemones         |")
				print(" |           - Ver tus victorias                |")
				print(" |                                              |")
				print(" |                 Opcion 2                      |")
				print(" |          Enfrentamiento 1vs Cpu              |")
				print(" |           - Batalla uno solo                 |")
				print(" |           - 6 Pokémon vs 6                   |")
				print(" |                                              |")
				print(" |                 Opcion 3                      |")
				print(" |            - Cambiar pokemon                 |")
				print(" |            - Reiniciar pp                    |")
				print(" |                                              |")
				print(" |                 Opcion 4                      |")
				print(" |           - Salir de juego                   |")
				print(" |                                              |")
				print(" |                                         \\/   |")
				print(" @----------------------------------------------@")
				input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			if opc3==1:
				while True:# no hay 'repetir' en python
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|   1.- CURAR POKEMONES     |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|   2.- VER VICTORIAS       |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX [3] Volver XXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("Eliga una opción :", end="")
					opc4 = int(input())
					if opc4==1 or opc4==2 or opc4==3: break
				if opc4==1:
					if cantidadpoke==1:
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("")
						print("SALUD DE LOS POKEMONES ACTUALES")
						print("")
						print(" Inventario ",jugador1)
						print("1.- ",mipoke[0],"  ",mipokeh1[0])
						print("")
						print("Inventario ",enemigo1)
						print("1.- ",enepoke[0],"  ",enepokeh1[0])
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						mipokeh1[0] = misalud[0]
						enepokeh1[0] = enesalud[0]
						print("")
						print("Curando a tus pokemon ...")
						sleep(2)
						print("")
						print("Se han curado tus pokemones")
						sleep(2)
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("")
						print(" V A  L O R E S     R E N O V A D O S ")
						print("")
						print(" Inventario ",jugador1)
						print("1.- ",mipoke[0],"  ",mipokeh1[0])
						print("")
						print("Inventario ",enemigo1)
						print("1.- ",enepoke[0],"  ",enepokeh1[0])
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					else:
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("")
						print("SALUD DE LOS POKEMONES ACTUALES")
						print("")
						print("Inventario ",jugador1)
						print("1.- ",mipoke[0],"  ",mipokeh1[0])
						print("2.- ",mipoke[1],"  ",mipokeh2[0])
						print("3.- ",mipoke[2],"  ",mipokeh3[0])
						print("4.- ",mipoke[3],"  ",mipokeh4[0])
						print("5.- ",mipoke[4],"  ",mipokeh5[0])
						print("6.- ",mipoke[5],"  ",mipokeh6[0])
						print("")
						print("Inventario ",enemigo1)
						print("1.- ",enepoke[0],"  ",enepokeh1[0])
						print("2.- ",enepoke[1],"  ",enepokeh2[0])
						print("3.- ",enepoke[2],"  ",enepokeh3[0])
						print("4.- ",enepoke[3],"  ",enepokeh4[0])
						print("5.- ",enepoke[4],"  ",enepokeh5[0])
						print("6.- ",enepoke[5],"  ",enepokeh6[0])
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						mipokeh1[0] = misalud[0]
						mipokeh2[0] = misalud[1]
						mipokeh3[0] = misalud[2]
						mipokeh4[0] = misalud[3]
						mipokeh5[0] = misalud[4]
						mipokeh6[0] = misalud[5]
						enepokeh1[0] = enesalud[0]
						enepokeh2[0] = enesalud[1]
						enepokeh3[0] = enesalud[2]
						enepokeh4[0] = enesalud[3]
						enepokeh5[0] = enesalud[4]
						enepokeh6[0] = enesalud[5]
						print("")
						print("Curando a tus pokemon")
						sleep(2)
						print("")
						print("Se han curado tus pokemones")
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print(" V A  L O R E S     R E N O V A D O S ")
						print("")
						print("SALUD DE LOS POKEMONES ACTUALES")
						print("")
						print("Inventario ",jugador1)
						print("1.- ",mipoke[0],"  ",mipokeh1[0])
						print("2.- ",mipoke[1],"  ",mipokeh2[0])
						print("3.- ",mipoke[2],"  ",mipokeh3[0])
						print("4.- ",mipoke[3],"  ",mipokeh4[0])
						print("5.- ",mipoke[4],"  ",mipokeh5[0])
						print("6.- ",mipoke[5],"  ",mipokeh6[0])
						print("")
						print("Inventario ",enemigo1)
						print("1.- ",enepoke[0],"  ",enepokeh1[0])
						print("2.- ",enepoke[1],"  ",enepokeh2[0])
						print("3.- ",enepoke[2],"  ",enepokeh3[0])
						print("4.- ",enepoke[3],"  ",enepokeh4[0])
						print("5.- ",enepoke[4],"  ",enepokeh5[0])
						print("6.- ",enepoke[5],"  ",enepokeh6[0])
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
				if opc4==2:
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|    V I C T O R I A S      |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|         ",win,"               |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			# *************************************************************BATALLAS OPCION 2**********************************
			# *************************************************************BATALLAS OPCION 2**********************************
			# *************************************************************BATALLAS OPCION 2**********************************
			# ASignar pokemones al invertario 
			# ASignar pokemones al invertario 
			if opc3==2:
				if mipoke[0]!="":
					while True:# no hay 'repetir' en python
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("CASA DE ",enemigo1)
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
						print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
						print("XXXXXXXXXX|       B A T A L L A       |XXXXXXXXXX")
						print("XXXXXXXXXX|                           |XXXXXXXXXX")
						print("XXXXXXXXXX|   1.- 1 V/s 1             |XXXXXXXXXX")
						print("XXXXXXXXXX|                           |XXXXXXXXXX")
						print("XXXXXXXXXX|                           |XXXXXXXXXX")
						print("XXXXXXXXXX|   2.- Duelo 6 POKéMON     |XXXXXXXXXX")
						print("XXXXXXXXXX|                           |XXXXXXXXXX")
						print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX [3] Volver XXXXXX")
						print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
						print("Eliga una opción :", end="")
						opc6 = int(input())
						if opc6==1 or opc6==2 or opc6==3: break
					# ********************************************************************
					# ******************COMBATE 1VS1 *************************************
					# ********************************************************************
					if cantidadpoke==1:
						totalsalud = mipokeh1[0]
						enetotalsalud = enepokeh1[0]
					if cantidadpoke==6:
						totalsalud = mipokeh1[0]+mipokeh2[0]+mipokeh3[0]+mipokeh4[0]+mipokeh5[0]+mipokeh6[0]
						enetotalsalud = enepokeh1[0]+enepokeh2[0]+enepokeh3[0]+enepokeh4[0]+enepokeh5[0]+enepokeh6[0]
					if cantidadpoke==1:
						if totalsalud==0:
							print("Ve de inmediato a curar a tu Pokémon")
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						if enetotalsalud==0 and totalsalud>0:
							print("El Pokémon de ",enemigo1," está debilidato. ")
							print("Ve a Curar a tu Pikachu y curaras al EEVEE de ",enemigo1)
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					if cantidadpoke==6:
						if totalsalud==0:
							print("Ve de inmediato a curar a tus Pokémon")
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						if enetotalsalud==0 and totalsalud>0:
							print("Los Pokémon de ",enemigo1," estan debilidatos")
							print("Ve a Curar los tuyos y curaras lo de el tambien")
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						if enetotalsalud>0 and totalsalud==0:
							print("¡",jugador1,"Tus Pokémon estan debilidatos!")
							print("Ve a curarlos a tu casa")
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					if opc6==2:
						if cantidadpoke==6:
							if (mipokeh1[0]>0 and mipokeh2[0]>0 and mipokeh3[0]>0 and mipokeh4[0]>0 and mipokeh5[0]>0 and mipokeh6[0]>0) and (enepokeh1[0]>0 and enepokeh2[0]>0 and enepokeh3[0]>0 and enepokeh4[0]>0 and enepokeh5[0]>0 and enepokeh6[0]>0):
								micontwin = 0
								enecontwin = 0
							else:
								micontwin = 7
								enecontwin = 7
					while (opc6==1 or opc6==2) and (totalsalud>0 and enetotalsalud>0):
						if opc6==1 and cantidadpoke==1:
							while True:# no hay 'repetir' en python
								print("") # no hay forma directa de borrar la pantalla con Python estandar
								print("")
								print("       ¿Que pokemon vas a usar?")
								print("")
								print("Lista de tus pokemones            |   Lista de los pokemones enemigos ")
								print("             Nivel                            Nivel")
								print("1.- ",mipoke[0],"  ",minivel[0],"            |          ",enepoke[0],"  ",enenivel[0])
								print("")
								print("")
								print("                                                       Opcion 0 VOLVER ")
								opcmipoke = int(input())
								start = True
								if opcmipoke==1 or opcmipoke==0: break
						if opc6==1 and cantidadpoke==6:
							while True:# no hay 'repetir' en python
								for contx in range(12):
									life[contx] = "O"
								if mipokeh1[0]<=0:
									life[0] = "X"
								if mipokeh2[0]<=0:
									life[1] = "X"
								if mipokeh3[0]<=0:
									life[2] = "X"
								if mipokeh4[0]<=0:
									life[3] = "X"
								if mipokeh5[0]<=0:
									life[4] = "X"
								if mipokeh6[0]<=0:
									life[5] = "X"
								if enepokeh1[0]<=0:
									life[6] = "X"
								if enepokeh2[0]<=0:
									life[7] = "X"
								if enepokeh3[0]<=0:
									life[8] = "X"
								if enepokeh4[0]<=0:
									life[9] = "X"
								if enepokeh5[0]<=0:
									life[10] = "X"
								if enepokeh6[0]<=0:
									life[11] = "X"
								print("") # no hay forma directa de borrar la pantalla con Python estandar
								print("")
								print("Que pokemon vas a usar                 (O=Diponible , X= Debilitado)")
								print("")
								print("Lista de tus pokemones            |   Lista de los pokemones enemigos ")
								print("          Nivel        Estado                   Nivel       Estado")
								print("1.- ",mipoke[0],"  ",minivel[0],"     ",life[0],"        |          ",enepoke[0],"  ",enenivel[0],"     ",life[6])
								print("2.- ",mipoke[1],"  ",minivel[1],"     ",life[1],"        |          ",enepoke[1],"  ",enenivel[1],"     ",life[7])
								print("3.- ",mipoke[2],"  ",minivel[2],"     ",life[2],"        |          ",enepoke[2],"  ",enenivel[2],"     ",life[8])
								print("4.- ",mipoke[3],"  ",minivel[3],"     ",life[3],"        |          ",enepoke[3],"  ",enenivel[3],"     ",life[9])
								print("5.- ",mipoke[4],"  ",minivel[4],"     ",life[4],"        |          ",enepoke[4],"  ",enenivel[4],"     ",life[10])
								print("6.- ",mipoke[5],"  ",minivel[5],"     ",life[5],"        |          ",enepoke[5],"  ",enenivel[5],"     ",life[11])
								print("")
								print("")
								print("                                                  Opción 0 VOLVER")
								opcmipoke = int(input())
								start = True
								if opcmipoke==1 and mipokeh1[0]==0:
									print("Pokémon ",mipoke[0]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==2 and mipokeh2[0]==0:
									print("Pokémon ",mipoke[1]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==3 and mipokeh3[0]==0:
									print("Pokémon ",mipoke[2]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==4 and mipokeh4[0]==0:
									print("Pokémon ",mipoke[3]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==5 and mipokeh5[0]==0:
									print("Pokémon ",mipoke[4]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==6 and mipokeh6[0]==0:
									print("Pokémon ",mipoke[5]," debilitado, ve al laboratorio para Curarlo")
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcmipoke==1 and mipokeh1[0]>0 or opcmipoke==2 and mipokeh2[0]>0 or opcmipoke==3 and mipokeh3[0]>0 or opcmipoke==4 and mipokeh4[0]>0 or opcmipoke==5 and mipokeh5[0]>0 or opcmipoke==6 and mipokeh6[0]>0 or opcmipoke==0: break
						# ****************************************************************************************
						# ****************************************************************************************
						if opc6==2:
							if cantidadpoke==6 and micontwin<=5 and enecontwin<=5:
								while True:# no hay 'repetir' en python
									for contx in range(12):
										life[contx] = "O"
									if mipokeh1[0]<=0:
										life[0] = "X"
									if mipokeh2[0]<=0:
										life[1] = "X"
									if mipokeh3[0]<=0:
										life[2] = "X"
									if mipokeh4[0]<=0:
										life[3] = "X"
									if mipokeh5[0]<=0:
										life[4] = "X"
									if mipokeh6[0]<=0:
										life[5] = "X"
									if enepokeh1[0]<=0:
										life[6] = "X"
									if enepokeh2[0]<=0:
										life[7] = "X"
									if enepokeh3[0]<=0:
										life[8] = "X"
									if enepokeh4[0]<=0:
										life[9] = "X"
									if enepokeh5[0]<=0:
										life[10] = "X"
									if enepokeh6[0]<=0:
										life[11] = "X"
									if life[0]=="O" and life[1]=="O" and life[2]=="O" and life[3]=="O" and life[4]=="O" and life[5]=="O" and life[6]=="O" and life[7]=="O" and life[8]=="O" and life[9]=="O" and life[10]=="O" and life[11]=="O":
										print("") # no hay forma directa de borrar la pantalla con Python estandar
										print("")
										print("")
										print("")
										print("###################################################################")
										print("##                                                               ##")
										print("##                  B A T A L L A     6 vs 6                     ##")
										print("##                                                               ##")
										print("##               ",jugador1)
										print("##                         v/S                                   ##")
										print("##                              ",enemigo1)
										print("###################################################################")
										print("")
										print("")
										print("                                                         Cargando...")
										sleep(5)
									print("") # no hay forma directa de borrar la pantalla con Python estandar
									print("")
									print("Que pokemon vas a usar                 (O=Diponible , X= Debilitado)")
									print("")
									print("          ",jugador1," : win ",micontwin," / ",enemigo1," : win ",enecontwin)
									print("")
									print("Lista de tus pokemones            |   Lista de los pokemones enemigos ")
									print("           Nivel              Estado                    Nivel           Estado")
									print("1.- ",mipoke[0],"  ",minivel[0],"     ",life[0],"        |          ",enepoke[0],"  ",enenivel[0],"     ",life[6])
									print("2.- ",mipoke[1],"  ",minivel[1],"     ",life[1],"        |          ",enepoke[1],"  ",enenivel[1],"     ",life[7])
									print("3.- ",mipoke[2],"  ",minivel[2],"     ",life[2],"        |          ",enepoke[2],"  ",enenivel[2],"     ",life[8])
									print("4.- ",mipoke[3],"  ",minivel[3],"     ",life[3],"        |          ",enepoke[3],"  ",enenivel[3],"     ",life[9])
									print("5.- ",mipoke[4],"  ",minivel[4],"     ",life[4],"        |          ",enepoke[4],"  ",enenivel[4],"     ",life[10])
									print("6.- ",mipoke[5],"  ",minivel[5],"     ",life[5],"        |          ",enepoke[5],"  ",enenivel[5],"     ",life[11])
									print("")
									print("")
									print("                                                  Opción 0 VOLVER")
									opcmipoke = int(input())
									start = True
									if opcmipoke==1 and mipokeh1[0]==0:
										print("Pokémon ",mipoke[0]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==2 and mipokeh2[0]==0:
										print("Pokémon ",mipoke[1]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==3 and mipokeh3[0]==0:
										print("Pokémon ",mipoke[2]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==4 and mipokeh4[0]==0:
										print("Pokémon ",mipoke[3]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==5 and mipokeh5[0]==0:
										print("Pokémon ",mipoke[4]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==6 and mipokeh6[0]==0:
										print("Pokémon ",mipoke[5]," debilitado, ve al laboratorio para Curarlo")
										input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
									if opcmipoke==1 and mipokeh1[0]>0 or opcmipoke==2 and mipokeh2[0]>0 or opcmipoke==3 and mipokeh3[0]>0 or opcmipoke==4 and mipokeh4[0]>0 or opcmipoke==5 and mipokeh5[0]>0 or opcmipoke==6 and mipokeh6[0]>0 or opcmipoke==0: break
							else:
								if cantidadpoke==1:
									print(jugador1," tienes que tener 6 Pokémon para poder jugar")
									sleep(2)
								if cantidadpoke==6:
									print(jugador1,"¡Los pokemones no tienen toda sus vidas!")
									sleep(3)
								opcmipoke = 0
								mihp = False
								enehp = False
								opc6 = 3
						if opcmipoke==0:
							opc6 = 3
							start = False
							mihp = False
							enehp = False
						if start==True:
							# SE CREA UNA NUEVA VARIABLE
							if opcmipoke==1:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[0]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket1[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket1[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh1[0]
								# ATAQUE
								miataquepoke = mipokeh1[1]
								# DEFENSA
								midefensapoke = mipokeh1[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh1[3]
								# ESPECIAL 
								miespecialpoke = mipokeh1[4]
								# Ingresar los datos siguientes 
								for pos in range(4):
									minombreataque[pos] = nombrea1[pos]
									mitipoa[pos] = tipoa1[pos]
									mipp[pos] = ppa1[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa1[pos]
									midano[pos] = danoa1[pos]
								# Se mostrara en el marcador
								misaludfija = mipokeh1[0]
								milvl = minivel[0]
							if opcmipoke==2:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[1]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket2[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket2[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh2[0]
								# ATAQUE
								miataquepoke = mipokeh2[1]
								# DEFENSA
								midefensapoke = mipokeh2[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh2[3]
								# ESPECIAL 
								miespecialpoke = mipokeh2[4]
								for pos in range(4):
									minombreataque[pos] = nombrea2[pos]
									mitipoa[pos] = tipoa2[pos]
									mipp[pos] = ppa2[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa2[pos]
									midano[pos] = danoa2[pos]
								# Se mostrara en el marcador
								misaludfija = mipokeh2[0]
								milvl = minivel[1]
							if opcmipoke==3:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[2]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket3[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket3[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh3[0]
								# ATAQUE
								miataquepoke = mipokeh3[1]
								# DEFENSA
								midefensapoke = mipokeh3[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh3[3]
								# ESPECIAL 
								miespecialpoke = mipokeh3[4]
								for pos in range(4):
									minombreataque[pos] = nombrea3[pos]
									mitipoa[pos] = tipoa3[pos]
									mipp[pos] = ppa3[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa3[pos]
									midano[pos] = danoa3[pos]
								# Se mostrara en el marcador
								misaludfija = mipokeh3[0]
								milvl = minivel[2]
							if opcmipoke==4:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[3]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket4[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket4[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh4[0]
								# ATAQUE
								miataquepoke = mipokeh4[1]
								# DEFENSA
								midefensapoke = mipokeh4[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh4[3]
								# ESPECIAL
								miespecialpoke = mipokeh4[4]
								for pos in range(4):
									minombreataque[pos] = nombrea4[pos]
									mitipoa[pos] = tipoa4[pos]
									mipp[pos] = ppa4[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa4[pos]
									midano[pos] = danoa4[pos]
								# Se mostrara en el marcador
								misaludfija = mipokeh4[0]
								milvl = minivel[3]
							if opcmipoke==5:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[4]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket5[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket5[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh5[0]
								# ATAQUE
								miataquepoke = mipokeh5[1]
								# DEFENSA
								midefensapoke = mipokeh5[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh5[3]
								# ESPECIAL
								miespecialpoke = mipokeh5[4]
								for pos in range(4):
									minombreataque[pos] = nombrea5[pos]
									mitipoa[pos] = tipoa5[pos]
									mipp[pos] = ppa5[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa5[pos]
									midano[pos] = danoa5[pos]
								milvl = minivel[4]
								# Se mostrara en el marcador
								misaludfija = mipokeh5[0]
							if opcmipoke==6:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								minombrepoke = mipoke[5]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								mitipo[0] = mipoket6[0]
								# Guarda el Tipo 2
								mitipo[1] = mipoket6[1]
								# Habilidad del poke 1
								# SALUD
								misaludpoke = mipokeh6[0]
								# ATAQUE
								miataquepoke = mipokeh6[1]
								# DEFENSA
								midefensapoke = mipokeh6[2]
								# VELOCIDAD
								mivelocidadpoke = mipokeh6[3]
								# ESPECIAL 
								miespecialpoke = mipokeh6[4]
								for pos in range(4):
									minombreataque[pos] = nombrea6[pos]
									mitipoa[pos] = tipoa6[pos]
									mipp[pos] = ppa6[pos]
									# Se mostrara en el marcador
									mifijopp[pos] = ppfa6[pos]
									midano[pos] = danoa6[pos]
								# Se mostrara en el marcador
								misaludfija = mipokeh6[0]
								milvl = minivel[5]
							# ***************************************** 1vs1 eleccion enemiga **************************
							if cantidadpoke==1:
								eneazar = 1
							else:
								while True:# no hay 'repetir' en python
									eneazar = randint(0,6)
									if eneazar==1 and enepokeh1[0]>0 or eneazar==2 and enepokeh2[0]>0 or eneazar==3 and enepokeh3[0]>0 or eneazar==4 and enepokeh4[0]>0 or eneazar==5 and enepokeh5[0]>0 or eneazar==6 and enepokeh6[0]>0: break
							if eneazar==1:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[0]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket1[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket1[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh1[0]
								# ATAQUE
								eneataquepoke = enepokeh1[1]
								# DEFENSA
								enedefensapoke = enepokeh1[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh1[3]
								# ESPECIAL 
								eneespecialpoke = enepokeh1[4]
								for pos in range(4):
									enenombreataque[pos] = nombree1[pos]
									enetipoa[pos] = tipoe1[pos]
									enepp[pos] = ppe1[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe1[pos]
									enedano[pos] = danoe1[pos]
								enelvl = enenivel[0]
								# Se mostrara en el marcador
								enesaludfija = enepokeh1[0]
							if eneazar==2:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[1]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket2[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket2[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh2[0]
								# ATAQUE
								eneataquepoke = enepokeh2[1]
								# DEFENSA
								enedefensapoke = enepokeh2[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh2[3]
								# ESPECIAL 
								eneespecialpoke = enepokeh2[4]
								for pos in range(4):
									enenombreataque[pos] = nombree2[pos]
									enetipoa[pos] = tipoe2[pos]
									enepp[pos] = ppe2[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe2[pos]
									enedano[pos] = danoe2[pos]
								enelvl = enenivel[1]
								# Se mostrara en el marcador
								enesaludfija = enepokeh2[0]
							if eneazar==3:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[2]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket3[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket3[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh3[0]
								# ATAQUE
								eneataquepoke = enepokeh3[1]
								# DEFENSA
								enedefensapoke = enepokeh3[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh3[3]
								# ESPECIAL 
								eneespecialpoke = enepokeh3[4]
								for pos in range(4):
									enenombreataque[pos] = nombree3[pos]
									enetipoa[pos] = tipoe3[pos]
									enepp[pos] = ppe3[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe3[pos]
									enedano[pos] = danoe3[pos]
								enelvl = enenivel[2]
								# Se mostrara en el marcador
								enesaludfija = enepokeh3[0]
							if eneazar==4:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[3]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket4[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket4[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh4[0]
								# ATAQUE
								eneataquepoke = enepokeh4[1]
								# DEFENSA
								enedefensapoke = enepokeh4[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh4[3]
								# ESPECIAL 
								eneespecialpoke = enepokeh4[4]
								for pos in range(4):
									enenombreataque[pos] = nombree4[pos]
									enetipoa[pos] = tipoe4[pos]
									enepp[pos] = ppe4[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe4[pos]
									enedano[pos] = danoe4[pos]
								enelvl = enenivel[3]
								# Se mostrara en el marcador
								enesaludfija = enepokeh4[0]
							if eneazar==5:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[4]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket5[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket5[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh5[0]
								# ATAQUE
								eneataquepoke = enepokeh5[1]
								# DEFENSA
								enedefensapoke = enepokeh5[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh5[3]
								# ESPECIAL
								eneespecialpoke = enepokeh5[4]
								for pos in range(4):
									enenombreataque[pos] = nombree5[pos]
									enetipoa[pos] = tipoe5[pos]
									enepp[pos] = ppe5[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe5[pos]
									enedano[pos] = danoe5[pos]
								enelvl = enenivel[4]
								# Se mostrara en el marcador
								enesaludfija = enepokeh5[0]
							if eneazar==6:
								# Guarda el nombre del pokemon 1 que voy a ocupar
								enenombrepoke = enepoke[5]
								# TIPO DEL POKE
								# Guarda el Tipo 1 del pokemon
								enetipo[0] = enepoket6[0]
								# Guarda el Tipo 2
								enetipo[1] = enepoket6[1]
								# Habilidad del poke 1
								# SALUD
								enesaludpoke = enepokeh6[0]
								# ATAQUE
								eneataquepoke = enepokeh6[1]
								# DEFENSA
								enedefensapoke = enepokeh6[2]
								# VELOCIDAD
								enevelocidadpoke = enepokeh6[3]
								# ESPECIAL 
								eneespecialpoke = enepokeh6[4]
								for pos in range(4):
									enenombreataque[pos] = nombree6[pos]
									enetipoa[pos] = tipoe6[pos]
									enepp[pos] = ppe6[pos]
									# Se mostrara en el marcador
									enefijopp[pos] = ppfe6[pos]
									enedano[pos] = danoe6[pos]
								enelvl = enenivel[5]
								# Se mostrara en el marcador
								enesaludfija = enepokeh6[0]
							if opcmipoke==0:
								mihp = False
								enehp = False
							if opcmipoke!=0:
								# Primera Batalla :3 27/06/2016 Despues de dos semanas por fin llegando casi al final :3 by Benjamin Mora
								# ------------------------------------------------------------------------------------
								# **********************************Subir Por nivel***********************************
								# ------------------------------------------------------------------------------------
								eneaumento = enelvl*(enedefensapoke*0.2)
								miaumento = milvl*(midefensapoke*0.3)
								midefensapoke = midefensapoke+miaumento
								enedefensapoke = enedefensapoke+eneaumento
								enehp = False
								mihp = False
								if enesaludpoke<=0:
									enesaludpoke = 0
									enesaludfija = enesaludpoke
									print("Pokémon enemigo bajo de vida")
									sleep(2)
								else:
									enesaludpoke = enesaludpoke+((enelvl-1)*3)
									enesaludfija = enesaludpoke
									enehp = True
								if misaludpoke<=0:
									misaludpoke = 0
									misaludfija = misaludpoke
									print("Pokémon Bajo de vida ",jugador1)
									sleep(2)
								else:
									misaludpoke = misaludpoke+((milvl-1)*3)
									misaludfija = misaludpoke
									mihp = True
								# miSaludPoke=10000000;
								# eneSaludPoke=10000000;
								miaumento = 0
								eneaumento = 0
								for v in range(milvl+1):
									miaumento = miaumento+randint(0,2)
								for v in range(enelvl+1):
									eneaumento = eneaumento+randint(0,2)
								mivelocidadpoke = mivelocidadpoke+miaumento
								enevelocidadpoke = enevelocidadpoke+eneaumento
								# *****************************************************************
								if mihp==True and enehp==True:
									print("") # no hay forma directa de borrar la pantalla con Python estandar
									print("                                            ")
									print("|----------------------")
									print("| ")
									print("|    ")
									print("|    ")
									print("|----------------------")
									print("")
									print("")
									print("")
									print("")
									print("")
									print("                             |-----------------")
									print("                             | ")
									print("                             |       ")
									print("                             | ")
									print("                             |-----------------")
									print("°------------------------------------------------°")
									print("|   ",enemigo1," Envió a ",enenombrepoke)
									print("|   ")
									print("°------------------------------------------------°")
									sleep(2)
						while mihp==True and enehp==True:
							# Visual grafico
							while True:# no hay 'repetir' en python
								print("") # no hay forma directa de borrar la pantalla con Python estandar
								print("                                 0 = Pokédex (Ayuda)")
								print("|----------------------")
								print("| ",enenombrepoke)
								print("|              Nv ",enelvl)
								print("|    Ps: ",enesaludpoke,"                        ________ ")
								print("|----------------------            \\/    \\/ ")
								print("                                   / ^  ^ \\ ")
								print("                                   I\\____/I ")
								print("                                  /_\\    /_\\  ")
								print("       ________                     |    |")
								print("       \\/    \\/                    /_\\__/_\\ ")
								print("       /  ^^  \\              |-----------------")
								print("      I   ^^   I             | ",minombrepoke)
								print("     /_\\      /_\\            |        Nv ",milvl)
								print("       |      |              | Ps : ",misaludpoke,"/",misaludfija)
								print("      /_\\____/_\\             |-----------------")
								print("°------------------------------------------------°")
								print("|   [1]",minombreataque[0],"(",mipp[0],"/",mifijopp[0],")        [2]",minombreataque[1],"(",mipp[1],"/",mifijopp[1],")")
								print("|   [3]",minombreataque[2],"(",mipp[2],"/",mifijopp[2],")        [4]",minombreataque[3],"(",mipp[3],"/",mifijopp[3],")")
								print("°------------------------------------------------°")
								opcionataque = int(input())
								if opcionataque==0:
									print("") # no hay forma directa de borrar la pantalla con Python estandar
									print("")
									print("         P O K E D E X - R E S U M E N")
									print("",enemigo1)
									print("Pokemon Enemigo :",enenombrepoke," Nivel ",enelvl)
									print("         Tipo pokemon: ",enetipo[0],"/",enetipo[1],"    Ps: ",enesaludpoke)
									print("                        Defensa: ",enedefensapoke,"  Velocidad: ",enevelocidadpoke)
									print("ATAQUES Pokémon")
									print("1.- ",enenombreataque[0]," | Tipo : ",enetipoa[0]," | pp : ",enepp[0],"  daño: ",enedano[0])
									print("2.- ",enenombreataque[1]," | Tipo : ",enetipoa[1]," | pp : ",enepp[1],"  daño: ",enedano[1])
									print("3.- ",enenombreataque[2]," | Tipo : ",enetipoa[2]," | pp : ",enepp[2],"  daño: ",enedano[2])
									print("4.- ",enenombreataque[3]," | Tipo : ",enetipoa[3]," | pp : ",enepp[3],"  daño: ",enedano[3])
									print("")
									print("",jugador1)
									print("Nombre Pokémon:",minombrepoke," Nivel ",milvl)
									print("         Tipo pokemon: ",mitipo[0],"/",mitipo[1],"      Ps: ",misaludpoke)
									print("                          Defensa: ",midefensapoke,"  Velocidad: ",mivelocidadpoke)
									print("ATAQUES Pokémon")
									print("1.- ",minombreataque[0]," | Tipo : ",mitipoa[0]," | pp : ",mipp[0],"  daño: ",midano[0])
									print("2.- ",minombreataque[1]," | Tipo : ",mitipoa[1]," | pp : ",mipp[1],"  daño: ",midano[1])
									print("3.- ",minombreataque[2]," | Tipo : ",mitipoa[2]," | pp : ",mipp[2],"  daño: ",midano[2])
									print("4.- ",minombreataque[3]," | Tipo : ",mitipoa[3]," | pp : ",mipp[3],"  daño: ",midano[3])
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcionataque==1 and mipp[0]==0:
									print("No tienes pp para hacer el ataque ",mitipoa[0])
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcionataque==2 and mipp[1]==0:
									print("No tienes pp para hacer el ataque ",mitipoa[1])
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcionataque==3 and mipp[2]==0:
									print("No tienes pp para hacer el ataque ",mitipoa[2])
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcionataque==4 and mipp[3]==0:
									print("No tienes pp para hacer el ataque ",mitipoa[3])
									input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
								if opcionataque==1 and mipp[0]>0 or opcionataque==2 and mipp[1]>0 or opcionataque==3 and mipp[2]>0 or opcionataque==4 and mipp[3]>0: break
							if paralizadoa==True:
								opcionataque = 99
							if opcionataque==99:
								miataque = ""
								mipoderataque = 0
								mitipoa[0] = ""
								mitipoa[1] = ""
								mitipo[0] = ""
								mitipo[1] = ""
								b = 0
								ataquepoke = 0
								tipoe = ""
								mipp = 0
							# *************** OPCION DE ATAQUE **********************
							b = 1
							# ****  U S U A R I O *************
							if opcionataque==1:
								# Se guarda el primer nombre
								miataque = minombreataque[0]
								mipoderataque = midano[0]
								# bono
								if mitipoa[0]==mitipo[0] or mitipoa[0]==mitipo[1]:
									b = 1.5
								if mitipoa[0]!="NORMAL":
									ataquepoke = miespecialpoke
								else:
									ataquepoke = miataquepoke
								# Asginacion de efectividad
								tipoe = mitipoa[0]
								mipp[0] = mipp[0]-1
							if opcionataque==2:
								# Se guarda el primer nombre
								miataque = minombreataque[1]
								mipoderataque = midano[1]
								# Bono
								if mitipoa[1]==mitipo[0] or mitipoa[1]==mitipo[1]:
									b = 1.5
								if mitipoa[1]!="NORMAL":
									ataquepoke = miespecialpoke
								else:
									ataquepoke = miataquepoke
								# Asginacion de efectividad
								tipoe = mitipoa[1]
								mipp[1] = mipp[1]-1
							if opcionataque==3:
								# Se guarda el primer nombre
								miataque = minombreataque[2]
								mipoderataque = midano[2]
								# Bono  
								if mitipoa[2]==mitipo[0] or mitipoa[2]==mitipo[1]:
									b = 1.5
								if mitipoa[2]!="NORMAL":
									ataquepoke = miespecialpoke
								else:
									ataquepoke = miataquepoke
								# Asginacion de efectividad
								tipoe = mitipoa[2]
								mipp[2] = mipp[2]-1
							if opcionataque==4:
								# Se guarda el primer nombre
								miataque = minombreataque[3]
								mipoderataque = midano[3]
								# Bono
								if mitipoa[3]==mitipo[0] or mitipoa[3]==mitipo[1]:
									b = 1.5
								if mitipoa[3]!="NORMAL":
									ataquepoke = miespecialpoke
								else:
									ataquepoke = miataquepoke
								# Asginacion de efectividad
								tipoe = mitipoa[3]
								mipp[3] = mipp[3]-1
							# Variacion 
							while True:# no hay 'repetir' en python
								v = randint(0,100)
								if v==85 or v==100: break
							# Efectividad 0.025 , 0.5 , 1 , 2 y 4
							# SOLO POR QUE TIENEN X, #, 0, porque los que tienen 1 estan por defecto en el caso si no dentran al algoritmo de abajo
							mie = 1
							suerte = randint(0,100)
							if tipoe=="AGUA":
								if enetipo[0]=="AGUA" or enetipo[1]=="AGUA" or enetipo[0]=="DRAGON" or enetipo[1]=="DRAGON" or enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA":
									mie = 0.5
								if enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="ROCA" or enetipo[1]=="ROCA" or enetipo[0]=="TIERRA" or enetipo[1]=="TIERRA":
									mie = 2
							if tipoe=="BICHO":
								if enetipo[0]=="FANTASMA" or enetipo[1]=="FANTASMA" or enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="LUCHA" or enetipo[1]=="LUCHA" or enetipo[0]=="VENENO" or enetipo[1]=="VENENO":
									mie = 0.5
								if enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA" or enetipo[0]=="PSIQUICO" or enetipo[1]=="PSIQUICO":
									mie = 0
							if tipoe=="DRAGON":
								if enetipo[0]==tipoe or enetipo[1]==tipoe:
									mie = 2
							if tipoe=="ELECTRICO":
								if enetipo[0]=="DRAGON" or enetipo[1]=="DRAGON" or enetipo[0]=="ELECTRICO" or enetipo[1]=="ELECTRICO" or enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA":
									mie = 0.5
								if enetipo[0]=="ELECTRICO" or enetipo[1]=="ELECTRICO" or enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 2
								if enetipo[0]=="TIERRA" or enetipo[0]=="TIERRA":
									mie = 0
							if tipoe=="FANTASMA":
								if enetipo[0]=="FANTASMA" or enetipo[1]=="FANTASMA":
									mie = 2
								if enetipo[0]=="NORMAL" or enetipo[0]=="NORMAL":
									mie = 0
							if tipoe=="FUEGO":
								if enetipo[0]=="AGUA" or enetipo[1]=="AGUA" or enetipo[0]=="DRAGON" or enetipo[1]=="DRAGON" or enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="ROCA" or enetipo[1]=="ROCA":
									mie = 0.5
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="HIELO" or enetipo[1]=="HIELO" or enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA":
									mie = 2
							if tipoe=="HIELO":
								if enetipo[0]=="AGUA" or enetipo[1]=="AGUA" or enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="HIELO" or enetipo[1]=="HIELO":
									mie = 0.5
								if enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA" or enetipo[0]=="TIERRA" or enetipo[1]=="TIERRA" or enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 2
							if tipoe=="LUCHA":
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="PSIQUICO" or enetipo[1]=="PSIQUICO" or enetipo[0]=="VENENO" or enetipo[1]=="VENENO" or enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 0.5
								if enetipo[0]=="HIELO" or enetipo[1]=="HIELO" or enetipo[0]=="NOMRAL" or enetipo[1]=="NORMAL" or enetipo[0]=="ROCA" or enetipo[0]=="ROCA":
									mie = 2
								if enetipo[0]=="FANTASMA" or enetipo[0]=="FANTASMA":
									mie = 0
							if tipoe=="NORMAL":
								if enetipo[0]=="FANTASMA" or enetipo[1]=="FANTASMA":
									mie = 0
							if tipoe=="PLANTA":
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="PLANTA" or enetipo[1]=="PLANTA" or enetipo[0]=="VENENO" or enetipo[1]=="VENENO" or enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 0.5
								if enetipo[0]=="AGUA" or enetipo[1]=="AGUA" or enetipo[0]=="ROCA" or enetipo[1]=="ROCA" or enetipo[0]=="TIERRA" or enetipo[1]=="TIERRA":
									mie = 2
							if tipoe=="PSIQUICO":
								if enetipo[0]=="PSIQUICO" or enetipo[1]=="PSIQUICO":
									mie = 0.5
								if enetipo[0]=="LUCHA" or enetipo[1]=="LUCHA" or enetipo[0]=="VENENO" or enetipo[0]=="VENENO":
									mie = 2
							if tipoe=="ROCA":
								if enetipo[0]=="LUCHA" or enetipo[1]=="LUCHA" or enetipo[0]=="TIERRA" or enetipo[1]=="TIERRA":
									mie = 0.5
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="FUEGO" or enetipo[1]=="FUEGO" or enetipo[0]=="HIELO" or enetipo[1]=="HIELO" or enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 2
							if tipoe=="TIERRA":
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="PLANTA" or enetipo[0]=="PLANTA":
									mie = 0.5
								if enetipo[0]=="ELECTRICO" or enetipo[1]=="ELECTRICO" or enetipo[0]=="ROCA" or enetipo[1]=="ROCA" or enetipo[0]=="VENENO" or enetipo[0]=="ROCA":
									mie = 2
								if enetipo[0]=="VOLADOR" or enetipo[1]=="VOLADOR":
									mie = 0
							if tipoe=="VENENO":
								if enetipo[0]=="LUCHA" or enetipo[1]=="LUCHA" or enetipo[0]=="ROCA" or enetipo[1]=="ROCA" or enetipo[0]=="TIERRA" or enetipo[1]=="TIERRA" or enetipo[0]=="VENENO" or enetipo[0]=="VENENO":
									mie = 0.5
								if enetipo[0]=="PLANTA" or enetipo[0]=="PLANTA":
									mie = 2
							if tipoe=="VOLADOR":
								if enetipo[0]=="ELECTRICO" or enetipo[1]=="ELECTRICO" or enetipo[0]=="ROCA" and enetipo[1]=="ROCA":
									mie = 0.5
								if enetipo[0]=="BICHO" or enetipo[1]=="BICHO" or enetipo[0]=="LUCHA" or enetipo[1]=="LUCHA" or enetipo[0]=="PLANTA" or enetipo[0]=="PLANTA":
									mie = 2
							if mie==0:
								miestado = "El pokemon enemigo es inmune a tu Tipo de Ataque"
							if mie==0.5:
								miestado = "Poco Eficaz"
							if mie==1:
								miestado = "Daño normal"
							if mie==2:
								miestado = "Muy Efectivo"
							# eneDefensaPoke = Defensa del pokemon
							# definir tipo de ataque, especial o normal
							# ################################################################################################
							# ########################### D A Ñ O   P O R  EL TIPO #########################
							# ################################################################################################
							# ################################################################################################
							estadoa = ""
							suerte = randint(0,100)
							estadofe = ""
							estadofa = ""
							# mi Estado favorable;
							miest = ""
							# Estado favorable para el enemigo
							eneest = ""
							if tipoe=="FUEGO" and miataque!="Giro Fuego" and (enetipo[0]!="FUEGO" or enetipo[1]!="FUEGO"):
								if (miataque=="Ascuas" or miataque=="Lanza Llamas" or miataque=="Puño Fuego") and suerte<=30:
									estadoa = "Quemado"
							# Disparo demoras baja un nivel de velocidad del pokemon enemigo, osea le resta "1".
							if miataque=="Disparo Demoras":
								estadoa = "menosVelocidad"
							# PARALIZAR   F  y V o v
							if tipoe=="ELECTRICO":
								if enetipo[0]!="TIERRA" or enetipo[1]!="TIERRA":
									if miataque=="Onda Trueno":
										suerte = randint(0,100)
										if suerte<=20:
											estadoa = "Paralizado"
									suerte = randint(0,100)
									if suerte<=20 and miataque=="Puño Trueno":
										estadoa = "Paralizado"
									if suerte<=30 and miataque=="Rayo":
										estadoa = "Paralizado"
									if miataque=="Trueno" and suerte<=15:
										estadoa = "Paralizado"
							# CONGELAR
							if tipoe=="HIELO":
								if (miataque=="Rayo Hielo" or miataque=="Vendisca" or miataque=="Puño Hielo") and suerte<=29 and (enetipo[0]!="HIELO" or enetipo[1]!="HIELO"):
									estadoa = "Congelado"
							if tipoe=="VENENO":
								if (mitipo[0]=="VENENO" or mitipo[1]=="VENENO") and miataque=="Toxico" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO"):
									estadoa = "Envenenado"
								else:
									if (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and miataque=="Toxico" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and suerte<=90:
										estadoa = "Envenenado"
								if miataque=="Polvo Veneno" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO"):
									estadoa = "Envenenado"
								if (miataque=="Picotazo Venenoso" or miataque=="Residuos") and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and suerte<=30:
									estadoa = "Envenenado"
								if miataque=="Gas Venenoso" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and suerte<=55:
									estadoa = "Envenenado"
								if miataque=="Acido" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and suerte<=10:
									estadoa = "Envenenado"
								if miataque=="Polucion" and (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and suerte<=40:
									estadoa = "Envenenado"
							# DORMIR
							if tipoe=="NORMAL":
								if miataque=="Canto":
									estadoa = "Dormido"
							# K.O SEGURO ;)
							# Precicion=[(U-O)+30]%
							# U=Nivel del Pokemon Usuario
							# O=Nivel del Pokemon Objetivo
							k_o = randint(0,2)
							if miataque=="Fisura" and suerte<=30 and k_o<=1:
								estadoa = "Debilitado"
							# DRENAJE
							# eL Drenaje es un estado donde se te resta Energia a Cada Turno
							if tipoe=="PLANTA":
								if miataque=="Drenadoras" and (enetipo[0]!="PLANTA" and enetipo[1]!="PLANTA"):
									estadoa = "Drenando"
								if miataque=="Agotamiento":
									estadoa = "Agotamiento"
								if miataque=="Absorber":
									estadoa = "Absorber"
							# Armadura Acida 
							# Armadura Acida suebe en 2 niveles los puntos de defensa del pokemon
							if miataque=="Armadura Acida":
								estadoa = "masDefensa"
							if miataque=="Chirridos":
								estadoa = "menosDefensa"
							if miataque=="Patada Salto" and suerte<=30:
								mipoderataque = 70
							else:
								if miataque=="Patada Salto" and suerte>30:
									miest = "Me hice daño"
									misaludpoke = misaludpoke-(misaludpoke/8)
									misaludpoke = int(misaludpoke)
							# Descanso
							# descanso es un ataque tipo psiquico que te duerme durante 2 turnos
							# mientras duermes recuperas todos tus puntos de salud(ps), puedes ser atacado en estos 2 turnos
							# depsues de 2 turnos el pokemon despierta solo
							if miataque=="Descanso":
								estadoa = "Dormido"
							# Amnesia
							# Amnesia es un ataque tipo Psiquico que al usarlo, sube el especial en 2 puntos
							if miataque=="Amnesia":
								estadoa = "masVelocidad"
							# Golpe Karate 
							# Golpe Karate es Tipo Normal en esta generacion y tiene un alto porcentaje de daño critico
							if miataque=="Golpe Karate":
								if suerte>=60:
									miest = "ha hecho un Critico favorable"
									mie = 6
							# Tienieblas
							# Tienielas es un ataque tipo fantasma que hace un daño al enemigo, igual al del nivel del atacante
							if miataque=="Tinieblas" and (enetipo[0]!="NORMAL" or enetipo[1]!="NORMAL"):
								enesaludpoke = enesaludpoke-milvl
								enesaludpoke = int(enesaludpoke)
							# Rayo Aurora
							# Rayo Aurora es un ataque tipo Hielo que tiene 10% de probabilidad de Congelar
							if miataque=="Rayo Aurora " and suerte<=29:
								estadoa = "Congelado"
							# Ataque Psiquico 
							# Ataque Psiquico o simplemente "Psiquico" es un ataque tipo PSIQUICO que tiene 10% de probabilidades de confundir
							if miataque=="Ataque Psiquico" and suerte<=10:
								estadoa = "Confundido"
							# Ataque Arena
							# en esta genracion Ataque Arena es Tipo NORMAL 
							# Ataque Arena baja la precicion en 2 puntos
							if miataque=="Ataque Arena":
								estadofa = "ha disminuido la presicion"
								enevelocidadpoke = enevelocidadpoke-(enevelocidadpoke/4)
								enevelocidadpoke = int(enevelocidadpoke)
							# Transformacion
							# Transformacion es un ataque del tipo normal que permite al ususario trasformarce en el pokemon enemigo
							if miataque=="Transformacion":
								miest = miataque
								for contx in range(4):
									minombreataque[contx] = enenombreataque[contx]
									mipp[contx] = enepp[contx]
									mitipoa[contx] = enetipoa[contx]
									mifijopp[contx] = enefijopp[contx]
									midano[contx] = enedano[contx]
							# ################################################################################################
							# ################################################################################################
							if estadoa=="masDefensa":
								midefensapoke = midefensapoke+30
								miest = " ha aumentado la Defensa"
							if estadoa=="menosDefensa":
								enedefensapoke = enedefensapoke-30
								estadofe = " ha bajado la Defensa"
							if estadoa=="Absorber":
								drenado = enesaludpoke*0.15
								misaludpoke = misaludpoke+drenado
								enesaludpoke = enesaludpoke-drenado
								misaludpoke = int(misaludpoke)
								enesaludpoke = int(enesaludpoke)
								estadofe = "ha absorvido al enemigo"
							if estadoa=="Agotamiento":
								drenado = enesaludpoke*0.1
								misaludpoke = misaludpoke+drenado
								enesaludpoke = enesaludpoke-drenado
								misaludpoke = int(misaludpoke)
								enesaludpoke = int(enesaludpoke)
								estadofe = " ha agotado al enemigo"
							if estadoa=="menosVelocidad":
								estadofe = "ha bajado la Velocidad"
								enevelocidadpoke = enevelocidadpoke-20
							if estadoa=="masVelocidad":
								miest = "ha subido la Velocidad"
								mivelocidadpoke = mivelocidadpoke+20
							if estadoa=="Quemado":
								enesaludpoke = enesaludpoke-(enesaludpoke*0.125)
								estadofe = "esta Quemado"
							if estadoa=="Paralizado":
								paralizadoe = True
								estadofe = "Paralizado"
							if estadoa=="Congelado":
								paralizadoe = True
								estadofe = "Congelado"
							if estadoa=="Envenenado":
								enesaludpoke = enesaludpoke-(enesaludpoke*0.125)
								enesaludpoke = int(enesaludpoke)
								estadofe = "esta Envenenado"
							if estadoa=="Dormido":
								paralizadoe = True
								estadofe = "esta Dormido"
							if estadoa=="Drenado":
								drenado = enesaludpoke*0.07
								misaludpoke = misaludpoke+drenado
								enesaludpoke = enesaludpoke-drenado
								misaludpoke = int(misaludpoke)
								enesaludpoke = int(enesaludpoke)
								estadofe = "ha drenado vida oponente"
							if estadoa=="Debilitado":
								enesaludpoke = 0
								estadofe = "El Pokémon enemigo esta debilitado"
								paralizadoe = True
							if estadoa=="Confundido":
								estadofe = "esta confundido"
								suerte = randint(0,1)
								if suerte==0:
									enesaludpoke = enesaludpoke-(enesaludpoke*0.1)
									enesaludpoke = int(enesaludpoke)
							# ################################################################################################
							# ################################################################################################
							# Calculo del daño
							mitotaldano = 0.01*b*mie*v*((((0.2+milvl+1)*ataquepoke*mipoderataque)/(25*enedefensapoke))+2)
							mitotaldano = int(mitotaldano)
							# ************************* Enemigo  CALCULO DE DAÑO
							while True:# no hay 'repetir' en python
								opcionataque = randint(0,4)
								if opcionataque==1 and enepp[0]>0 or opcionataque==2 and enepp[1]>0 or opcionataque==3 and enepp[2]>0 or opcionataque==4 and enepp[3]>0: break
							b = 1
							if paralizadoe==True:
								opcionataque = 99
							if opcionataque==99:
								eneataque = ""
								enepoderataque = 0
								enetipoa[0] = ""
								enetipoa[1] = ""
								enetipo[0] = ""
								enetipo[1] = ""
								b = 0
								ataquepoke = 0
								tipox = ""
							if opcionataque==1:
								# Se guarda el primer nombre
								eneataque = enenombreataque[0]
								enepoderataque = enedano[0]
								# Bono  
								if enetipoa[0]==enetipo[0] or enetipoa[0]==enetipo[1]:
									b = 1.5
								if enetipoa[0]!="NORMAL":
									ataquepoke = eneespecialpoke
								else:
									ataquepoke = eneataquepoke
								tipox = enetipoa[0]
								enepp[0] = enepp[0]-1
							if opcionataque==2:
								# Se guarda el primer nombre
								eneataque = enenombreataque[1]
								enepoderataque = enedano[1]
								# Bono  
								if enetipoa[1]==enetipo[0] or enetipoa[1]==enetipo[1]:
									b = 1.5
								if enetipoa[1]!="NORMAL":
									ataquepoke = eneespecialpoke
								else:
									ataquepoke = eneataquepoke
								enepp[1] = enepp[1]-1
								tipox = enetipoa[1]
							if opcionataque==3:
								# Se guarda el primer nombre
								eneataque = enenombreataque[2]
								enepoderataque = enedano[2]
								# Bono  
								if enetipoa[2]==enetipo[0] or enetipoa[2]==enetipo[1]:
									b = 1.5
								if enetipoa[2]!="NORMAL":
									ataquepoke = eneespecialpoke
								else:
									ataquepoke = eneataquepoke
								tipox = enetipoa[2]
								enepp[2] = enepp[2]-1
							if opcionataque==4:
								# Se guarda el primer nombre
								eneataque = enenombreataque[3]
								enepoderataque = enedano[3]
								# Bono  
								if enetipoa[3]==enetipo[0] or enetipoa[3]==enetipo[1]:
									b = 1.5
								if enetipoa[3]!="NORMAL":
									ataquepoke = eneespecialpoke
								else:
									ataquepoke = eneataquepoke
								tipox = enetipoa[3]
								enepp[3] = enepp[3]-1
							# Efectividad 0.025 , 0.5 , 1 , 2 y 4
							# SOLO POR QUE TIENEN X, #, 0, porque los que tienen 1 estan por defecto en el caso si no dentran al algoritmo de abajo
							mie = 1
							if tipox=="AGUA":
								if mitipo[0]=="AGUA" or mitipo[1]=="AGUA" or mitipo[0]=="DRAGON" or mitipo[1]=="DRAGON" or mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA":
									mie = 0.5
								if mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="ROCA" or mitipo[1]=="ROCA" or mitipo[0]=="TIERRA" or mitipo[1]=="TIERRA":
									mie = 2
							if tipox=="BICHO":
								if mitipo[0]=="FANTASMA" or mitipo[1]=="FANTASMA" or mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="LUCHA" or mitipo[1]=="LUCHA" or mitipo[0]=="VENENO" or mitipo[1]=="VENENO":
									mie = 0.5
								if mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA" or mitipo[0]=="PSIQUICO" or mitipo[1]=="PSIQUICO":
									mie = 0
							if tipox=="DRAGON":
								if mitipo[0]==tipox or mitipo[1]==tipox:
									mie = 2
							if tipox=="ELECTRICO":
								if mitipo[0]=="DRAGON" or mitipo[1]=="DRAGON" or mitipo[0]=="ELECTRICO" or mitipo[1]=="ELECTRICO" or mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA":
									mie = 0.5
								if mitipo[0]=="ELECTRICO" or mitipo[1]=="ELECTRICO" or mitipo[0]=="VOLADOR" or mitipo[1]=="VOLADOR":
									mie = 2
								if mitipo[0]=="TIERRA" or mitipo[0]=="TIERRA":
									mie = 0
							if tipox=="FANTASMA":
								if mitipo[0]=="FANTASMA" or mitipo[1]=="FANTASMA":
									mie = 2
								if mitipo[0]=="NORMAL" or mitipo[0]=="NORMAL":
									mie = 0
							if tipox=="FUEGO":
								if mitipo[0]=="AGUA" or mitipo[1]=="AGUA" or mitipo[0]=="DRAGON" or mitipo[1]=="DRAGON" or mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="ROCA" or mitipo[1]=="ROCA":
									mie = 0.5
								if mitipo[0]=="BICHO" or mitipo[1]=="BICHO" or mitipo[0]=="HIELO" or mitipo[1]=="HIELO" or mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA":
									mie = 2
							if tipox=="HIELO":
								if mitipo[0]=="AGUA" or mitipo[1]=="AGUA" or mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="HIELO" or mitipo[1]=="HIELO":
									mie = 0.5
								if mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA" or mitipo[0]=="TIERRA" or mitipo[1]=="TIERRA" or mitipo[0]=="VOLADOR" or mitipo[1]=="VOLADOR":
									mie = 2
							if tipox=="LUCHA":
								if mitipo[0]=="BICHO" or mitipo[0]=="BICHO" or mitipo[0]=="PSIQUICO" or mitipo[1]=="PSIQUICO" or mitipo[0]=="VENENO" or mitipo[0]=="VENENO" or mitipo[0]=="VOLADOR" or mitipo[0]=="VOLADOR":
									mie = 0.5
								if mitipo[0]=="HIELO" or mitipo[1]=="HIELO" or mitipo[0]=="NOMRAL" or mitipo[1]=="NORMAL" or mitipo[0]=="ROCA" or mitipo[0]=="ROCA":
									mie = 2
								if mitipo[0]=="FANTASMA" or mitipo[0]=="FANTASMA":
									mie = 0
							if tipox=="NORMAL":
								if mitipo[0]=="FANTASMA" or mitipo[1]=="FANTASMA":
									mie = 0
							if tipox=="PLANTA":
								if mitipo[0]=="BICHO" or mitipo[1]=="BICHO" or mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="PLANTA" or mitipo[1]=="PLANTA" or mitipo[0]=="VENENO" or mitipo[1]=="VENENO" or mitipo[0]=="VOLADOR" or mitipo[1]=="VOLADOR":
									mie = 0.5
								if mitipo[0]=="AGUA" or mitipo[1]=="AGUA" or mitipo[0]=="ROCA" or mitipo[1]=="ROCA" or mitipo[0]=="TIERRA" or mitipo[1]=="TIERRA":
									mie = 2
							if tipox=="PSIQUICO":
								if mitipo[0]=="PSIQUICO" or mitipo[1]=="PSIQUICO":
									mie = 0.5
								if mitipo[0]=="LUCHA" or mitipo[1]=="LUCHA" or mitipo[0]=="VENENO" or mitipo[0]=="VENENO":
									mie = 2
							if tipox=="ROCA":
								if mitipo[0]=="LUCHA" or mitipo[1]=="LUCHA" or mitipo[0]=="TIERRA" or mitipo[1]=="TIERRA":
									mie = 0.5
								if mitipo[0]=="BICHO" or mitipo[1]=="BICHO" or mitipo[0]=="FUEGO" or mitipo[1]=="FUEGO" or mitipo[0]=="HIELO" or mitipo[1]=="HIELO" or mitipo[0]=="VOLADOR" or mitipo[1]=="VOLADOR":
									mie = 2
							if tipox=="TIERRA":
								if mitipo[0]=="BICHO" or mitipo[1]=="BICHO" or mitipo[0]=="PLANTA" or mitipo[0]=="PLANTA":
									mie = 0.5
								if mitipo[0]=="ELECTRICO" or mitipo[1]=="ELECTRICO" or mitipo[0]=="ROCA" or mitipo[1]=="ROCA" or mitipo[0]=="VENENO" or mitipo[0]=="ROCA":
									mie = 2
								if mitipo[0]=="VOLADOR" or mitipo[1]=="VOLADOR":
									mie = 0
							if tipox=="VENENO":
								if mitipo[0]=="LUCHA" or mitipo[1]=="LUCHA" or mitipo[0]=="ROCA" or mitipo[1]=="ROCA" or mitipo[0]=="TIERRA" or mitipo[1]=="TIERRA" or mitipo[0]=="VENENO" or mitipo[0]=="VENENO":
									mie = 0.5
								if mitipo[0]=="PLANTA" or mitipo[0]=="PLANTA":
									mie = 2
							if tipox=="VOLADOR":
								if mitipo[0]=="ELECTRICO" or mitipo[1]=="ELECTRICO" or mitipo[0]=="ROCA" and mitipo[1]=="ROCA":
									mie = 0.5
								if mitipo[0]=="BICHO" or mitipo[1]=="BICHO" or mitipo[0]=="LUCHA" or mitipo[1]=="LUCHA" or mitipo[0]=="PLANTA" or mitipo[0]=="PLANTA":
									mie = 2
							if mie==0:
								eneestado = "Tu pokemon es inmune al Ataque enemigo"
							if mie==0.5:
								eneestado = "Poco Eficaz"
							if mie==1:
								eneestado = "Daño normal"
							if mie==2:
								eneestado = "Muy Efectivo"
							# definir tipo de ataque, especial o normal
							# ################################################################################################
							# ########################### D A Ñ O   P O R  EL TIPO #########################
							# ################################################################################################
							# ################################################################################################
							estadoe = ""
							suerte = randint(0,100)
							estadofa = ""
							# Estado favorable para el enemigo
							eneest = ""
							if tipox=="FUEGO" and eneataque!="Giro Fuego" and (mitipo[0]!="FUEGO" or mitipo[1]!="FUEGO"):
								if (eneataque=="Ascuas" or eneataque=="Lanza Llamas" or eneataque=="Puño Fuego") and suerte<=30:
									estadoe = "Quemado"
							# Disparo demoras baja un nivel de velocidad del pokemon enemigo, osea le resta "1".
							if eneataque=="Disparo Demoras":
								estadoe = "menosVelocidad"
							# PARALIZAR   F  y V o v
							if tipox=="ELECTRICO":
								if mitipo[0]!="TIERRA" or mitipo[1]!="TIERRA":
									if eneataque=="Onda Trueno":
										suerte = randint(0,100)
										if suerte<=20:
											estadoe = "Paralizado"
									suerte = randint(0,100)
									if suerte<=20 and eneataque=="Puño Trueno":
										estadoe = "Paralizado"
									if suerte<=30 and eneataque=="Rayo":
										estadoe = "Paralizado"
									if eneataque=="Trueno" and suerte<=15:
										estadoe = "Paralizado"
							if tipox=="PLANTA":
								if eneataque=="Paralizador":
									estadoe = "Paralizado"
							# CONGELAR
							if tipox=="HIELO":
								if (eneataque=="Rayo Hielo" or eneataque=="Vendisca" or eneataque=="Puño Hielo") and suerte<=29 and (mitipo[0]!="HIELO" or mitipo[1]!="HIELO"):
									estadoe = "Congelado"
							if tipox=="VENENO":
								if (enetipo[0]=="VENENO" or enetipo[1]=="VENENO") and eneataque=="Toxico" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO"):
									estadoe = "Envenenado"
								else:
									if (enetipo[0]!="VENENO" or enetipo[1]!="VENENO") and eneataque=="Toxico" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and suerte<=90:
										estadoe = "Envenenado"
								if eneataque=="Polvo Veneno" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO"):
									estadoe = "Envenenado"
								if (eneataque=="Picotazo Venenoso" or eneataque=="Residuos") and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and suerte<=30:
									estadoe = "Envenenado"
								if eneataque=="Gas Venenoso" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and suerte<=55:
									estadoe = "Envenenado"
								if eneataque=="Acido" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and suerte<=10:
									estadoe = "Envenenado"
								if eneataque=="Polucion" and (mitipo[0]!="VENENO" or mitipo[1]!="VENENO") and suerte<=40:
									estadoe = "Envenenado"
							# DORMIR
							if tipox=="NORMAL":
								if eneataque=="Canto":
									estadoe = "Dormido"
							# K.O SEGURO ;)
							# Precicion=[(U-O)+30]%
							# U=Nivel del Pokemon Usuario
							# O=Nivel del Pokemon Objetivo
							k_o = randint(0,2)
							if eneataque=="Fisura" and suerte<=30 and k_o<=1:
								estadoe = "Debilitado"
							# DRENAJE
							# eL Drenaje es un estado donde se te resta Energia a Cada Turno
							if tipox=="PLANTA":
								if eneataque=="Drenadoras" and (mitipo[0]!="PLANTA" and mitipo[1]!="PLANTA"):
									estadoe = "Drenando"
								if eneataque=="Agotamiento":
									estadoe = "Agotamiento"
								if eneataque=="Absorber":
									estadoe = "Absorber"
							# Armadura Acida 
							# Armadura Acida suebe en 2 niveles los puntos de defensa del pokemon
							if eneataque=="Armadura Acida":
								estadoe = "masDefensa"
							if eneataque=="Chirridos":
								estadoe = "menosDefensa"
							if eneataque=="Patada Salto" and suerte<=30:
								enepoderataque = 70
							else:
								if eneataque=="Patada Salto" and suerte>30:
									eneest = "se ha hecho daño"
									enesaludpoke = enesaludpoke-(enesaludpoke/8)
									enesaludpoke = int(enesaludpoke)
							# Descanso
							# descanso es un ataque tipo psiquico que te duerme durante 2 turnos
							# mientras duermes recuperas todos tus puntos de salud(ps), puedes ser atacado en estos 2 turnos
							# depsues de 2 turnos el pokemon despierta solo
							if eneataque=="Descanso":
								estadoe = "Dormido"
							# Amnesia
							# Amnesia es un ataque tipo Psiquico que al usarlo, sube el especial en 2 puntos
							if eneataque=="Amnesia":
								estadoe = "masVelocidad"
							# Golpe Karate 
							# Golpe Karate es Tipo Normal en esta generacion y tiene un alto porcentaje de daño critico
							if eneataque=="Golpe Karate":
								if suerte>=60:
									eneest = "ha hecho un Critico"
									mie = 6
							# Tienieblas
							# Tienielas es un ataque tipo fantasma que hace un daño al enemigo, igual al del nivel del atacante
							if eneataque=="Tinieblas" and (mitipo[0]!="NORMAL" or mitipo[1]!="NORMAL"):
								misaludpoke = misaludpoke-enelvl
								misaludpoke = int(misaludpoke)
							# Rayo Aurora
							# Rayo Aurora es un ataque tipo Hielo que tiene 10% de probabilidad de Congelar
							if eneataque=="Rayo Aurora " and suerte<=29:
								estadoe = "Congelado"
							# Ataque Psiquico 
							# Ataque Psiquico o simplemente "Psiquico" es un ataque tipo PSIQUICO que tiene 10% de probabilidades de confundir
							if eneataque=="Ataque Psiquico" and suerte<=10:
								estadoe = "Confundido"
							# Ataque Arena
							# en esta genracion Ataque Arena es Tipo NORMAL 
							# Ataque Arena baja la precicion en 2 puntos
							if eneataque=="Ataque Arena":
								estadofe = "ha disminuido la presicion"
								mivelocidadpoke = mivelocidadpoke-(mivelocidadpoke/4)
								mivelocidadpoke = int(mivelocidadpoke)
							# Transformacion
							# Transformacion es un ataque del tipo normal que permite al ususario trasformarce en el pokemon enemigo
							if eneataque=="Transformacion":
								eneest = eneataque
								for contx in range(4):
									enenombreataque[contx] = minombreataque[contx]
									enepp[contx] = mipp[contx]
									enetipoa[contx] = mitipoa[contx]
									enefijopp[contx] = mifijopp[contx]
									enedano[contx] = midano[contx]
							# ################################################################################################
							# ################################################################################################
							if estadoe=="masDefensa":
								enedefensapoke = enedefensapoke+30
								eneest = "ha Aumentado la Defensa"
							if estadoe=="menosDefensa":
								midefensapoke = midefensapoke-30
								estadofa = "ha Bajado la Defensa"
							if estadoe=="Absorber":
								drenado = misaludpoke*0.15
								enesaludpoke = enesaludpoke+drenado
								misaludpoke = misaludpoke-drenado
								enesaludpoke = int(enesaludpoke)
								misaludpoke = int(misaludpoke)
								estadofa = "ha abosorvido"
							if estadoe=="Agotamiento":
								drenado = misaludpoke*0.1
								enesaludpoke = enesaludpoke+drenado
								misaludpoke = misaludpoke-drenado
								enesaludpoke = int(enesaludpoke)
								misaludpoke = int(misaludpoke)
								estadofa = estadoe
							if estadoe=="menosVelocidad":
								estadofa = "ha Bajado Velocidad"
								mivelocidadpoke = mivelocidadpoke-20
							if estadoe=="masVelocidad":
								eneest = "ha subido Velocidad"
								enevelocidadpoke = enevelocidadpoke+20
							if estadoe=="Quemado":
								misaludpoke = misaludpoke-(misaludpoke*0.125)
								misaludpoke = int(misaludpoke)
								estadofa = "esta Quemado"
							if estadoe=="Paralizado":
								paralizadoa = True
								estadofa = "Paralizado"
							if estadoe=="Congelado":
								paralizadoa = True
								estadofa = "Congelado"
							if estadoe=="Envenenado":
								misaludpoke = misaludpoke-(misaludpoke*0.125)
								misaludpoke = int(misaludpoke)
								estadofa = "esta Envenenado"
							if estadoe=="Dormido":
								paralizadoa = True
								estadofa = "Esta Dormido"
							if estadoe=="Drenado":
								drenado = misaludpoke*0.07
								enesaludpoke = enesaludpoke+drenado
								misaludpoke = misaludpoke-drenado
								enesaludpoke = int(enesaludpoke)
								misaludpoke = int(misaludpoke)
								estadofa = "ha drenado vida"
							if estadoe=="Debilitado":
								misaludpoke = 0
								estadofa = "El Pokémon enemigo esta debilitado"
								paralizadoa = True
							if estadoe=="Confundido":
								estadofa = "esta confundido"
								suerte = randint(0,1)
								if suerte==0:
									misaludpoke = misaludpoke-(misaludpoke*0.1)
									misaludpoke = int(misaludpoke)
							# ################################################################################################
							# ################################################################################################
							enetotaldano = 0.01*b*mie*v*((((0.2+enelvl+1)*ataquepoke*enepoderataque)/(25*midefensapoke))+2)
							enetotaldano = int(enetotaldano)
							# ¿Quien Ataca Primero ? 
							miv = randint(0,mivelocidadpoke)
							enev = randint(0,enevelocidadpoke)
							if paralizadoa==False and paralizadoe==False:
								if miv>=enev:
									print("Has Ganado en velocidad")
									enesaludpoke = enesaludpoke-mitotaldano
									print("¡",minombrepoke," usó ",miataque,"!")
									sleep(2)
									if miest!="":
										print("¡mi Pokémon ",minombrepoke," ",miest,"!")
										sleep(2)
									if estadofe!="":
										print("¡El Pokémon ",enenombrepoke," ",estadofe,"!")
										sleep(2)
									if enesaludpoke<=0:
										# Batalla termino
										print("ha muerto el pokemon enemigo")
										enehp = False
										win = win+1
										enesaludpoke = 0
									if enesaludpoke>0:
										misaludpoke = misaludpoke-enetotaldano
										print("¡Enemigo ",enenombrepoke," usó ",eneataque,"!")
										sleep(2)
										if eneest!="":
											print("¡Enemigo Pokémon ",enenombrepoke," ",eneest,"!")
											sleep(2)
										if estadofa!="":
											print("¡mi Pokémon ",minombrepoke," ",estadofa,"!")
											sleep(2)
										if misaludpoke<=0:
											print("Ha muerto tu pokemon")
											mihp = False
											misaludpoke = 0
								if enev>miv:
									print("El ha Ganado en velocidad")
									misaludpoke = misaludpoke-enetotaldano
									print("¡Enemigo ",enenombrepoke," usó ",eneataque,"!")
									sleep(2)
									if eneest!="":
										print("¡Enemigo Pokémon ",enenombrepoke," ",eneest,"!")
										sleep(2)
									if estadofa!="":
										print("¡mi Pokémon ",minombrepoke," ",estadofa,"!")
										sleep(2)
									if misaludpoke<=0:
										# Batalla termino
										print("ha muerto tu pokemon")
										misaludpoke = 0
										mihp = False
									if misaludpoke>0:
										enesaludpoke = enesaludpoke-mitotaldano
										print("¡",minombrepoke," usó ",miataque,"!")
										sleep(2)
										if miest!="":
											print("¡mi Pokémon ",minombrepoke," ",miest,"!")
											sleep(2)
										if estadofe!="":
											print("¡El Pokémon ",enenombrepoke," ",estadofe,"!")
											sleep(2)
										if enesaludpoke<=0:
											print("Ha muerto el pokemon enemigo")
											enehp = False
											win = win+1
											enesaludpoke = 0
							# paralizadoA = Yo estoy paralizado Verdadero=Cuando esta
							# paralizadoE = enemigo paralizado  Falso= cuando no esta
							# EL ATACA
							if paralizadoa==True and paralizadoe==False:
								print("¡Estas ",estadofa,"!")
								misaludpoke = misaludpoke-enetotaldano
								print("¡Enemigo ",enenombrepoke," usó ",eneataque,"!")
								# Esperar 2 Segundos;        
								if misaludpoke<0:
									print("Ha muerto tu Pokémon")
									mihp = False
									misaludpoke = 0
								paralizadoa = False
								paralizadoe = False
								estadofa = ""
							# YO ATACO
							if paralizadoa==False and paralizadoe==True:
								# en el caso que yo 
								print("¡",enenombrepoke," esta ",estadofe,"!")
								enesaludpoke = enesaludpoke-mitotaldano
								print("¡",minombrepoke," usó ",miataque,"!")
								# Esperar 2 Segundos;
								if enesaludpoke<=0:
									print("Ha muerto el pokemon enemigo")
									enehp = False
									win = win+1
									enesaludpoke = 0
								paralizadoa = False
								paralizadoe = False
								estadofe = ""
							# LOS DOS ESTAMOS DORMIDOS
							if paralizadoa==True and paralizadoe==True:
								print("¡",enenombrepoke," esta ",estadofe,"!")
								print("¡",minombrepoke," esta ",estadofa,"!")
								paralizadoa = False
								paralizadoe = False
								estadofe = ""
								estadofa = ""
							# Volver a los valores
							if misaludpoke==0 or enesaludpoke==0:
								if enesaludpoke==0:
									if opc6==2:
										micontwin = micontwin+1
									print("") # no hay forma directa de borrar la pantalla con Python estandar
									print("  ")
									print("|----------------------")
									print("| ",enenombrepoke)
									print("|              Nv ",enelvl)
									print("|    Ps: 0                         ________ ")
									print("|----------------------            \\/    \\/ ")
									print("                                   / X  X \\ ")
									print("                                   I\\____/I ")
									print("                                  /_\\    /_\\  ")
									print("       ________                     |    |")
									print("       \\/    \\/                    /_\\__/_\\ ")
									print("       /  ^^  \\              |-----------------")
									print("      I   ^^   I             | ",minombrepoke)
									print("     /_\\      /_\\            |        Nv ",milvl)
									print("       |      |              | Ps : ",misaludpoke,"/",misaludfija)
									print("      /_\\____/_\\             |-----------------")
									print("°------------------------------------------------°")
									print("|  ¡Pokémon ",enenombrepoke," debilitado!")
									sleep(1)
									print("|   ¡",jugador1," has ganado este combate!")
									print("°------------------------------------------------°")
								if misaludpoke==0:
									if opc6==2:
										enecontwin = enecontwin+1
									print("") # no hay forma directa de borrar la pantalla con Python estandar
									print("  ")
									print("|----------------------")
									print("| ",enenombrepoke)
									print("|              Nv ",enelvl)
									print("|    Ps:  ",enesaludpoke,"                       ________ ")
									print("|----------------------            \\/    \\/ ")
									print("                                   / O  O \\ ")
									print("                                   I\\____/I ")
									print("                                  /_\\    /_\\  ")
									print("                                    |    |")
									print("                                   /_\\__/_\\ ")
									print("       ________              |-----------------")
									print("       \\/    \\/    </3       | ",minombrepoke)
									print("       /  !   \\              |        Nv ",milvl)
									print("      I     !  I             | Ps : 0/",misaludfija)
									print("     /_\\  !   /_\\            |-----------------")
									print("°------------------------------------------------°")
									print("|  ¡Tu Pokémon ",minombrepoke," se ha debilitado!")
									sleep(1)
									print("|   ¡",enemigo1," ha ganado este combate!")
									print("°------------------------------------------------°")
								if opcmipoke==1:
									mipokeh1[0] = misaludpoke
									for contx in range(4):
										ppa1[contx] = mipp[contx]
								if eneazar==1:
									enepokeh1[0] = enesaludpoke
									for contx in range(4):
										ppe1[contx] = enepp[contx]
								if opcmipoke==2:
									mipokeh2[0] = misaludpoke
									for contx in range(4):
										ppa2[contx] = mipp[contx]
								if eneazar==2:
									enepokeh2[0] = enesaludpoke
									for contx in range(4):
										ppe2[contx] = enepp[contx]
								if opcmipoke==3:
									mipokeh3[0] = misaludpoke
									for contx in range(4):
										ppa3[contx] = mipp[contx]
								if eneazar==3:
									enepokeh3[0] = enesaludpoke
									for contx in range(4):
										ppe3[contx] = enepp[contx]
								if opcmipoke==4:
									mipokeh4[0] = misaludpoke
									for contx in range(4):
										ppa4[contx] = mipp[contx]
								if eneazar==4:
									enepokeh4[0] = enesaludpoke
									for contx in range(4):
										ppe4[contx] = enepp[contx]
								if opcmipoke==5:
									mipokeh5[0] = misaludpoke
									for contx in range(4):
										ppa5[contx] = mipp[contx]
								if eneazar==5:
									enepokeh5[0] = enesaludpoke
									for contx in range(4):
										ppe5[contx] = enepp[contx]
								if opcmipoke==6:
									mipokeh6[0] = misaludpoke
									for contx in range(4):
										ppa6[contx] = mipp[contx]
								if eneazar==6:
									enepokeh6[0] = enesaludpoke
									for contx in range(4):
										ppe6[contx] = enepp[contx]
								if cantidadpoke==1:
									totalsalud = mipokeh1[0]
									enetotalsalud = enepokeh1[0]
								if cantidadpoke==6:
									totalsalud = mipokeh1[0]+mipokeh2[0]+mipokeh3[0]+mipokeh4[0]+mipokeh5[0]+mipokeh6[0]
									enetotalsalud = enepokeh1[0]+enepokeh2[0]+enepokeh3[0]+enepokeh4[0]+enepokeh5[0]+enepokeh6[0]
							input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					if micontwin==6:
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("  ")
						print("|----------------------")
						print("| ",enemigo1)
						print("|           ")
						print("|    P E R D E D O R               ________ ")
						print("|----------------------            \\/    \\/ ")
						print("                                   / X  X \\ ")
						print("                                   I\\____/I ")
						print("                                  /_\\    /_\\  ")
						print("       ________                     |    |")
						print("       \\/    \\/                    /_\\__/_\\ ")
						print("       /  ^^  \\              |-----------------")
						print("      I   ^^   I             | ",jugador1)
						print("     /_\\      /_\\            |       ")
						print("       |      |              | G A N A D O R ")
						print("      /_\\____/_\\             |-----------------")
						print("°------------------------------------------------°")
						print("|  ",enemigo1,": ¡Maldito! ¡me has ganado!")
						sleep(1)
						print("|  ¡Nos volveremos a encontrar y te pateare el trasero!")
						print("°------------------------------------------------°")
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						micontwin = 0
						enecontwin = 0
					if enecontwin==6:
						print("") # no hay forma directa de borrar la pantalla con Python estandar
						print("  ")
						print("|----------------------")
						print("| ",enemigo1)
						print("|              ")
						print("|  G A N A D O R                   ________ ")
						print("|----------------------            \\/    \\/ ")
						print("                                   / -  O \\ ")
						print("                                   I\\____/I ")
						print("                                  /_\\    /_\\  ")
						print("                                    |    |")
						print("                                   /_\\__/_\\ ")
						print("       ________              |-----------------")
						print("       \\/    \\/    </3       | ",juagador1)
						print("       /  !   \\              | ")
						print("      I     !  I             |  P E R D E D O R ")
						print("     /_\\  !   /_\\            |-----------------")
						print("°------------------------------------------------°")
						print("|  ¡Te he ganado ",jugador1,", eres muy malo!")
						sleep(1)
						print("|   ¡Nos volveremos a ver, sigue entrenando !")
						print("°------------------------------------------------°")
						input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
						micontwin = 0
						enecontwin = 0
				else:
					# ERROR POR NO ASIGNAR POKEMONES AL INVENTARIO
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("")
					print("Te Falta asignar pokemones a tu inventario")
					print("")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
			# **********************************************************LABORATORIO**** OPCION 3 **************************
			# **********************************************************LABORATORIO**** OPCION 3 **************************
			# **********************************************************LABORATORIO**** OPCION 3 **************************
			if opc3==3:
				while True:# no hay 'repetir' en python
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXX| L A B O R A T O R I O     |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|   1.- ELEGIR POKEMON      |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX|   2.- REINICIAR PP        |XXXXXXXXXX")
					print("XXXXXXXXXX|                           |XXXXXXXXXX")
					print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX [3] Volver XXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("Eliga una opción :", end="")
					opc5 = int(input())
					if opc5==1 or opc5==2 or opc5==3: break
				if opc5==2:
					if cantidadpoke==1:
						print("")
						print("¡Reiniciando PP tu Pokémon ",jugador1,"!")
						sleep(2)
						print("")
						print("¡Reiniciando PP de los Pokémon ",enemigo1,"!")
						sleep(2)
						for contx in range(4):
							ppa1[contx] = ppfa1[contx]
							ppe1[contx] = ppfe1[contx]
					if cantidadpoke==6:
						print("")
						print("¡Reiniciando PP de tus Pokémon ",jugador1,"!")
						sleep(2)
						print("")
						print("¡Reiniciando PP de los Pokémon ",enemigo1,"!")
						sleep(2)
						for contx in range(4):
							ppa1[contx] = ppfa1[contx]
							ppa2[contx] = ppfa2[contx]
							ppa3[contx] = ppfa3[contx]
							ppa4[contx] = ppfa4[contx]
							ppa5[contx] = ppfa5[contx]
							ppa6[contx] = ppfa6[contx]
							ppe1[contx] = ppfe1[contx]
							ppe2[contx] = ppfe2[contx]
							ppe3[contx] = ppfe3[contx]
							ppe4[contx] = ppfe4[contx]
							ppe5[contx] = ppfe5[contx]
							ppe6[contx] = ppfe6[contx]
				if opc5==1:
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("")
					print("")
					print("SUGERENCIA ANOTAR POKEMON DEL QUE VA A USAR EN UN PAPEL")
					print("")
					print("")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
					print("")
					print("       PRESIONES CUALQUIER TECLA PARA CONTINUAR")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					# ***************************************************************LISTA DE POKEMONES**************************
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("            INVENTARIO                             POKEDEX                   INVENTARIO")
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #1     | BULBASAUR   |  PLANTA  |  VENENO |   45    |   49     |   49    |    45     |    65    |   253   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #2     | CHARMANDER  |  FUEGO   |         |   39    |   52     |   43    |    65     |    50    |   249   |")
					print("@-----------------------------------------------------------------------------------------------------------|")
					print("| #3     | SQUITLE     |  AGUA    |         |   44    |   48     |   65    |    43     |    50    |   250   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #4     | CATERPIE    |  BICHO   |         |   45    |   30     |   35    |    45     |    20    |   175   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #5     | WEEDLE      |  BICHO   | VENENO  |   40    |   35     |   30    |    50     |    20    |   175   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #6     | PIDGEY      |  NORMAL  | VOLADOR |   40    |   45     |   40    |    56     |    35    |   216   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #7     | RATTTATA    |  NORMAL  |         |   30    |   56     |   35    |    72     |    25    |   218   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #8     | SPEAROW     |  NORMAL  | VOLADOR |   40    |   60     |   30    |    70     |    31    |   231   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #9     | EKANS       |  VENENO  |         |   35    |   60     |   44    |    55     |    40    |   234   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #10    | PIKACHU     | ELECTRICO|         |   35    |   55     |   30    |    90     |    50    |   260   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 1/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #11    | SANDSHREW   |  TIERRA  |         |   50    |   75     |   85    |    40     |    30    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #12    | NIDORAN F   |  VENENO  |         |   55    |   47     |   52    |    41     |    40    |   235   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #13    | NIDORAN M   |  VENENO  |         |   46    |   57     |   40    |    50     |    40    |   233   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #14    | CLEFAIRY    |  NORMAL  |         |   70    |   45     |   48    |    35     |    60    |   258   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #15    | VULPIX      |  FUEGO   |         |   38    |   41     |   40    |    65     |    65    |   249   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #16    | JIGGLYPUFF  |  NORMAL  |         |   115   |   45     |   20    |    20     |    25    |   225   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #17    | ZUBAT       |  VENENO  |  VOLADOR|   40    |   45     |   35    |    55     |    40    |   215   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #18    | ODDISH      |  PLANTA  |  VENENO |   45    |   50     |   55    |    30     |    75    |   255   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #19    | PARAS       |  BICHO   |  PLANTA |   35    |   70     |   55    |    25     |    55    |   240   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #20    | VENONAT     |  BICHO   |  VENENO |   60    |   55     |   50    |    45     |    40    |   250   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 2/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #21    | DIGLETT     |  TIERRA  |         |   10    |   55     |   25    |    95     |    45    |   230   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #22    | MEOWTH      |  NORMAL  |         |   40    |   45     |   35    |    90     |    40    |   250   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #23    | PSYDUCK     |  AGUA    |         |   50    |   52     |   48    |    55     |    50    |   255   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #24    | MANKEY      |  LUCHA   |         |   40    |   80     |   35    |    70     |    35    |   260   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #25    | GROWLITHE   |  FUEGO   |         |   55    |   70     |   45    |    60     |    50    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #26    | POLIWAG     |  AGUA    |         |   40    |   50     |   40    |    90     |    40    |   260   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #27    | ABRA        |  PSIQUICO|         |   25    |   20     |   15    |    90     |    105   |   255   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #28    | MACHOP      |  LUCHA   |         |   70    |   80     |   50    |    35     |    35    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #29    | BELLSPROUT  |  PLATNA  |   VENENO|   50    |   75     |   35    |    40     |    70    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #30    | TENTACOOL   |  AGUA    |   VENENO|    40    |   40     |   35    |    70     |    100   |   285   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 3/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #31    | GEODUDE     |  ROCA    |   TIERRA|   40    |   80     |   100   |    20     |    30    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #32    | PONYTA      |  FUEGO   |         |   50    |   85     |   55    |    90     |    65    |   345   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #33    | SLOWPOKE    |  AGUA    | PSIQUICO|   90    |   65     |   65    |    15     |    40    |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #34    | MAGNEMITE   | ELECTRICO|         |   25    |   35     |   70    |    45     |    95    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #35    | FARFETC¨D   |  NORMAL  |  VOLADOR|   52    |   65     |   55    |    60     |    58    |   290   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #36    | DODUO       |  NORMAL  |  VOLADOR|   35    |   85     |   45    |    75     |    35    |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #37    | SEEL        |  AGUA    |         |   65    |   45     |   55    |    45     |    70    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #38    | GRIMER      |  VENENO  |         |   80    |   80     |   50    |    25     |    70    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #39    | SHELLDER    |  AGUA    |   HIELO |   30    |   65     |   100   |    40     |    40    |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #40    | GASTLY      |  FANTASMA|   VENENO|   30    |   35     |   30    |    80     |    45    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 4/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #41    | ONIX        |  ROCA    |   TIERRA|   35    |   45     |   160   |    70     |    100   |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #42    | DROWZEE     |  SPIQUICO|         |   60    |   48     |   45    |    42     |    30    |   340   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #43    | KRABBY      |  AGUA    |         |   30    |   105    |   90    |    50     |    90    |   285   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #44    | VOLTROD     |  ELECTICO|         |   40    |   30     |   50    |   100     |    55    |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #45    | EXEGGUTE    |  PLANTA  | PSIQUICO|   60    |   40     |   80    |    40     |    25    |   300   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #46    | CUBONE      |  TIERRA  |         |   50    |   50     |   95    |    35     |    55    |   275   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #47    | HITMONLEE   |  LUCHA   |         |   50    |   120    |   53    |    87     |    60    |   289   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #48    | HITMONCHAN  |  LUCHA   |         |   50    |   105    |   79    |    76     |    40    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #49    | LICKITUNG   |  NORMAL  |         |   90    |   55     |   75    |    30     |    35    |   345   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #50    | KOFFING     |  VENENO  |         |   40    |   65     |   95    |    35     |    35    |   345   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 5/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #51    | RHYHORN     |  ROCA    |   TIERRA|   80    |   85     |   95    |    25     |    60    |   310   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #52    | CHANSEY     |  NORMAL  |         |   250   |   5      |   5     |    50     |    60    |   265   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #53    | TANGELA     |  PLANTA  |   VENENO|   65    |   55     |   115   |    60     |    30    |   315   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #54    | KANGASKHAN  |  NORMAL  |         |   105   |   95     |   80    |    90     |    105   |   215   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #55    | HORSEA      |  AGUA    |         |   30    |   40     |   70    |    60     |    100   |   395   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #56    | GOLDEEN     |  AGUA    |         |   45    |   67     |   60    |    63     |    40    |   410   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #57    | STARYU      |  AGUA    |         |   30    |   45     |   55    |    85     |    70    |   270   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #58    | MR.MIME     |  PSIQUICO|         |   40    |   45     |   65    |    90     |    50    |   285   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #59    | SCYTHER     |  BICHO   |  VOLADOR|   70    |   110    |   80    |    105    |    70    |   285   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #60    | JYNX        |  HIELO   | PSIQUICO|   65    |   50     |   35    |    95     |    100   |   340   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 6/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #61    | ELECTABUZZ  | ELECTRICO|         |   65    |   83     |   57    |    105    |    55    |   420   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #62    | MAGMAR      |  FUEGO   |         |   65    |   95     |   57    |    93     |    85    |   395   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #63    | PINSIR      |  BICHO   |         |   65    |   125    |   100   |    85     |    55    |   430   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #64    | TAUROS      |  NORMAL  |         |   75    |   100    |   95    |    110    |    70    |   450   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #65    | MAGIKARP    |  AGUA    |         |   20    |   10     |   55    |    80     |    20    |   185   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #66    | LAPRAS      |  AGUA    |  HIELO  |   103   |   85     |   80    |    60     |    95    |   450   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #67    | DITTO       |  NORMAL  |         |   48    |   48     |   48    |    48     |    48    |   240   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #68    | EEVEE       |  NORMAL  |         |   55    |   55     |   50    |    55     |    65    |   280   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #69    | PORYGON     |  NORMAL  |         |   65    |   60     |   70    |    40     |    75    |   310   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #70    | OMANYTE     |  ROCA    |  AGUA   |   35    |   40     |   100   |    35     |    90    |   300   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 7/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					print("") # no hay forma directa de borrar la pantalla con Python estandar
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("| NÚMERO |  NOMBRE     |  TIPO 1  | TIPO 2  | SALUD   |  ATAQUE  | DEFENSA | VELOCIDAD | ESPECIAL | TOTAL   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #71    | KABUTO      |  ROCA    |     AGUA|   30    |   80     |   90    |    55     |    45    |   300   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #72    | AERODACTYL  |  ROCA    |  VOLADOR|   80    |   105    |   65    |    130    |    60    |   440   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #73    | SNORLAX     |  NORMAL  |         |   160   |   110    |   65    |    30     |    65    |   430   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #74    | ARTICUNO    |  HIELO   |  VOLADOR|   90    |   85     |   100   |    85     |    125   |   485   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #75    | ZAPDOS      | ELECTRICO|  VOLADOR|   90    |   90     |   85    |    100    |    125   |   490   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #76    | MOLTRES     |  FUEGO   |  VOLADOR|   90    |   100    |   90    |    90     |    125   |   495   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #77    | DRATINI     |  DRAGON  |         |   41    |   64     |   45    |    50     |    50    |   250   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #78    | MEWTWO      |  PSIQUICO|         |   106   |   110    |   90    |    130    |    154   |   590   |")
					print("|-----------------------------------------------------------------------------------------------------------|")
					print("| #79    | MEW         |  PSIQUICO|         |   100   |   100    |   100   |    100    |    100   |   500   |")
					print("@-----------------------------------------------------------------------------------------------------------@")
					print("PRESIONES CUALQUIER TECLA PARA CONTINUAR                                                             Pág 8/8")
					input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
					err = 0
					for z in range(2,7):
						# OPCION DE POSICION DE POKEMON "USUARIO"
						while True:# no hay 'repetir' en python
							if z>=3:
								print("") # no hay forma directa de borrar la pantalla con Python estandar
							print("")
							print("Elegir un pokemon ",z)
							print("")
							print("")
							p = int(input())
							if p>=1 and p!=10 and p<=79 and p!=error[0] and p!=error[1] and p!=error[2] and p!=error[3] and p!=error[4] and p!=error[5]: break
						error[err] = p
						# *******************************************LISTA DE POKEMONES USUARIO********************
						# POKEMON 1
						if p==1:
							nombrepokemon[1] = "BULBASAUR"
							# Tipo1
							pokemon[0] = "PLANTA"
							# Tipo2
							pokemon[1] = "VENENO"
							# SALUD
							pokemon[2] = "45"
							# ATAQUE
							pokemon[3] = "49"
							# DEFENSA
							pokemon[4] = "49"
							# VELOCIDAD
							pokemon[5] = "45"
							# ESPECIAL
							pokemon[6] = "65"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Latigo Cepa"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "35"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "95"
							efectivo[3] = "20"
							dano[3] = "65"
						# POKEMON 2
						if p==2:
							nombrepokemon[2] = "CHARMANDER"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "39"
							pokemon[3] = "52"
							pokemon[4] = "43"
							pokemon[5] = "65"
							pokemon[6] = "50"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 3
						if p==3:
							nombrepokemon[3] = "SQUIRTLE"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "44"
							pokemon[3] = "48"
							pokemon[4] = "65"
							pokemon[5] = "43"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 4 
						if p==4:
							nombrepokemon[4] = "CATERPIE"
							pokemon[0] = "BICHO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "30"
							pokemon[4] = "35"
							pokemon[5] = "45"
							pokemon[6] = "20"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Pin Misille"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Chupa Vidas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "20"
						# POKEMON 5
						if p==5:
							nombrepokemon[5] = "WEEDLE"
							pokemon[0] = "BICHO"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "35"
							pokemon[4] = "30"
							pokemon[5] = "50"
							pokemon[6] = "20"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Picotazo Venenoso"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 6
						if p==6:
							nombrepokemon[6] = "PIDGEY"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "40"
							pokemon[5] = "56"
							pokemon[6] = "35"
							nombreataque[0] = "Ataque Aereo"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "90"
							dano[0] = "140"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Vuelo"
							tipoataque[3] = pokemon[1]
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "30"
						# POKEMON 7
						if p==7:
							nombrepokemon[7] = "RATTATA"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "56"
							pokemon[4] = "35"
							pokemon[5] = "72"
							pokemon[6] = "25"
							nombreataque[0] = "Desctructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañazo"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 8
						if p==8:
							nombrepokemon[8] = "SPEAROW"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "60"
							pokemon[4] = "30"
							pokemon[5] = "70"
							pokemon[6] = "31"
							nombreataque[0] = "Ataque Aereo"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "90"
							dano[0] = "140"
							nombreataque[1] = "Vuelo"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "95"
							dano[1] = "90"
							nombreataque[2] = "Ataque Ala"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 9
						if p==9:
							nombrepokemon[9] = "EKANS"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "60"
							pokemon[4] = "44"
							pokemon[5] = "55"
							pokemon[6] = "40"
							nombreataque[0] = "Ácido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "70"
							dano[1] = "0"
							nombreataque[2] = "Residuos"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "95"
							dano[2] = "65"
							nombreataque[3] = "Picotazo Venenoso"
							tipoataque[3] = pokemon[0]
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "15"
						# POKEMON 9
						if p==10:
							nombrepokemon[10] = "PIKACHU"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "55"
							pokemon[4] = "30"
							pokemon[5] = "90"
							pokemon[6] = "50"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "Impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON  11
						if p==11:
							nombrepokemon[11] = "SANDSHREW"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "75"
							pokemon[4] = "85"
							pokemon[5] = "40"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Hueso Bumerang"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 12
						if p==12:
							nombrepokemon[12] = "NIDORAN F"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "47"
							pokemon[4] = "52"
							pokemon[5] = "41"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Acido"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 13
						if p==13:
							nombrepokemon[13] = "NIDORAN M"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "46"
							pokemon[3] = "57"
							pokemon[4] = "40"
							pokemon[5] = "50"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Smog"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "70"
							dano[1] = "20"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 14
						if p==14:
							nombrepokemon[14] = "CLEFAIRY"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "45"
							pokemon[4] = "48"
							pokemon[5] = "35"
							pokemon[6] = "60"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 15
						if p==15:
							nombrepokemon[15] = "VULPIX"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "38"
							pokemon[3] = "41"
							pokemon[4] = "40"
							pokemon[5] = "65"
							pokemon[6] = "65"
							nombreataque[0] = "Asucas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 16
						if p==16:
							nombrepokemon[16] = "JIGGLYPUFF"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "115"
							pokemon[3] = "45"
							pokemon[4] = "20"
							pokemon[5] = "20"
							pokemon[6] = "25"
							nombreataque[0] = "Canto"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "55"
							dano[0] = "0"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 17 
						if p==17:
							nombrepokemon[17] = "ZUBAT"
							pokemon[0] = "VENENO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "35"
							pokemon[5] = "55"
							pokemon[6] = "40"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Picotazo Venenoso"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "15"
							nombreataque[3] = "Tornado"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 18
						if p==18:
							nombrepokemon[18] = "ODDISH"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "50"
							pokemon[4] = "55"
							pokemon[5] = "30"
							pokemon[6] = "75"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 19
						if p==19:
							nombrepokemon[19] = "PARAS"
							pokemon[0] = "BICHO"
							pokemon[1] = "PLANTA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "70"
							pokemon[4] = "55"
							pokemon[5] = "25"
							pokemon[6] = "55"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[1]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Chupa Vidas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "20"
						# POKEMON 20
						if p==20:
							nombrepokemon[20] = "VENONAT"
							pokemon[0] = "BICHO"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "55"
							pokemon[4] = "50"
							pokemon[5] = "45"
							pokemon[6] = "40"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 21
						if p==21:
							nombrepokemon[21] = "DIGLETT"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "10"
							pokemon[3] = "55"
							pokemon[4] = "25"
							pokemon[5] = "95"
							pokemon[6] = "45"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 22
						if p==22:
							nombrepokemon[22] = "MEOWTH"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "35"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 23
						if p==23:
							nombrepokemon[23] = "PSYDUCK"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "52"
							pokemon[4] = "48"
							pokemon[5] = "55"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 24
						if p==24:
							nombrepokemon[24] = "MANKEY"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "80"
							pokemon[4] = "35"
							pokemon[5] = "70"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Pata Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 25 
						if p==25:
							nombrepokemon[25] = "GROWLITHE"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "70"
							pokemon[4] = "45"
							pokemon[5] = "60"
							pokemon[6] = "50"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 26
						if p==26:
							nombrepokemon[26] = "POLIWAG"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "50"
							pokemon[4] = "40"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if p==27:
							nombrepokemon[27] = "ABRA"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "25"
							pokemon[3] = "20"
							pokemon[4] = "15"
							pokemon[5] = "90"
							pokemon[6] = "105"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 28
						if p==28:
							nombrepokemon[28] = "MACHOP"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "80"
							pokemon[4] = "50"
							pokemon[5] = "35"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 29 
						if p==29:
							nombrepokemon[29] = "BELLSPROUT"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "75"
							pokemon[4] = "35"
							pokemon[5] = "40"
							pokemon[6] = "70"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Latigo Cepa"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "35"
							nombreataque[3] = "Acido"
							tipoataque[3] = pokemon[1]
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 30
						if p==30:
							nombrepokemon[30] = "TENTACOOL"
							pokemon[0] = "AGUA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "40"
							pokemon[4] = "35"
							pokemon[5] = "70"
							pokemon[6] = "100"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Picotazo Venenoso"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 31
						if p==31:
							nombrepokemon[31] = "GEODUDE"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "80"
							pokemon[4] = "100"
							pokemon[5] = "20"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Hueso Bumerang"
							tipoataque[1] = pokemon[1]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Lanza Roca"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Avalancha"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "75"
						# POKEMON 32
						if p==32:
							nombrepokemon[32] = "PONYTA"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "85"
							pokemon[4] = "55"
							pokemon[5] = "90"
							pokemon[6] = "65"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = "NORMAL"
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 33
						if p==33:
							nombrepokemon[33] = "SLOWPOKE"
							pokemon[0] = "AGUA"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "65"
							pokemon[4] = "65"
							pokemon[5] = "15"
							pokemon[6] = "40"
							nombreataque[0] = "Psico rayo"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 34
						if p==34:
							nombrepokemon[34] = "MAGNEMITE"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "25"
							pokemon[3] = "35"
							pokemon[4] = "70"
							pokemon[5] = "45"
							pokemon[6] = "95"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "Impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 35
						if p==35:
							nombrepokemon[35] = "FARFECTC D"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "52"
							pokemon[3] = "65"
							pokemon[4] = "55"
							pokemon[5] = "60"
							pokemon[6] = "58"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Tornado"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 36
						if p==36:
							nombrepokemon[36] = "DODUO"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "85"
							pokemon[4] = "45"
							pokemon[5] = "75"
							pokemon[6] = "35"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 37
						if p==37:
							nombrepokemon[37] = "SEEL"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "45"
							pokemon[4] = "55"
							pokemon[5] = "45"
							pokemon[6] = "70"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 38
						if p==38:
							nombrepokemon[38] = "GRIMER"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "80"
							pokemon[4] = "50"
							pokemon[5] = "25"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Picotazo Venenoso"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "15"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "95"
							efectivo[3] = "20"
							dano[3] = "65"
						# POKEMON 39
						if p==39:
							nombrepokemon[39] = "SHELLDER"
							pokemon[0] = "AGUA"
							pokemon[1] = "HIELO"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "65"
							pokemon[4] = "100"
							pokemon[5] = "40"
							pokemon[6] = "45"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Rayo Hielo"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 40
						if p==40:
							nombrepokemon[40] = "GASTLY"
							pokemon[0] = "FANTASMA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "35"
							pokemon[4] = "30"
							pokemon[5] = "80"
							pokemon[6] = "100"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[1]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Tinieblas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 41
						if p==41:
							nombrepokemon[41] = "ONIX"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "45"
							pokemon[4] = "160"
							pokemon[5] = "70"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Lanza Rocas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Avalancha"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "75"
						# POKEMON 42
						if p==42:
							nombrepokemon[42] = "DROWZEE"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "48"
							pokemon[4] = "45"
							pokemon[5] = "42"
							pokemon[6] = "90"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 43 
						if p==43:
							nombrepokemon[43] = "KRABBY"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "105"
							pokemon[4] = "90"
							pokemon[5] = "50"
							pokemon[6] = "25"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 44
						if p==44:
							nombrepokemon[44] = "VOLTORD"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "30"
							pokemon[4] = "50"
							pokemon[5] = "100"
							pokemon[6] = "55"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "Impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 45
						if p==45:
							nombrepokemon[45] = "EXEGGUTE"
							pokemon[0] = "PLANTA"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "40"
							pokemon[4] = "80"
							pokemon[5] = "40"
							pokemon[6] = "60"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Psico Rayo"
							tipoataque[1] = pokemon[1]
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = ""
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[1]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 46
						if p==46:
							nombrepokemon[46] = "CUBONE"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "50"
							pokemon[4] = "95"
							pokemon[5] = "35"
							pokemon[6] = "40"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Hueso Bumerag"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Excabar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 47
						if p==47:
							nombrepokemon[47] = "HITMONLEE"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "105"
							pokemon[4] = "79"
							pokemon[5] = "76"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 48
						if p==48:
							nombrepokemon[48] = "HITMONCHAN"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "105"
							pokemon[4] = "79"
							pokemon[5] = "76"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Contador"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 49
						if p==49:
							nombrepokemon[49] = "LICKITUNG"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "55"
							pokemon[4] = "75"
							pokemon[5] = "30"
							pokemon[6] = "60"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 50
						if p==50:
							nombrepokemon[50] = "KOFFING"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "65"
							pokemon[4] = "95"
							pokemon[5] = "35"
							pokemon[6] = "60"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Residuos"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "95"
							dano[2] = "65"
							nombreataque[3] = "Armadura Acida"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 51
						if p==51:
							nombrepokemon[51] = "RHYHORN"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "85"
							pokemon[4] = "95"
							pokemon[5] = "25"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Avalancha"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "75"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[1]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Lanza Rocas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "90"
							dano[3] = "50"
						# POKEMON 52
						if p==52:
							nombrepokemon[52] = "CHANSEY"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "250"
							pokemon[3] = "5"
							pokemon[4] = "5"
							pokemon[5] = "5"
							pokemon[6] = "50"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON
						if p==53:
							nombrepokemon[53] = "TANGELA"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "55"
							pokemon[4] = "115"
							pokemon[5] = "60"
							pokemon[6] = "100"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Drenadoras"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "0"
						# POKEMON
						if p==54:
							nombrepokemon[54] = "KANGASKHAN"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "105"
							pokemon[3] = "95"
							pokemon[4] = "80"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if p==55:
							nombrepokemon[55] = "HORSEA"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "40"
							pokemon[4] = "70"
							pokemon[5] = "60"
							pokemon[6] = "70"
							nombreataque[0] = "Pistol de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "100"
						# POKEMON 
						if p==56:
							nombrepokemon[56] = "GOLDEEN"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "67"
							pokemon[4] = "60"
							pokemon[5] = "63"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "95"
							dano[2] = "100"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if p==57:
							nombrepokemon[57] = "STARYU"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "45"
							pokemon[4] = "55"
							pokemon[5] = "85"
							pokemon[6] = "70"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if p==58:
							nombrepokemon[58] = "MR.MIME"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "65"
							pokemon[5] = "90"
							pokemon[6] = "100"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if p==59:
							nombrepokemon[59] = "SCYTHER"
							pokemon[0] = "BICHO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "110"
							pokemon[4] = "80"
							pokemon[5] = "105"
							pokemon[6] = "55"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "80"
							nombreataque[1] = "Pin Misile"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Disparo Demora"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Ataque Ala"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "60"
						# POKEMON 
						if p==60:
							nombrepokemon[60] = "JYNX"
							pokemon[0] = "HIELO"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "50"
							pokemon[4] = "35"
							pokemon[5] = "95"
							pokemon[6] = "95"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Puño Hielo"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = pokemon[1]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Doble Bofeton"
							tipoataque[3] = "NORMAL"
							pp[3] = "10"
							efectivo[3] = "85"
							dano[3] = "15"
						# POKEMON 
						if p==61:
							nombrepokemon[61] = "ELECTABUZZ"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "83"
							pokemon[4] = "57"
							pokemon[5] = "105"
							pokemon[6] = "85"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Golpe Karate"
							tipoataque[1] = "LUCHA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "50"
							nombreataque[2] = "Mega Puño"
							tipoataque[2] = "NORMAL"
							pp[2] = "20"
							efectivo[2] = "85"
							dano[2] = "80"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 
						if p==62:
							nombrepokemon[62] = "MAGMAR"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "95"
							pokemon[4] = "57"
							pokemon[5] = "93"
							pokemon[6] = "85"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Puño Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "75"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if p==63:
							nombrepokemon[63] = "PINSIR"
							pokemon[0] = "BICHO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "125"
							pokemon[4] = "100"
							pokemon[5] = "85"
							pokemon[6] = "55"
							nombreataque[0] = "Destructor"
							tipoataque[0] = "NORMAL"
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Pin Misille"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Cornada"
							tipoataque[2] = "NORMAL"
							pp[2] = "25"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON
						if p==64:
							nombrepokemon[64] = "TAUROS"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "75"
							pokemon[3] = "100"
							pokemon[4] = "95"
							pokemon[5] = "110"
							pokemon[6] = "70"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = "TIERRA"
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "95"
						# POKEMON 
						if p==65:
							nombrepokemon[65] = "MAGIKARP"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "20"
							pokemon[3] = "10"
							pokemon[4] = "55"
							pokemon[5] = "80"
							pokemon[6] = "20"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "95"
						# POKEMON 
						if p==66:
							nombrepokemon[66] = "LAPRAS"
							pokemon[0] = "AGUA"
							pokemon[1] = "HIELO"
							# Salud
							pokemon[2] = "130"
							pokemon[3] = "85"
							pokemon[4] = "80"
							pokemon[5] = "60"
							pokemon[6] = "95"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Rayo Aurora"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if p==67:
							nombrepokemon[67] = "DITTO"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "48"
							pokemon[3] = "48"
							pokemon[4] = "48"
							pokemon[5] = "48"
							pokemon[6] = "48"
							nombreataque[0] = "Transformacion"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = ""
							tipoataque[1] = ""
							pp[1] = ""
							efectivo[1] = ""
							dano[1] = ""
							nombreataque[2] = ""
							tipoataque[2] = ""
							pp[2] = ""
							efectivo[2] = ""
							dano[2] = ""
							nombreataque[3] = ""
							tipoataque[3] = ""
							pp[3] = ""
							efectivo[3] = ""
							dano[3] = ""
						# POKEMON 
						if p==68:
							nombrepokemon[68] = "EEVEE"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "55"
							pokemon[4] = "50"
							pokemon[5] = "55"
							pokemon[6] = "65"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = "TIERRA"
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 
						if p==69:
							nombrepokemon[69] = "PORYGON"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "60"
							pokemon[4] = "70"
							pokemon[5] = "40"
							pokemon[6] = "75"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = "PSIQUICO"
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Impactrueno"
							tipoataque[3] = "ELECTRICO"
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 
						if p==70:
							nombrepokemon[70] = "OMANYTE"
							pokemon[0] = "ROCA"
							pokemon[1] = "AGUA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "40"
							pokemon[4] = "100"
							pokemon[5] = "35"
							pokemon[6] = "90"
							nombreataque[0] = "Hidro Bomba"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "80"
							dano[0] = "120"
							nombreataque[1] = "Absorber"
							tipoataque[1] = "PLANTA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "20"
							nombreataque[2] = "Excavar"
							tipoataque[2] = "TIERRA"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Lanza Rocas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "90"
							dano[3] = "50"
						# POKEMON 
						if p==71:
							nombrepokemon[71] = "KABUTO"
							pokemon[0] = "ROCA"
							pokemon[1] = "AGUA"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "80"
							pokemon[4] = "90"
							pokemon[5] = "55"
							pokemon[6] = "45"
							nombreataque[0] = "Hidro Bomba"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "80"
							dano[0] = "120"
							nombreataque[1] = "Absorber"
							tipoataque[1] = "PLANTA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "20"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[1]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if p==72:
							nombrepokemon[72] = "AERODACTYL"
							pokemon[0] = "ROCA"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "105"
							pokemon[4] = "65"
							pokemon[5] = "130"
							pokemon[6] = "60"
							nombreataque[0] = "Ataque Ala"
							tipoataque[0] = pokemon[1]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "60"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = "FUEGO"
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Lanza Rocas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = "PSIQUICO"
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if p==73:
							nombrepokemon[73] = "SNORLAX"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "160"
							pokemon[3] = "110"
							pokemon[4] = "65"
							pokemon[5] = "30"
							pokemon[6] = "65"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Descanso"
							tipoataque[1] = "PSIQUICO"
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Doble Bofeton"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "85"
							dano[3] = "15"
						# POKEMON 
						if p==74:
							nombrepokemon[74] = "ARTICUNO"
							pokemon[0] = "HIELO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "85"
							pokemon[4] = "100"
							pokemon[5] = "85"
							pokemon[6] = "125"
							nombreataque[0] = "Rayo Hielo"
							tipoataque[0] = pokemon[0]
							pp[0] = "16"
							efectivo[0] = "100"
							dano[0] = "90"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Rayo Aurora"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if p==75:
							nombrepokemon[75] = "ZAPDOS"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "90"
							pokemon[4] = "85"
							pokemon[5] = "100"
							pokemon[6] = "125"
							nombreataque[0] = "Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "70"
							dano[0] = "120"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Impactrueno"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "100"
							dano[3] = "90"
						# POKEMON 
						if p==76:
							nombrepokemon[76] = "MOLTRES"
							pokemon[0] = "FUEGO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "100"
							pokemon[4] = "90"
							pokemon[5] = "90"
							pokemon[6] = "125"
							nombreataque[0] = "Lanza LLamas"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "95"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Ataque Psiquico"
							tipoataque[3] = "PSIQUICO"
							pp[3] = "10"
							efectivo[3] = "100"
							dano[3] = "90"
						# POKEMON 
						if p==77:
							nombrepokemon[77] = "DRATINI"
							pokemon[0] = "DRAGON"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "41"
							pokemon[3] = "64"
							pokemon[4] = "45"
							pokemon[5] = "50"
							pokemon[6] = "50"
							nombreataque[0] = "Furia Dragon"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Descanso"
							tipoataque[1] = "PSIQUICO"
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Placaje"
							tipoataque[2] = "NORMAL"
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Surf"
							tipoataque[3] = "AGUA"
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "100"
						# POKEMON 
						if p==78:
							nombrepokemon[78] = "MEWTWO"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "106"
							pokemon[3] = "110"
							pokemon[4] = "90"
							pokemon[5] = "130"
							pokemon[6] = "154"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = ""
							efectivo[0] = ""
							dano[0] = "65"
							nombreataque[1] = "Mega Puño"
							tipoataque[1] = "NORMAL"
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "80"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if p==79:
							nombrepokemon[79] = "MEW"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "100"
							pokemon[3] = "100"
							pokemon[4] = "100"
							pokemon[5] = "100"
							pokemon[6] = "100"
							nombreataque[0] = "Transformacion"
							tipoataque[0] = "NORMAL"
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Psico Rayo"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "65"
							nombreataque[2] = "Mega Puño"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "85"
							dano[2] = "80"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# ******PARTE X **********
						# OPCION DE POSICION DE POKEMON "USUARIO"
						if z==2:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							mipoke[1] = nombrepokemon[p]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							mipoket2[0] = pokemon[0]
							# Guarda el Tipo 2
							mipoket2[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							mipokeh2[0] = float(pokemon[2])
							# ATAQUE
							mipokeh2[1] = float(pokemon[3])
							# DEFENSA
							mipokeh2[2] = float(pokemon[4])
							# VELOCIDAD
							mipokeh2[3] = float(pokemon[5])
							# ESPECIAL
							mipokeh2[4] = float(pokemon[6])
							# Guarda la salud y es fijo
							misalud[1] = mipokeh2[0]
							# NombreAtaque[0]="Absorber";   TipoAtaque[0]=pokemon[0] ;  pp[0]="25"; efectivo[0]="100"; Dano[0]="20";
							for contx in range(4):
								nombrea2[contx] = nombreataque[contx]
								tipoa2[contx] = tipoataque[contx]
								ppa2[contx] = float(pp[contx])
								ppfa2[contx] = float(pp[contx])
								efectivoa2[contx] = float(efectivo[contx])
								danoa2[contx] = float(dano[contx])
						if z==3:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							mipoke[2] = nombrepokemon[p]
							# TIPO DEL POKE 3
							# Guarda el Tipo 1 del pokemon
							mipoket3[0] = pokemon[0]
							# Guarda el Tipo 2
							mipoket3[1] = pokemon[1]
							# Habilidad del poke 3
							# SALUD
							mipokeh3[0] = float(pokemon[2])
							# ATAQUE
							mipokeh3[1] = float(pokemon[3])
							# DEFENSA
							mipokeh3[2] = float(pokemon[4])
							# VELOCIDAD
							mipokeh3[3] = float(pokemon[5])
							# ESPECIAL
							mipokeh3[4] = float(pokemon[6])
							misalud[2] = mipokeh3[0]
							for contx in range(4):
								nombrea3[contx] = nombreataque[contx]
								tipoa3[contx] = tipoataque[contx]
								ppa3[contx] = float(pp[contx])
								ppfa3[contx] = float(pp[contx])
								efectivoa3[contx] = float(efectivo[contx])
								danoa3[contx] = float(dano[contx])
						if z==4:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							mipoke[3] = nombrepokemon[p]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							mipoket4[0] = pokemon[0]
							# Guarda el Tipo 2
							mipoket4[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							mipokeh4[0] = float(pokemon[2])
							# ATAQUE
							mipokeh4[1] = float(pokemon[3])
							# DEFENSA
							mipokeh4[2] = float(pokemon[4])
							# VELOCIDAD
							mipokeh4[3] = float(pokemon[5])
							# ESPECIAL
							mipokeh4[4] = float(pokemon[6])
							misalud[3] = mipokeh4[0]
							for contx in range(4):
								nombrea4[contx] = nombreataque[contx]
								tipoa4[contx] = tipoataque[contx]
								ppa4[contx] = float(pp[contx])
								ppfa4[contx] = float(pp[contx])
								efectivoa4[contx] = float(efectivo[contx])
								danoa4[contx] = float(dano[contx])
						if z==5:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							mipoke[4] = nombrepokemon[p]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							mipoket5[0] = pokemon[0]
							# Guarda el Tipo 2
							mipoket5[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							mipokeh5[0] = float(pokemon[2])
							# ATAQUE
							mipokeh5[1] = float(pokemon[3])
							# DEFENSA
							mipokeh5[2] = float(pokemon[4])
							# VELOCIDAD
							mipokeh5[3] = float(pokemon[5])
							# ESPECIAL
							mipokeh5[4] = float(pokemon[6])
							misalud[4] = mipokeh5[0]
							for contx in range(4):
								nombrea5[contx] = nombreataque[contx]
								tipoa5[contx] = tipoataque[contx]
								ppa5[contx] = float(pp[contx])
								ppfa5[contx] = float(pp[contx])
								efectivoa5[contx] = float(efectivo[contx])
								danoa5[contx] = float(dano[contx])
						if z==6:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							mipoke[5] = nombrepokemon[p]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							mipoket6[0] = pokemon[0]
							# Guarda el Tipo 2
							mipoket6[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							mipokeh6[0] = float(pokemon[2])
							# ATAQUE
							mipokeh6[1] = float(pokemon[3])
							# DEFENSA
							mipokeh6[2] = float(pokemon[4])
							# VELOCIDAD
							mipokeh6[3] = float(pokemon[5])
							# ESPECIAL
							mipokeh6[4] = float(pokemon[6])
							misalud[5] = mipokeh6[0]
							for contx in range(4):
								nombrea6[contx] = nombreataque[contx]
								tipoa6[contx] = tipoataque[contx]
								ppa6[contx] = float(pp[contx])
								ppfa6[contx] = float(pp[contx])
								efectivoa6[contx] = float(efectivo[contx])
								danoa6[contx] = float(dano[contx])
							cantidadpoke = 6
						# ***PARTE XI ***
						# Defino nivel para ambos
						for lvl in range(1,6):
							while True:# no hay 'repetir' en python
								minivel[lvl] = randint(0,30)
								if minivel[lvl]>=25: break
							while True:# no hay 'repetir' en python
								enenivel[lvl] = randint(0,30)
								if enenivel[lvl]>=25: break
						# ASIGNACION 
						# OPCION DE POSICION DE POKEMON "CPU"
						while True:# no hay 'repetir' en python
							eleccionpoke = randint(0,78)
							if eleccionpoke>0 and eleccionpoke!=68 and eleccionpoke!=error2[0] and eleccionpoke!=error2[1] and eleccionpoke!=error2[2] and eleccionpoke!=error2[3] and eleccionpoke!=error2[4]: break
						error2[err] = eleccionpoke
						err = err+1
						# PONER ABAJO LA LISTA COMPLETA
						# POKEMON 1
						# POKEMON 1
						if eleccionpoke==1:
							nombrepokemon[1] = "BULBASAUR"
							# Tipo1
							pokemon[0] = "PLANTA"
							# Tipo2
							pokemon[1] = "VENENO"
							# SALUD
							pokemon[2] = "45"
							# ATAQUE
							pokemon[3] = "49"
							# DEFENSA
							pokemon[4] = "49"
							# VELOCIDAD
							pokemon[5] = "45"
							# ESPECIAL
							pokemon[6] = "65"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Latigo Cepa"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "35"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "95"
							efectivo[3] = "20"
							dano[3] = "65"
						# POKEMON 2
						if eleccionpoke==2:
							nombrepokemon[2] = "CHARMANDER"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "39"
							pokemon[3] = "52"
							pokemon[4] = "43"
							pokemon[5] = "65"
							pokemon[6] = "50"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 3
						if eleccionpoke==3:
							nombrepokemon[3] = "SQUIRTLE"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "44"
							pokemon[3] = "48"
							pokemon[4] = "65"
							pokemon[5] = "43"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 4 
						if eleccionpoke==4:
							nombrepokemon[4] = "CATERPIE"
							pokemon[0] = "BICHO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "30"
							pokemon[4] = "35"
							pokemon[5] = "45"
							pokemon[6] = "20"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Pin Misille"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Chupa Vidas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "20"
						# POKEMON 5
						if eleccionpoke==5:
							nombrepokemon[5] = "WEEDLE"
							pokemon[0] = "BICHO"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "35"
							pokemon[4] = "30"
							pokemon[5] = "50"
							pokemon[6] = "20"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Picotazo Venenoso"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 6
						if eleccionpoke==6:
							nombrepokemon[6] = "PIDGEY"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "40"
							pokemon[5] = "56"
							pokemon[6] = "35"
							nombreataque[0] = "Ataque Aereo"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "90"
							dano[0] = "140"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Vuelo"
							tipoataque[3] = pokemon[1]
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "30"
						# POKEMON 7
						if eleccionpoke==7:
							nombrepokemon[7] = "RATTATA"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "56"
							pokemon[4] = "35"
							pokemon[5] = "72"
							pokemon[6] = "25"
							nombreataque[0] = "Desctructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañazo"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 8
						if eleccionpoke==8:
							nombrepokemon[8] = "SPEAROW"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "60"
							pokemon[4] = "30"
							pokemon[5] = "70"
							pokemon[6] = "31"
							nombreataque[0] = "Ataque Aereo"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "90"
							dano[0] = "140"
							nombreataque[1] = "Vuelo"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "95"
							dano[1] = "90"
							nombreataque[2] = "Ataque Ala"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 9
						if eleccionpoke==9:
							nombrepokemon[9] = "EKANS"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "60"
							pokemon[4] = "44"
							pokemon[5] = "55"
							pokemon[6] = "40"
							nombreataque[0] = "Ácido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = ""
							dano[1] = ""
							nombreataque[2] = "Residuos"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "95"
							dano[2] = "65"
							nombreataque[3] = "Picotazo Venenoso"
							tipoataque[3] = pokemon[0]
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "15"
						# POKEMON 9
						if eleccionpoke==10:
							nombrepokemon[10] = "PIKACHU"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "55"
							pokemon[4] = "30"
							pokemon[5] = "90"
							pokemon[6] = "50"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON  11
						if eleccionpoke==11:
							nombrepokemon[11] = "SANDSHREW"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "75"
							pokemon[4] = "85"
							pokemon[5] = "40"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Hueso Bumerang"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 12
						if eleccionpoke==12:
							nombrepokemon[12] = "NIDORAN F"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "47"
							pokemon[4] = "52"
							pokemon[5] = "41"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Acido"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 13
						if eleccionpoke==13:
							nombrepokemon[13] = "NIDORAN M"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "46"
							pokemon[3] = "57"
							pokemon[4] = "40"
							pokemon[5] = "50"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Smog"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "70"
							dano[1] = "20"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 14
						if eleccionpoke==14:
							nombrepokemon[14] = "CLEFAIRY"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "45"
							pokemon[4] = "48"
							pokemon[5] = "35"
							pokemon[6] = "60"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 15
						if eleccionpoke==15:
							nombrepokemon[15] = "VULPIX"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "38"
							pokemon[3] = "41"
							pokemon[4] = "40"
							pokemon[5] = "65"
							pokemon[6] = "65"
							nombreataque[0] = "Asucas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 16
						if eleccionpoke==16:
							nombrepokemon[16] = "JIGGLYPUFF"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "115"
							pokemon[3] = "45"
							pokemon[4] = "20"
							pokemon[5] = "20"
							pokemon[6] = "25"
							nombreataque[0] = "Canto"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "55"
							dano[0] = "0"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 17 
						if eleccionpoke==17:
							nombrepokemon[17] = "ZUBAT"
							pokemon[0] = "VENENO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "35"
							pokemon[5] = "55"
							pokemon[6] = "40"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Picotazo Venenoso"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "15"
							nombreataque[3] = "Tornado"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 18
						if eleccionpoke==18:
							nombrepokemon[18] = "ODDISH"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "50"
							pokemon[4] = "55"
							pokemon[5] = "30"
							pokemon[6] = "75"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 19
						if eleccionpoke==19:
							nombrepokemon[19] = "PARAS"
							pokemon[0] = "BICHO"
							pokemon[1] = "PLANTA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "70"
							pokemon[4] = "55"
							pokemon[5] = "25"
							pokemon[6] = "55"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[1]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Chupa Vidas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "20"
						# POKEMON 20
						if eleccionpoke==20:
							nombrepokemon[20] = "VENONAT"
							pokemon[0] = "BICHO"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "55"
							pokemon[4] = "50"
							pokemon[5] = "45"
							pokemon[6] = "40"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "25"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Disparo Demoras"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 21
						if eleccionpoke==21:
							nombrepokemon[21] = "DIGLETT"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "10"
							pokemon[3] = "55"
							pokemon[4] = "25"
							pokemon[5] = "95"
							pokemon[6] = "45"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 22
						if eleccionpoke==22:
							nombrepokemon[22] = "MEOWTH"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "35"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 23
						if eleccionpoke==23:
							nombrepokemon[23] = "PSYDUCK"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "52"
							pokemon[4] = "48"
							pokemon[5] = "55"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 24
						if eleccionpoke==24:
							nombrepokemon[24] = "MANKEY"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "80"
							pokemon[4] = "35"
							pokemon[5] = "70"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Pata Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 25 
						if eleccionpoke==25:
							nombrepokemon[25] = "GROWLITHE"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "70"
							pokemon[4] = "45"
							pokemon[5] = "60"
							pokemon[6] = "50"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 26
						if eleccionpoke==26:
							nombrepokemon[26] = "POLIWAG"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "50"
							pokemon[4] = "40"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Pistla de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if eleccionpoke==27:
							nombrepokemon[27] = "ABRA"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "25"
							pokemon[3] = "20"
							pokemon[4] = "15"
							pokemon[5] = "90"
							pokemon[6] = "105"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 28
						if eleccionpoke==28:
							nombrepokemon[28] = "MACHOP"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "80"
							pokemon[4] = "50"
							pokemon[5] = "35"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 29 
						if eleccionpoke==29:
							nombrepokemon[29] = "BELLSPROUT"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "75"
							pokemon[4] = "35"
							pokemon[5] = "40"
							pokemon[6] = "70"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Latigo Cepa"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "35"
							nombreataque[3] = "Acido"
							tipoataque[3] = pokemon[1]
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 30
						if eleccionpoke==30:
							nombrepokemon[30] = "TENTACOOL"
							pokemon[0] = "AGUA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "40"
							pokemon[4] = "35"
							pokemon[5] = "70"
							pokemon[6] = "100"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Picotazo Venenoso"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 31
						if eleccionpoke==31:
							nombrepokemon[31] = "GEODUDE"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "80"
							pokemon[4] = "100"
							pokemon[5] = "20"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "100"
							nombreataque[1] = "Hueso Bumerang"
							tipoataque[1] = pokemon[1]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Lanza Roca"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Avalancha"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "75"
						# POKEMON 32
						if eleccionpoke==32:
							nombrepokemon[32] = "PONYTA"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "85"
							pokemon[4] = "55"
							pokemon[5] = "90"
							pokemon[6] = "65"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza Llamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Giro Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "70"
							dano[2] = "15"
							nombreataque[3] = "Puño Fuego"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "75"
						# POKEMON 33
						if eleccionpoke==33:
							nombrepokemon[33] = "SLOWPOKE"
							pokemon[0] = "AGUA"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "65"
							pokemon[4] = "65"
							pokemon[5] = "15"
							pokemon[6] = "40"
							nombreataque[0] = "Psico rayo"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 34
						if eleccionpoke==34:
							nombrepokemon[34] = "MAGNEMITE"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "25"
							pokemon[3] = "35"
							pokemon[4] = "70"
							pokemon[5] = "45"
							pokemon[6] = "95"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "Impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 35
						if eleccionpoke==35:
							nombrepokemon[35] = "FARFECTC D"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "52"
							pokemon[3] = "65"
							pokemon[4] = "55"
							pokemon[5] = "60"
							pokemon[6] = "58"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Tornado"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 36
						if eleccionpoke==36:
							nombrepokemon[36] = "DODUO"
							pokemon[0] = "NORMAL"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "85"
							pokemon[4] = "45"
							pokemon[5] = "75"
							pokemon[6] = "35"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 37
						if eleccionpoke==37:
							nombrepokemon[37] = "SEEL"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "45"
							pokemon[4] = "55"
							pokemon[5] = "45"
							pokemon[6] = "70"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 38
						if eleccionpoke==38:
							nombrepokemon[38] = "GRIMER"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "80"
							pokemon[4] = "50"
							pokemon[5] = "25"
							pokemon[6] = "40"
							nombreataque[0] = "Armadura Acida"
							tipoataque[0] = pokemon[0]
							pp[0] = "40"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Picotazo Venenoso"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "100"
							dano[2] = "15"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[0]
							pp[3] = "95"
							efectivo[3] = "20"
							dano[3] = "65"
						# POKEMON 39
						if eleccionpoke==39:
							nombrepokemon[39] = "SHELLDER"
							pokemon[0] = "AGUA"
							pokemon[1] = "HIELO"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "65"
							pokemon[4] = "100"
							pokemon[5] = "40"
							pokemon[6] = "45"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Rayo Hielo"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 40
						if eleccionpoke==40:
							nombrepokemon[40] = "GASTLY"
							pokemon[0] = "FANTASMA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "35"
							pokemon[4] = "30"
							pokemon[5] = "80"
							pokemon[6] = "100"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[1]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Tinieblas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Residuos"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "95"
							dano[3] = "65"
						# POKEMON 41
						if eleccionpoke==41:
							nombrepokemon[41] = "ONIX"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "45"
							pokemon[4] = "160"
							pokemon[5] = "70"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = pokemon[1]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Lanza Rocas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Avalancha"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "75"
						# POKEMON 42
						if eleccionpoke==42:
							nombrepokemon[42] = "DROWZEE"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "48"
							pokemon[4] = "45"
							pokemon[5] = "42"
							pokemon[6] = "90"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 43 
						if eleccionpoke==43:
							nombrepokemon[43] = "KRABBY"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "105"
							pokemon[4] = "90"
							pokemon[5] = "50"
							pokemon[6] = "25"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 44
						if eleccionpoke==44:
							nombrepokemon[44] = "VOLTORD"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "30"
							pokemon[4] = "50"
							pokemon[5] = "100"
							pokemon[6] = "55"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Trueno"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "70"
							dano[1] = "120"
							nombreataque[2] = "Impactrueno"
							tipoataque[2] = pokemon[0]
							pp[2] = "30"
							efectivo[2] = "100"
							dano[2] = "40"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 45
						if eleccionpoke==45:
							nombrepokemon[45] = "EXEGGUTE"
							pokemon[0] = "PLANTA"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "60"
							pokemon[3] = "40"
							pokemon[4] = "80"
							pokemon[5] = "40"
							pokemon[6] = "60"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Psico Rayo"
							tipoataque[1] = pokemon[1]
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = ""
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[1]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 46
						if eleccionpoke==46:
							nombrepokemon[46] = "CUBONE"
							pokemon[0] = "TIERRA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "50"
							pokemon[4] = "95"
							pokemon[5] = "35"
							pokemon[6] = "40"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Hueso Bumerag"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "50"
							nombreataque[2] = "Excabar"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Fisura"
							tipoataque[3] = pokemon[0]
							pp[3] = "5"
							efectivo[3] = "30"
							dano[3] = "0"
						# POKEMON 47
						if eleccionpoke==47:
							nombrepokemon[47] = "HITMONLEE"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "105"
							pokemon[4] = "79"
							pokemon[5] = "76"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Doble Patada"
							tipoataque[1] = pokemon[0]
							pp[1] = "30"
							efectivo[1] = "100"
							dano[1] = "30"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 48
						if eleccionpoke==48:
							nombrepokemon[48] = "HITMONCHAN"
							pokemon[0] = "LUCHA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "50"
							pokemon[3] = "105"
							pokemon[4] = "79"
							pokemon[5] = "76"
							pokemon[6] = "35"
							nombreataque[0] = "Golpe Karate"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "50"
							nombreataque[1] = "Contador"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Patada Giro"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "85"
							dano[2] = "60"
							nombreataque[3] = "Patada Salto"
							tipoataque[3] = pokemon[0]
							pp[3] = "25"
							efectivo[3] = "95"
							dano[3] = "85"
						# POKEMON 49
						if eleccionpoke==49:
							nombrepokemon[49] = "LICKITUNG"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "55"
							pokemon[4] = "75"
							pokemon[5] = "30"
							pokemon[6] = "60"
							nombreataque[0] = "Mega Puño"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON 50
						if eleccionpoke==50:
							nombrepokemon[50] = "KOFFING"
							pokemon[0] = "VENENO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "65"
							pokemon[4] = "95"
							pokemon[5] = "35"
							pokemon[6] = "60"
							nombreataque[0] = "Acido"
							tipoataque[0] = pokemon[0]
							pp[0] = "30"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Polvo Veneno"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "75"
							dano[1] = "0"
							nombreataque[2] = "Residuos"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "95"
							dano[2] = "65"
							nombreataque[3] = "Armadura Acida"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 51
						if eleccionpoke==51:
							nombrepokemon[51] = "RHYHORN"
							pokemon[0] = "ROCA"
							pokemon[1] = "TIERRA"
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "85"
							pokemon[4] = "95"
							pokemon[5] = "25"
							pokemon[6] = "30"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Avalancha"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "90"
							dano[1] = "75"
							nombreataque[2] = "Excavar"
							tipoataque[2] = pokemon[1]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Lanza Rocas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "90"
							dano[3] = "50"
						# POKEMON 52
						if eleccionpoke==52:
							nombrepokemon[52] = "CHANSEY"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "250"
							pokemon[3] = "5"
							pokemon[4] = "5"
							pokemon[5] = "5"
							pokemon[6] = "50"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Chirridos"
							tipoataque[3] = pokemon[0]
							pp[3] = "40"
							efectivo[3] = "85"
							dano[3] = "0"
						# POKEMON
						if eleccionpoke==53:
							nombrepokemon[53] = "TANGELA"
							pokemon[0] = "PLANTA"
							pokemon[1] = "VENENO"
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "55"
							pokemon[4] = "115"
							pokemon[5] = "60"
							pokemon[6] = "100"
							nombreataque[0] = "Absorber"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "20"
							nombreataque[1] = "Agotamiento"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Polvo Veneno"
							tipoataque[2] = pokemon[1]
							pp[2] = "35"
							efectivo[2] = "75"
							dano[2] = "0"
							nombreataque[3] = "Drenadoras"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "90"
							dano[3] = "0"
						# POKEMON
						if eleccionpoke==54:
							nombrepokemon[54] = "KANGASKHAN"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "105"
							pokemon[3] = "95"
							pokemon[4] = "80"
							pokemon[5] = "90"
							pokemon[6] = "40"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Arañaso"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if eleccionpoke==55:
							nombrepokemon[55] = "HORSEA"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "40"
							pokemon[4] = "70"
							pokemon[5] = "60"
							pokemon[6] = "70"
							nombreataque[0] = "Pistol de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Rayo Burbuja"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Surf"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "100"
						# POKEMON 
						if eleccionpoke==56:
							nombrepokemon[56] = "GOLDEEN"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "45"
							pokemon[3] = "67"
							pokemon[4] = "60"
							pokemon[5] = "63"
							pokemon[6] = "50"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "95"
							dano[2] = "100"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if eleccionpoke==57:
							nombrepokemon[57] = "STARYU"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "45"
							pokemon[4] = "55"
							pokemon[5] = "85"
							pokemon[6] = "70"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Cascada"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "100"
							dano[1] = "80"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if eleccionpoke==58:
							nombrepokemon[58] = "MR.MIME"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "40"
							pokemon[3] = "45"
							pokemon[4] = "65"
							pokemon[5] = "90"
							pokemon[6] = "100"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Descanso"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if eleccionpoke==59:
							nombrepokemon[59] = "SCYTHER"
							pokemon[0] = "BICHO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "70"
							pokemon[3] = "110"
							pokemon[4] = "80"
							pokemon[5] = "105"
							pokemon[6] = "55"
							nombreataque[0] = "Doble Ataque"
							tipoataque[0] = pokemon[0]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "80"
							nombreataque[1] = "Pin Misile"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Disparo Demora"
							tipoataque[2] = pokemon[0]
							pp[2] = "40"
							efectivo[2] = "95"
							dano[2] = "0"
							nombreataque[3] = "Ataque Ala"
							tipoataque[3] = pokemon[1]
							pp[3] = "35"
							efectivo[3] = "100"
							dano[3] = "60"
						# POKEMON 
						if eleccionpoke==60:
							nombrepokemon[60] = "JYNX"
							pokemon[0] = "HIELO"
							pokemon[1] = "PSIQUICO"
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "50"
							pokemon[4] = "35"
							pokemon[5] = "95"
							pokemon[6] = "95"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[1]
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Puño Hielo"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "15"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = pokemon[1]
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Doble Bofeton"
							tipoataque[3] = "NORMAL"
							pp[3] = "10"
							efectivo[3] = "85"
							dano[3] = "15"
						# POKEMON 
						if eleccionpoke==61:
							nombrepokemon[61] = "ELECTABUZZ"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "83"
							pokemon[4] = "57"
							pokemon[5] = "105"
							pokemon[6] = "85"
							nombreataque[0] = "Puño Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "75"
							nombreataque[1] = "Golpe Karate"
							tipoataque[1] = "LUCHA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "50"
							nombreataque[2] = "Mega Puño"
							tipoataque[2] = "NORMAL"
							pp[2] = "20"
							efectivo[2] = "85"
							dano[2] = "80"
							nombreataque[3] = "Rayo"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 
						if eleccionpoke==62:
							nombrepokemon[62] = "MAGMAR"
							pokemon[0] = "FUEGO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "95"
							pokemon[4] = "57"
							pokemon[5] = "93"
							pokemon[6] = "85"
							nombreataque[0] = "Ascuas"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = pokemon[0]
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Puño Fuego"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "75"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "35"
						# POKEMON 
						if eleccionpoke==63:
							nombrepokemon[63] = "PINSIR"
							pokemon[0] = "BICHO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "125"
							pokemon[4] = "100"
							pokemon[5] = "85"
							pokemon[6] = "55"
							nombreataque[0] = "Destructor"
							tipoataque[0] = "NORMAL"
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Pin Misille"
							tipoataque[1] = pokemon[0]
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "14"
							nombreataque[2] = "Cornada"
							tipoataque[2] = "NORMAL"
							pp[2] = "25"
							efectivo[2] = "100"
							dano[2] = "65"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON
						if eleccionpoke==64:
							nombrepokemon[64] = "TAUROS"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "75"
							pokemon[3] = "100"
							pokemon[4] = "95"
							pokemon[5] = "110"
							pokemon[6] = "70"
							nombreataque[0] = "Terremoto"
							tipoataque[0] = "TIERRA"
							pp[0] = "20"
							efectivo[0] = "85"
							dano[0] = "80"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "95"
						# POKEMON 
						if eleccionpoke==65:
							nombrepokemon[65] = "MAGIKARP"
							pokemon[0] = "AGUA"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "20"
							pokemon[3] = "10"
							pokemon[4] = "55"
							pokemon[5] = "80"
							pokemon[6] = "20"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Hidro Bomba"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Placaje"
							tipoataque[3] = "NORMAL"
							pp[3] = "35"
							efectivo[3] = "95"
							dano[3] = "95"
						# POKEMON 
						if eleccionpoke==66:
							nombrepokemon[66] = "LAPRAS"
							pokemon[0] = "AGUA"
							pokemon[1] = "HIELO"
							# Salud
							pokemon[2] = "130"
							pokemon[3] = "85"
							pokemon[4] = "80"
							pokemon[5] = "60"
							pokemon[6] = "95"
							nombreataque[0] = "Pistola de Agua"
							tipoataque[0] = pokemon[0]
							pp[0] = "25"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "HIDRO BOMBA"
							tipoataque[1] = pokemon[0]
							pp[1] = "5"
							efectivo[1] = "80"
							dano[1] = "120"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Rayo Aurora"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if eleccionpoke==67:
							nombrepokemon[67] = "DITTO"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "48"
							pokemon[3] = "48"
							pokemon[4] = "48"
							pokemon[5] = "48"
							pokemon[6] = "48"
							nombreataque[0] = "Transformacion"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = ""
							tipoataque[1] = ""
							pp[1] = ""
							efectivo[1] = ""
							dano[1] = ""
							nombreataque[2] = ""
							tipoataque[2] = ""
							pp[2] = ""
							efectivo[2] = ""
							dano[2] = ""
							nombreataque[3] = ""
							tipoataque[3] = ""
							pp[3] = ""
							efectivo[3] = ""
							dano[3] = ""
						# POKEMON 
						if eleccionpoke==68:
							nombrepokemon[68] = "EEVEE"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "55"
							pokemon[3] = "55"
							pokemon[4] = "50"
							pokemon[5] = "55"
							pokemon[6] = "65"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Ataque Arena"
							tipoataque[1] = "TIERRA"
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Doble Bofeton"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "85"
							dano[2] = "15"
							nombreataque[3] = "Placaje"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "100"
							dano[3] = "95"
						# POKEMON 
						if eleccionpoke==69:
							nombrepokemon[69] = "PORYGON"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "65"
							pokemon[3] = "60"
							pokemon[4] = "70"
							pokemon[5] = "40"
							pokemon[6] = "75"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = "PSIQUICO"
							pp[0] = "20"
							efectivo[0] = "100"
							dano[0] = "65"
							nombreataque[1] = "Destructor"
							tipoataque[1] = pokemon[0]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "40"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Impactrueno"
							tipoataque[3] = "ELECTRICO"
							pp[3] = "30"
							efectivo[3] = "100"
							dano[3] = "40"
						# POKEMON 
						if eleccionpoke==70:
							nombrepokemon[70] = "OMANYTE"
							pokemon[0] = "ROCA"
							pokemon[1] = "AGUA"
							# Salud
							pokemon[2] = "35"
							pokemon[3] = "40"
							pokemon[4] = "100"
							pokemon[5] = "35"
							pokemon[6] = "90"
							nombreataque[0] = "Hidro Bomba"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "80"
							dano[0] = "120"
							nombreataque[1] = "Absorber"
							tipoataque[1] = "PLANTA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "20"
							nombreataque[2] = "Excavar"
							tipoataque[2] = "TIERRA"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "60"
							nombreataque[3] = "Lanza Rocas"
							tipoataque[3] = pokemon[0]
							pp[3] = "15"
							efectivo[3] = "90"
							dano[3] = "50"
						# POKEMON 
						if eleccionpoke==71:
							nombrepokemon[71] = "KABUTO"
							pokemon[0] = "ROCA"
							pokemon[1] = "AGUA"
							# Salud
							pokemon[2] = "30"
							pokemon[3] = "80"
							pokemon[4] = "90"
							pokemon[5] = "55"
							pokemon[6] = "45"
							nombreataque[0] = "Hidro Bomba"
							tipoataque[0] = pokemon[1]
							pp[0] = "5"
							efectivo[0] = "80"
							dano[0] = "120"
							nombreataque[1] = "Absorber"
							tipoataque[1] = "PLANTA"
							pp[1] = "25"
							efectivo[1] = "100"
							dano[1] = "20"
							nombreataque[2] = "Surf"
							tipoataque[2] = pokemon[1]
							pp[2] = "15"
							efectivo[2] = "100"
							dano[2] = "95"
							nombreataque[3] = "Rayo Burbuja"
							tipoataque[3] = pokemon[1]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if eleccionpoke==72:
							nombrepokemon[72] = "AERODACTYL"
							pokemon[0] = "ROCA"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "80"
							pokemon[3] = "105"
							pokemon[4] = "65"
							pokemon[5] = "130"
							pokemon[6] = "60"
							nombreataque[0] = "Ataque Ala"
							tipoataque[0] = pokemon[1]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "60"
							nombreataque[1] = "Lanza LLamas"
							tipoataque[1] = "FUEGO"
							pp[1] = "15"
							efectivo[1] = "100"
							dano[1] = "95"
							nombreataque[2] = "Lanza Rocas"
							tipoataque[2] = pokemon[0]
							pp[2] = "15"
							efectivo[2] = "90"
							dano[2] = "50"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = "PSIQUICO"
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if eleccionpoke==73:
							nombrepokemon[73] = "SNORLAX"
							pokemon[0] = "NORMAL"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "160"
							pokemon[3] = "110"
							pokemon[4] = "65"
							pokemon[5] = "30"
							pokemon[6] = "65"
							nombreataque[0] = "Destructor"
							tipoataque[0] = pokemon[0]
							pp[0] = "35"
							efectivo[0] = "100"
							dano[0] = "40"
							nombreataque[1] = "Descanso"
							tipoataque[1] = "PSIQUICO"
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Placaje"
							tipoataque[2] = pokemon[0]
							pp[2] = ""
							efectivo[2] = ""
							dano[2] = ""
							nombreataque[3] = "Doble Bofeton"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "85"
							dano[3] = "15"
						# POKEMON 
						if eleccionpoke==74:
							nombrepokemon[74] = "ARTICUNO"
							pokemon[0] = "HIELO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "85"
							pokemon[4] = "100"
							pokemon[5] = "85"
							pokemon[6] = "125"
							nombreataque[0] = "Rayo Hielo"
							tipoataque[0] = pokemon[0]
							pp[0] = "16"
							efectivo[0] = "100"
							dano[0] = "90"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Rayo Aurora"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "65"
						# POKEMON 
						if eleccionpoke==75:
							nombrepokemon[75] = "ZAPDOS"
							pokemon[0] = "ELECTRICO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "90"
							pokemon[4] = "85"
							pokemon[5] = "100"
							pokemon[6] = "125"
							nombreataque[0] = "Trueno"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "70"
							dano[0] = "120"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Amnesia"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "20"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Impactrueno"
							tipoataque[3] = pokemon[0]
							pp[3] = "10"
							efectivo[3] = "100"
							dano[3] = "90"
						# POKEMON 
						if eleccionpoke==76:
							nombrepokemon[76] = "MOLTRES"
							pokemon[0] = "FUEGO"
							pokemon[1] = "VOLADOR"
							# Salud
							pokemon[2] = "90"
							pokemon[3] = "100"
							pokemon[4] = "90"
							pokemon[5] = "90"
							pokemon[6] = "125"
							nombreataque[0] = "Lanza LLamas"
							tipoataque[0] = pokemon[0]
							pp[0] = "15"
							efectivo[0] = "100"
							dano[0] = "95"
							nombreataque[1] = "Ataque Ala"
							tipoataque[1] = pokemon[1]
							pp[1] = "35"
							efectivo[1] = "100"
							dano[1] = "60"
							nombreataque[2] = "Descanso"
							tipoataque[2] = "PSIQUICO"
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "0"
							nombreataque[3] = "Ataque Psiquico"
							tipoataque[3] = "PSIQUICO"
							pp[3] = "10"
							efectivo[3] = "100"
							dano[3] = "90"
						# POKEMON 
						if eleccionpoke==77:
							nombrepokemon[77] = "DRATINI"
							pokemon[0] = "DRAGON"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "41"
							pokemon[3] = "64"
							pokemon[4] = "45"
							pokemon[5] = "50"
							pokemon[6] = "50"
							nombreataque[0] = "Furia Dragon"
							tipoataque[0] = pokemon[0]
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Descanso"
							tipoataque[1] = "PSIQUICO"
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "0"
							nombreataque[2] = "Placaje"
							tipoataque[2] = "NORMAL"
							pp[2] = "35"
							efectivo[2] = "95"
							dano[2] = "35"
							nombreataque[3] = "Surf"
							tipoataque[3] = "AGUA"
							pp[3] = "15"
							efectivo[3] = "95"
							dano[3] = "100"
						# POKEMON 
						if eleccionpoke==78:
							nombrepokemon[78] = "MEWTWO"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "106"
							pokemon[3] = "110"
							pokemon[4] = "90"
							pokemon[5] = "130"
							pokemon[6] = "154"
							nombreataque[0] = "Psico Rayo"
							tipoataque[0] = pokemon[0]
							pp[0] = ""
							efectivo[0] = ""
							dano[0] = "65"
							nombreataque[1] = "Mega Puño"
							tipoataque[1] = "NORMAL"
							pp[1] = "20"
							efectivo[1] = "85"
							dano[1] = "80"
							nombreataque[2] = "Ataque Psiquico"
							tipoataque[2] = pokemon[0]
							pp[2] = "10"
							efectivo[2] = "100"
							dano[2] = "90"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# POKEMON 
						if eleccionpoke==79:
							nombrepokemon[79] = "MEW"
							pokemon[0] = "PSIQUICO"
							pokemon[1] = ""
							# Salud
							pokemon[2] = "100"
							pokemon[3] = "100"
							pokemon[4] = "100"
							pokemon[5] = "100"
							pokemon[6] = "100"
							nombreataque[0] = "Transformacion"
							tipoataque[0] = "NORMAL"
							pp[0] = "10"
							efectivo[0] = "100"
							dano[0] = "0"
							nombreataque[1] = "Psico Rayo"
							tipoataque[1] = pokemon[0]
							pp[1] = "10"
							efectivo[1] = "100"
							dano[1] = "65"
							nombreataque[2] = "Mega Puño"
							tipoataque[2] = pokemon[0]
							pp[2] = "20"
							efectivo[2] = "85"
							dano[2] = "80"
							nombreataque[3] = "Amnesia"
							tipoataque[3] = pokemon[0]
							pp[3] = "20"
							efectivo[3] = "100"
							dano[3] = "0"
						# LISTA DE POKEMONES USUARIO
						# BUSQUEDA DE POKEMON ENEMIGO
						if z==2:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							enepoke[1] = nombrepokemon[eleccionpoke]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							enepoket2[0] = pokemon[0]
							# Guarda el Tipo 2
							enepoket2[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							enepokeh2[0] = float(pokemon[2])
							# ATAQUE
							enepokeh2[1] = float(pokemon[3])
							# DEFENSA
							enepokeh2[2] = float(pokemon[4])
							# VELOCIDAD
							enepokeh2[3] = float(pokemon[5])
							# ESPECIAL
							enepokeh2[4] = float(pokemon[6])
							enesalud[1] = enepokeh2[0]
							for contx in range(4):
								nombree2[contx] = nombreataque[contx]
								tipoe2[contx] = tipoataque[contx]
								ppe2[contx] = float(pp[contx])
								efectivoe2[contx] = float(efectivo[contx])
								ppfe2[contx] = float(pp[contx])
								danoe2[contx] = float(dano[contx])
						if z==3:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							enepoke[2] = nombrepokemon[eleccionpoke]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							enepoket3[0] = pokemon[0]
							# Guarda el Tipo 2
							enepoket3[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							enepokeh3[0] = float(pokemon[2])
							# ATAQUE
							enepokeh3[1] = float(pokemon[3])
							# DEFENSA
							enepokeh3[2] = float(pokemon[4])
							# VELOCIDAD
							enepokeh3[3] = float(pokemon[5])
							# ESPECIAL 
							enepokeh3[4] = float(pokemon[6])
							enesalud[2] = enepokeh3[0]
							for contx in range(4):
								nombree3[contx] = nombreataque[contx]
								tipoe3[contx] = tipoataque[contx]
								ppe3[contx] = float(pp[contx])
								ppfe3[contx] = float(pp[contx])
								efectivoe3[contx] = float(efectivo[contx])
								danoe3[contx] = float(dano[contx])
						if z==4:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							enepoke[3] = nombrepokemon[eleccionpoke]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							enepoket4[0] = pokemon[0]
							# Guarda el Tipo 2
							enepoket4[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							enepokeh4[0] = float(pokemon[2])
							# ATAQUE
							enepokeh4[1] = float(pokemon[3])
							# DEFENSA
							enepokeh4[2] = float(pokemon[4])
							# VELOCIDAD
							enepokeh4[3] = float(pokemon[5])
							# ESPECIAL 
							enepokeh4[4] = float(pokemon[6])
							enesalud[3] = enepokeh4[0]
							for contx in range(4):
								nombree4[contx] = nombreataque[contx]
								tipoe4[contx] = tipoataque[contx]
								ppe4[contx] = float(pp[contx])
								ppfe4[contx] = float(pp[contx])
								efectivoe4[contx] = float(efectivo[contx])
								danoe4[contx] = float(dano[contx])
						if z==5:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							enepoke[4] = nombrepokemon[eleccionpoke]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							enepoket5[0] = pokemon[0]
							# Guarda el Tipo 2
							enepoket5[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							enepokeh5[0] = float(pokemon[2])
							# ATAQUE
							enepokeh5[1] = float(pokemon[3])
							# DEFENSA
							enepokeh5[2] = float(pokemon[4])
							# VELOCIDAD
							enepokeh5[3] = float(pokemon[5])
							# ESPECIAL
							enepokeh5[4] = float(pokemon[6])
							enesalud[4] = enepokeh5[0]
							for contx in range(4):
								nombree5[contx] = nombreataque[contx]
								tipoe5[contx] = tipoataque[contx]
								ppe5[contx] = float(pp[contx])
								ppfe5[contx] = float(pp[contx])
								efectivoe5[contx] = float(efectivo[contx])
								danoe5[contx] = float(dano[contx])
						if z==6:
							# Guarda el nombre del pokemon 1 que voy a ocupar
							enepoke[5] = nombrepokemon[eleccionpoke]
							# TIPO DEL POKE
							# Guarda el Tipo 1 del pokemon
							enepoket6[0] = pokemon[0]
							# Guarda el Tipo 2
							enepoket6[1] = pokemon[1]
							# Habilidad del poke 1
							# SALUD
							enepokeh6[0] = float(pokemon[2])
							# ATAQUE
							enepokeh6[1] = float(pokemon[3])
							# DEFENSA
							enepokeh6[2] = float(pokemon[4])
							# VELOCIDAD
							enepokeh6[3] = float(pokemon[5])
							# ESPECIAL 
							enepokeh6[4] = float(pokemon[6])
							enesalud[5] = enepokeh6[0]
							for contx in range(4):
								nombree6[contx] = nombreataque[contx]
								tipoe6[contx] = tipoataque[contx]
								ppe6[contx] = float(pp[contx])
								efectivoe6[contx] = float(efectivo[contx])
								ppfe6[contx] = float(pp[contx])
								danoe6[contx] = float(dano[contx])
			# ***************************************************************************
			# ***     xxxxxx  xx   xx xx xxxxxxxxx    ***********************************
			# ***     xx       xx xx  xx    xx        ***********************************
			# ***     xxxxxx    xxx   xx    xx        ***********************************
			# ***     xx       xx xx  xx    xx        ***********************************
			# ***     xxxxxx  xx   xx xx    xx        ***********************************
			# ***************************************************** OPCION 4 *************************************
			# ******************************************************SALIR DEL JUEGO*******************************
			# ******************************************************SALIR DEL JUEGO*******************************
			if opc3==4:
				while True:# no hay 'repetir' en python
					print("¿Estas seguro que quieres salir?, si o no ")
					saliropc = input()
					if saliropc=="si" or saliropc=="SI" or saliropc=="no" or saliropc=="NO": break
				if saliropc=="SI" or saliropc=="si":
					opc = 2
	if opc==2:
		print("")
		print("")
		print("")
		print("                 Fin del Juego")
		print("")
		if win>0:
			print("        Partidas Guardadas ",win)
		else:
			print("")
		print("")
		print("")
		sleep(2)
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|        D  U  O  C         |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|   S A N  B E R N A R D O  |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|        2  0  1  6         |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|        D  U  O  C         |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|   S A N  B E R N A R D O  |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|        2  0  1  6         |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|      A N A L I S I S      |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX| CARLOS ORELLANA           |XXXXXXXXXX")
		print("XXXXXXXXXX|            &              |XXXXXXXXXX")
		print("XXXXXXXXXX|              CARLOS CERDA |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX| P R O G R A M A D O R E S |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX| BENJAMIN MORA             |XXXXXXXXXX")
		print("XXXXXXXXXX|            &              |XXXXXXXXXX")
		print("XXXXXXXXXX|           CARLOS ORELLANA |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|  L I S T A D O  P O K E   |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|       MELANIE ORDEN       |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|       P R O F E S O R     |XXXXXXXXXX")
		print("XXXXXXXXXX|                           |XXXXXXXXXX")
		print("XXXXXXXXXX|          IGNACIO V.       |XXXXXXXXXX")
		print("XXXXXXXXXX| PROGRAMCION               |XXXXXXXXXX")
		print("XXXXXXXXXX|             DE            |XXXXXXXXXX")
		print("XXXXXXXXXX|               ALGORITMO   |XXXXXXXXXX")
		print("XXXXXXXXXX@---------------------------@XXXXXXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxXXXXX")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		sleep(2)
	print("") # no hay forma directa de borrar la pantalla con Python estandar
	print("")
	print("  D U O C  2 0 1 6               .::. ")
	print("                               .;:** ")
	print("                               `")
	print("   .:XHHHHk.              db.   .;;.     dH  MX  ")
	print("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN")
	print("QMMMMMb   MMX       MMMMMMP  MX   M~   MMM MMM  .oo. XMMM   ´MMM")
	print("  `MMMM.  )M> :X!Hk. MMMM   XMM.o   .  MMMMMMM X?XMMM MMM> !MMP")
	print("   ´MMMb.dM! XM M´?M MMMMMX.`MMMMMMMM~ MM M MM XM `  MX MMX XMM")
	print("    ~MMMMM~ XMM. .XM XM` MMMb.~~MMMM~.MMX M  t MMbooMM XM MMMMP")
	print("     ?MMM>  YMMMMMM! MM   `?MMRb.    `       !L MMMMM XM  IMMM")
	print("      MMMX    MMMM   MM       ~%:            !Mh.  dMI     IMMP")
	print("      ´MMM.                                                IMX")
	print("       ~M!M                                                 BMT")
	print("                      A M A R I L L O ")
	print("")
	input() # a diferencia del pseudocódigo, espera un Enter, no cualquier tecla

