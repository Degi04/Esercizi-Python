#De Gironimo Matteo 5A


import csv
def load_data(file):
    count = 1
    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        dicarr= []
        for row in csvreader:
            if count == 1:
                dizionario = dict.fromkeys(row)
                count += 1
            else:
                for i in dizionario:
                    el = row[list(dizionario).index(i)]
                    dizionario[i] = el
                dicarr.append(dizionario.copy())

    return dicarr


def printStructindex(dizionario, index):
        if  (index > 0 and index < len(dizionario)):
            print(dizionario[index])
        else:
            return print("no right index")


def mediaCostoBiglietto(dizionario):
    costotot=0
    for i in range(len(dizionario)):
        costotot+=float(dizionario[i]["Fare"])
    costotot =costotot /len(dizionario)
    print("costo medio biglietto: ",costotot)

def distribuzioneEta(dizionario):
    count22 = count23 =count24=0
    for i in range(len(dizionario)):
        eta = dizionario[i]["Age"]
        if eta == "22":
            count22 += 1
        elif eta == "23":
            count23 += 1
        elif eta == "24":
            count24 += 1
    print("n-persone con 22 anni: ",count22," ","n-persone con 23 anni: ",count23," ","n-persone con 24 anni: ",count24)
def nomePiuDiffuso(dizionario):
    d = dict()
    for i in range(len(dizionario)):
        valore = dizionario[i]["Name"]
        index = valore.find(".")
        name = valore[index+1:len(valore)].strip()
        if name in d:
            d[name] +=1
        else:
            d[name] = 1
    massimo = max(d, key=d.get)
    minimo = min(d, key=d.get)
    print("nome più frequente: ",massimo)
    print("nome meno frequente: ",minimo)

def percentauleMaschiFemmine(dizionario):
    countM = countF = 0

    for i in range(0, len(dizionario)):
        if(dizionario[i]["Sex"] == "male"):
            countM += 1
        else:
            countF += 1
    print("percentuale maschi: ",round((countM/len(dizionario) )*100), "%") #uso la funzione round per arrotondarmi il risultato per eccesso o difetto
    print("percentuale femmine: ",round((countF/len(dizionario) )*100), "%")    

dizionarioall = load_data("titanic.csv")
mediaCostoBiglietto(dizionarioall)
distribuzioneEta(dizionarioall)
percentauleMaschiFemmine(dizionarioall)
nomePiuDiffuso(dizionarioall)
