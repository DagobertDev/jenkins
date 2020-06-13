print("Dateset erstellen:")
print("")
calculation=input("Rechnung eingeben:")
calculation_split = calculation.split()
listeCalculations = []
listeHeads = []
listeDep = []
for i in range(0, len(calculation_split)):
   listeCalculations.append(calculation_split[i] + str([i]))

print(listeCalculations)

print("")
print("Heads festlegen:")
for i in range(0, len(calculation_split)):
    heads=input("Heads für " + calculation_split[i] + " : ")
    listeHeads.append(heads + ",")

print(listeHeads)
print("")
print("Dependencies festlegen:")
for i in range(0, len(calculation_split)):
    deps=input("Dependencies für " + calculation_split[i] + " : ").upper()
    listeDep.append("'" + deps + "'")

print(listeDep)

ausgabe = "( \n " + "'" + calculation + "'" +",\n { \n 'heads': [" + ' '.join(listeHeads) + "],\n 'deps': [" + ' '.join(listeDep) + "], \n }, \n ),"
print(ausgabe)
f=open('dataset_Example.txt','a')
f.write(str(ausgabe))






