import random
def stop(x):
    if x == 'stop':
        print('Programma tiek apstādināta, jauku dienu!')
        exit()
def sajaukts(saraksts):
 
    jauns = sorted(saraksts, key=lambda x: random.random())
    return jauns

def ievade():
    global turpinat
    global fails
    try:            
        faila_nosaukums = input('Ievadiet jūsu faila nosaukumu(bez ".txt"): ')
        stop(faila_nosaukums)
        parbaude = faila_nosaukums.split('.')
        if parbaude[1] == 'txt':
            faila_nosaukums = parbaude[0]+'.txt'
        fails = open(faila_nosaukums,'r',encoding='UTF-8')
        try:
            fails = open(faila_nosaukums,'r',encoding='UTF-8')
            turpinat = 'j'
        except FileNotFoundError: 
            print('Fails netika atrasts!')
            ievade()

        except IndexError:
            faila_nosaukums = faila_nosaukums+'.txt'  

        except Exception as e:
            print(f'Kļūda: Neparedzēta kļūda - {e}')
            ievade()  
        
        try:
            fails = open(faila_nosaukums,'r',encoding='UTF-8')
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
sajaukts(saraksts)

def specifikacija():
    grupu_skaits = int(input('Cik grupās Jūs vēlaties sadalīt?: '))
    stop(grupu_skaits)
    jautajums1 = input('Vai jūs vēlaties pielikt kritērijus?\n(T.i. izvēlēties skolēnus kuri nedrīkst būt vienā grupā un\nizvēlēties skolēnus kuriem obligāti ir jābūt vienā grupā)\n(jā/nē): ')
    stop(jautajums1)
    if jautajums1 == 'jā':
        for i in range(len(saraksts)):
            print(f'{i+1} - {saraksts[i]}')

            nevar_but = []
            var_but = []

            nevar_but_viena_grupa = input('Ievadiet skolēnu kārtas numurus, kuri nevar būt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(1,3;5,2):')
            stop(nevar_but_viena_grupa)
            nevar_but = nevar_but_viena_grupa.split(';')

            var_but_viena_grupa = input('Ievadiet skolēnu kārtas numurus, kuriem jābūt vienā grupā, atdalot tos ar komatu, ja ir vairākas skolēnu kopas, tad katru nākamo kopu atdala ar semikolu(2,3;4,5): ')
            stop(var_but_viena_grupa)
            var_but = var_but_viena_grupa.split(';')

    elif jautajums1 == 'nē':
        var_but = 0
        nevar_but = 0

        return grupu_skaits,nevar_but,var_but


idk = int(specifikacija()[0])
skoleni = [saraksts[i] for i in range(len(saraksts()))]
obj = [[] for i in range(idk)]
try:
    while len(skoleni) > 0:
        for i in range(len(obj)):
            if len(skoleni) == 0:
                obj[i].append(' ')
            else:
                obj[i].append(skoleni[0])
                skoleni.pop(0)
except IndexError:
    print('Index out of range')
for i in range(len(obj)):
    for j in obj[i]:
        if j == ' ':
            obj[i].remove(' ')
        else:
            ...
print(obj)