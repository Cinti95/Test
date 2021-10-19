# -*- coding:Utf-8 -*-

rekesz = input("Adja meg a rendelt rekeszek darabszámát (5-10):") #Bekérjük a rekeszek számát
r = int(rekesz)                                                   #A karakterlánc konvertálása egésszé
almák = input("Adja meg a mai napon leszüretelt almák darabszámát (100 - 200)")
a = int(almák)
arekesz = a/12                                                    # A napi rekeszek száma
if arekesz > r:
    print ("A rendelt mennyiség teljesíthető")
else:
    print ("A rendelt mennyiség nem teljesíthető, max.", int(arekesz), "rekeszt lehet értékesíteni")