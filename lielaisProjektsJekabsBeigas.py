import random
def stop(x): #Funkcija lai apstādinātu programu
    if x == 'stop':
        print('Programma tiek apstādināta, jauku dienu!')
        exit()

def sajaukts(sajauktais): #Funkcija sajauc sarakstu izmantojot importu "random"
 
    jauns = sorted(sajauktais, key=lambda x: random.random())
    return jauns

def ievade(): #Funkcija kurā lietotājs ievada .txt faila nosaukumu, kurā atrodas personu saraksts
    global turpinat
    global fails
    try:
        nosaukums = input('Ievadiet jūsu faila nosaukumu: ')
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

def atkartojas(var, nevar): #funkcija pārbauda, vai tie paši skolēni nav ievadīti gan sarakstā, kuri var būt vienā grupā, gan sarakstā, kuri nevar būt vienā grupā
    for x in var:
        for y in nevar:
            if x in y:
                print('Skolēni nevar būt un nebūt vienā grupā!')
                atkartot = True
            elif y in x:
                print('Skolēni nevar būt un nebūt vienā grupā!')
                atkartot = True
            else:
                atkartot = False
    return atkartot

def specifikacija(): #Funkcija kurā tiek apkopota visa ievadītā informācija no lietotāja

    while True:
        skaits = input('Cik grupās Jūs vēlaties sadalīt?(vesels skaitlis): ')
        stop(skaits)
        if skaits.isdigit(): #Pārbauda vai ievadītais ir vesels skaitlis
            break
        else:
            print('Ievadiet veselu skaitli!')
            continue

    stop(skaits)
    while True:
        jauta1 = input('Vai jūs vēlaties pievienot kritērijus?\n(T.i. izvēlēties skolēnus kuri nedrīkst būt vienā grupā un\nizvēlēties skolēnus kuriem obligāti ir jābūt vienā grupā)\n(jā/nē): ')
        stop(jauta1)
        if jauta1 == 'jā':
            for i in range(len(jaukt)):
                print(f'{i+1} - {jaukt[i]}') #Izvada uz ekrāna sarakstu ar skolēniem

            nevar = []
            var = []

            atkartot = True

            while True:

                if atkartot == True:
                    nevar_grupa = input('Ievadiet skolēnu kārtas numurus, kuri nevar būt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(1,3;5,2): ')
                    stop(nevar_grupa)
                    nevar = nevar_grupa.split(';') #Sadala ievadīto skolēnu grupās, kas nevar būt vienā grupā

                    var_grupa = input('Ievadiet skolēnu kārtas numurus, kuriem jābūt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(2,3;4,5): ')
                    stop(var_grupa)
                    var = var_grupa.split(';') #Sadala ievadīto skolēnu grupās, kas var būt vienā grupā
                    if var[0] == '0':
                        break
                    else:
                        atkartot = atkartojas(var, nevar)
                else:
                    break
            break
        elif jauta1 == 'nē':
            var = 0
            nevar = 0
            break
        else:
            continue
    return skaits, nevar, var

skaits, nevar, var = specifikacija()

skoleni = [jaukt[i] for i in range(len(jaukt))]

skolIznemti = []
objekti = [[] for i in range(int(skaits))] #Izveido sarakstu katrai grupai, kurā ievadīt grupas dalībniekus
if nevar == 0:
    ...
elif nevar[0] == '0':
    ...
else:
    for i in range (len(nevar)):
        x = nevar[i-1].split(',') #Atdala katru skolēnu atsevišķi
        for j in range(len(x)):
            objekti[j+i].append(skoleni[(int(x[j-1])-1)]) #Pievieno skolēnus grupām, nesaliekot skolēnus, kas nevar būt vienā grupā, kopā
            skolIznemti.append(int(x[j-1])-1) #Pievieno skolenus, kas jau ir ievietoti kādā grupā
if var == 0:
    ...
elif var[0] == '0':
    ...
else:
    for i in range (len(var)):
        y = var[i-1].split(',') #Atdala katru skolēnu atsevišķi
        for j in range(len(y)):
            if (skoleni[(int(y[j-1])-1)]) in objekti[i]: #Pārbauda, vai skolēns jau atrodas šajā grupā
                ...
            else:
                objekti[i].append(skoleni[(int(y[j-1])-1)]) #Pievieno skolēnus grupām, saliekot skolēnus kopā, kam jābūt vienā grupā
                skolIznemti.append(int(y[j-1])-1) #Pievieno skolenus, kas jau ir ievietoti kādā grupā
    skolIznemti.sort(reverse=True)
    for i in range (len(skolIznemti)):
        skoleni.pop(skolIznemti[i]) #No saraksta ar skolēniem izņem skolēnus, kas jau ievietoti grupā

while len(skoleni) > 0:
    for i in range(len(objekti)):
        if len(skoleni) == 0:
            objekti[i].append(' ')
        else:
            objekti[objekti.index(min(objekti, key=len))].append(skoleni[0]) #Grupā ar vismazāk skolēniem pievieno skolēnu
            skoleni.pop(0) #No saraksta ar skolēniem izņem skolēnu, kas tika ievietots grupā

for i in range(len(objekti)):
    for j in objekti[i]:
        if j == ' ':
            objekti[i].remove(' ')
        else:
            ...
k = 1
for i in objekti:
    print(f'{k}. grupa:') #Izvada grupas
    for j in range(len(i)):
        print(f'- {i[j]}') #Izvada skolēnus grupās
    print('')
    k += 1