'''
2.3 Feladat
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!

    O O O
    O O O
    O O O 
  
Feladat
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0), a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot, hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!

Feladat
Alakítsd át úgy a programot, hogy a koordinátapárok bekérése addig folytatódjon, míg a felhasználó intervallumon kívüli értéket nem ad meg! A program minden bekérés után rajzolja ki a rácsot úgy, hogy megjeleníti a már korábban megadott koordináták esetében is a '+' jelet!
'''


tarolo = []
for i in range(3):
    tarolo.append(['O ' for szam in range(3)])

def listToString(i):
    str1 = " "
    return (str1.join(i))

def ooo():
    for i in tarolo:
        print(listToString(i))

while True:
    fuggoleges = int(input('Szám: (0-2): \t'))
    vizszintes = int(input('Szám: (0-2): \t'))

    if fuggoleges > 2 or vizszintes > 2:
        break
    
    tarolo[fuggoleges][vizszintes] = tarolo[fuggoleges][vizszintes].replace('O ', '+ ')

    ooo()
