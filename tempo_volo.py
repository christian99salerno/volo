
print

print "Tempo di Volo"
print "Determina la durata massima di volo conoscendo"
print "la quantita' di carburante ed il consumo orario"

print

carb=input("Carburante (in galloni): ")
cons=input("Consumo Orario (in galloni/h): ")

print 

if(carb<0 or cons<0): 
    print"ERRORE!!!"
    print

else:
    ore=float(carb)/float(cons)
    minuti=(ore-int(ore))*60
    secondi=(minuti-int(minuti))*60
    print "Tempo di volo:",int(ore),"h",int(minuti),"min",int(secondi),"sec"
    print 
