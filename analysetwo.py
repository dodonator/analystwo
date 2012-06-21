import os
import time
import datetime
os.system('clear')
def zahlenAnalyse(toAnalyse):
	zahlen = ['0','1','2','3','4','5','6','7','8','9']
	counterUltimate = {}	
	#toAnalyse = raw_input('Gib bitte eine Zahl ein:\n')
	for Counter1 in range(len(toAnalyse)):
		if toAnalyse[Counter1] in zahlen:
			#for Counter2 in range(len(zahlen)):
			#if toAnalyse[Counter1] == zahlen[Counter2]:
			if toAnalyse[Counter1] in counterUltimate:
				counterUltimate[toAnalyse[Counter1]] += 1
			else:
				counterUltimate[toAnalyse[Counter1]] = 1
	ausgabe = ''
	for key, value in counterUltimate.items():
		ausgabe += str(key) + ' --> ' + str(value) + '\n'		
	return ausgabe

	
def analyse(text):
	alphaKl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alphaGr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	zahlen = ['0','1','2','3','4','5','6','7','8','9']
	mathChar = ['+','-','*','/','(',')','[',']','=','^','<','>']
	satzZeichen = ['.','!','?',',',';',':','"']
	analyseB = []
	mathCharCounter = 0
	leerCounter = 0
	sazCounter = 0
	buchstabenCounter = {}
	buchstabenCounter2 = 0
	
	
	#for C7 in range(26):
	#	buchstabenCounter.append(0)
	os.system('clear')
	dataname = raw_input('Gib bitte einen Dateinamen ein!\n')
	#text = raw_input('Gib bitte einen Text zur Analyse ein:\n')
	for C1 in range(len(text)):
		if text[C1] in alphaKl or text[C1] in alphaGr: 
			for C6 in range(26):
				if text[C1] == alphaKl[C6] or text[C1] == alphaGr[C6]:
					buchstabenCounter2 += 1
					if text[C1] in buchstabenCounter:
						buchstabenCounter[text[C1]] += 1
					else:
						buchstabenCounter[text[C1]] = 1
						

		elif text[C1] in mathChar:
			mathCharCounter += 1
		elif text[C1] in satzZeichen:
			sazCounter += 1
		elif text[C1] == ' ':
			leerCounter += 1
	Analyse = ''
	clock = time.localtime()
	year = str(clock[0])
	month = str(clock[1])
	day = str(clock[2])
	hour = str(clock[3])
	minute = str(clock[4])
	second = str(clock[5])
	datum = 'Analyse vom: ' + day + '.' + month + '.' + year + '  Um: ' + hour + ':' + minute + ':' + second
	Analyse += datum + '\n' + 'Buchstabenanalyse: \n'
	
	analyseM = 'Mathematische Zeichen: ' + str(mathCharCounter) + '\n'
	#vokale = buchstabenCounter['A'] + buchstabenCounter['E'] + buchstabenCounter['I'] + buchstabenCounter['O'] + buchstabenCounter['U']
	#analyseV = 'Vokale: ' + str(vokale) + '\n'
	#analyseK = 'Konsonanten: ' + str(buchstabenCounter2 - vokale) + '\n'
	analyseS = 'Satzzeichen: ' + str(sazCounter) + '\n'
	analyseL = 'Leerzeichen: ' + str(leerCounter) + '\n'
	
	for key, value in buchstabenCounter.items():
		Analyse += key + ' --> ' + str(value) + '\n'
	zahlen = zahlenAnalyse(text)
	#for C9 in range(26):
	#	Analyse += alphaGr[C9] + ': ' + str(buchstabenCounter[C9]) + '\n'
	#for C10 in range(len(analyseB)):
	#	print analyseB[C10]
	Analyse += zahlen
	Analyse += 'Andere Analysefaktoren: \n'
	#Analyse += analyseV
	#Analyse += analyseK
	Analyse += analyseS
	Analyse += analyseM
	Analyse += analyseL
	
	
	
	
	text1 = open(dataname + '.txt','w')
	t1 = text1.write(Analyse)
	text1.close()
	ende = ''
	while ende != '1':
		print 'Geben Sie "0" ein, um die Analyse in gedit zu oeffnen!'
		print 'Geben Sie "1" ein, um das Programm zu beenden!'
		print 'Geben Sie "2" ein, um einen neuen Text einzugeben!'
		ende = raw_input(':')
		if ende == '0':
			os.system('gedit ' + dataname + '.txt &')
			time.sleep(2)
			os.system('clear')
		elif ende == '1':
			os.system('clear')
			print '000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
			print '0         00           00           00      000000      0000 0000000 00        00  0'
			print '0 0000000000 000000000 00 000000000 00 000000 0000 00000 0000 00000 000 000000000  0'
			print '0 0000000000 000000000 00 000000000 00 000000 0000 000000 0000 000 0000 000000000  0'
			print '0 0000000000 000000000 00 000000000 00 000000 0000        00000 0 00000        00  0'
			print '0 0000    00 000000000 00 000000000 00 000000 0000        000000 000000        00  0'
			print '0 0000000 00 000000000 00 000000000 00 000000 0000 000000 000000 000000 000000000000'
			print '0 0000000 00 000000000 00 000000000 00 000000 0000 00000 0000000 000000 000000000  0'
			print '0         00           00           00      000000      00000000 000000        00  0'
			print '000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
		elif ende == '2':
			text = raw_input('Gib bitte einen Text zur Analyse ein:\n')
			analyse(text)
			
	

text = raw_input('Gib bitte einen Text zur Analyse ein:\n')
analyse(text)
												
