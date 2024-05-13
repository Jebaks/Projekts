import random
import re
def stop(x): #Funkcija lai apstādinātu programu
    if x == 'stop':
        print('Programma tiek apstādināta, jauku dienu!')
        exit()

def atkartojas(apskata):
    return bool(len(apskata) != len(set(apskata)))

def sajaukts(sajauktais): #Funkcija sajauc sarakstu izmantojot importu "random"
 
    jauns = sorted(sajauktais, key=lambda x: random.random())
    return jauns

def ievade(): #Funkcija kurā lietotājs ievada .txt faila nosaukumu, kurā atrodas personu saraksts
    global turpinat
    global fails
    try:
        nosaukums = input('Ievadiet jūsu faila nosaukumu(bez ".txt"): ')
        stop(nosaukums)
        parbaude = nosaukums.split('.')
        if parbaude[1] == 'txt':
            nosaukums = parbaude[0]+'.txt'
        fails = open(nosaukums,'r',encoding='UTF-8')
        try:
            fails = open(nosaukums,'r',encoding='UTF-8')
            turpinat = 'j'
        except FileNotFoundError: 
            print('Fails netika atrasts!')
            ievade()
        except Exception as e:
            print(f'Kļūda: Neparedzēta kļūda - {e}')
            ievade()  

    except IndexError:
        nosaukums = nosaukums+'.txt'  
        try:
            fails = open(nosaukums,'r',encoding='UTF-8')
            turpinat = 'j'
        except FileNotFoundError: 
            print('Fails netika atrasts!')
            ievade()
        except Exception as e:
            print(f'Kļūda: Neparedzēta kļūda - {e}')
            ievade()



    except FileNotFoundError: 
        print('Fails netika atrasts!')
        ievade()
    except Exception as e:
            print(f'Kļūda: Neparedzēta kļūda - {e}')
            ievade() 

    if turpinat == 'j':
        return fails


saraksts = ievade().readlines()
saraksts = ''.join(saraksts)
saraksts = saraksts.split('\n')
jaukt = sajaukts(saraksts) #Jauktais saraksts



def specifikacija(): #Funkcija kurā tiek apkopota visa ievadītā informācija no lietotāja

    while True:
        skaits = input('Cik grupās Jūs vēlaties sadalīt?(vesels skaitlis): ')
        if skaits.isdigit():
            break
        else:
            print('Ievadiet veselu skaitli!')
            continue

    stop(skaits)
    jauta1 = input('Vai jūs vēlaties pielikt kritērijus?\n(T.i. izvēlēties skolēnus kuri nedrīkst būt vienā grupā un\nizvēlēties skolēnus kuriem obligāti ir jābūt vienā grupā)\n(jā/nē): ')
    stop(jauta1)
    if jauta1 == 'jā':
        for i in range(len(jaukt)):
            print(f'{i+1} - {jaukt[i]}')

        nevar = []
        var = []

        nevar_grupa = input('Ievadiet skolēnu kārtas numurus, kuri nevar būt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(1,3;5,2): ')
        stop(nevar_grupa)
        nevar = nevar_grupa.split(';')

        while True:
            var_grupa = input('Ievadiet skolēnu kārtas numurus, kuriem jābūt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(2,3;4,5): ')
            stop(var_grupa)
            parbaude = re.split(',|;', var_grupa)
            if atkartojas(parbaude) == False:
                break
            else:
                print('Viens skolēns nevar būt divās grupās!')
                continue
        var = var_grupa.split(';')
            

    elif jauta1 == 'nē':
        var = 0
        nevar = 0

    return skaits, nevar, var

skaits, nevar, var = specifikacija()

skoleni = [jaukt[i] for i in range(len(jaukt))]

skolIznemti = []
objekti = [[] for i in range(int(skaits))]
if nevar == 0:
    ...
elif nevar[0] == '0':
    ...
else:
    for i in range (len(nevar)):
        x = nevar[i-1].split(',')
        for j in range(len(x)):
            objekti[j+i].append(skoleni[(int(x[j-1])-1)])
            skolIznemti.append(int(x[j-1])-1)
if var == 0:
    ...
elif var[0] == '0':
    ...
else:
    for i in range (len(var)):
        y = var[i-1].split(',')
        for j in range(len(y)):
            objekti[i].append(skoleni[(int(y[j-1])-1)])
            skolIznemti.append(int(y[j-1])-1)
    skolIznemti.sort(reverse=True)
    for i in range (len(skolIznemti)):
        skoleni.pop(skolIznemti[i])

while len(skoleni) > 0:
    for i in range(len(objekti)):
        if len(skoleni) == 0:
            objekti[i].append(' ')
        else:
            objekti[objekti.index(min(objekti, key=len))].append(skoleni[0])
            skoleni.pop(0)

for i in range(len(objekti)):
    for j in objekti[i]:
        if j == ' ':
            objekti[i].remove(' ')
        else:
            ...
print(objekti)