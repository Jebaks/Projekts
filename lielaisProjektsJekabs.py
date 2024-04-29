class vardi:
    def __init__(self):
        pass
    def vardini(self):
        klase = ['Jānis', 'Pēteris', 'Juris', 'Anna', 'Jēkabs', 'Artūrs', 'Marija']
        return klase
class specifikacija:
    def __init__(self):
        pass
    def grupas(self):
        grupas = int(input('Ievadiet grupu daudzumu: '))
        return grupas
testins = specifikacija()
testins2 = vardi()
idk = int(testins.grupas())
skoleni = [testins2.vardini()[i] for i in range(len(testins2.vardini()))]
obj = [[] for i in range(idk)]
try:
    while len(skoleni) > 0:
        for i in range(len(obj)):
            if len(skoleni) == 0:
                obj[i].append(' ')
            else:
                obj[i].append(skoleni[0])
                skoleni.pop(0)
    print(obj)
except IndexError:
    print('Index out of range')
for i in range(len(obj)):
    for j in obj[i]:
        if j == ' ':
            obj[i].remove(' ')
        else:
            ...
print(obj)