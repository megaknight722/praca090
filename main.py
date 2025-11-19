import bryly
import plaskie
import math
print('1 plaskie 2 bryly')
inp = int(input())
if inp == 1:
    print('1 kwadrat 2 prostokat 3 romb 4 trojkata 5 rownolegloboku 5 trapez')
    inp1 = int(input())
    if inp1 == 1:
        print('dgdfdd')
        a:float =float(input('dlugosc boku kwadratu : '))
        b = a
        print(f'pkwadratu = {plaskie.kwipro(a,b)}')
    elif inp1 == 2:
        print('dgddrdthdf')
        a:float = float(input('dlugosc podstawy prostokatu: '))
        b:float = float(input('drugi bok prostokatu: '))
        print(f'pprostokata = {plaskie.kwipro(a,b)}')
    elif inp1 == 3:
        print('grgrghtrgfh')
        a:float = float(input('dlugosc podstawy rombu'))
        b:float = float(input('wysokosc rombu'))
        print(f'prombu = {plaskie.kwipro(a,b)}')
    elif inp1 == 4:
        print('234234234')
        a:float = float(input('podstawa trojkata'))
        b:float = float(input('wysokosc trojkata'))
        print(f'ptrojkata = {plaskie.troj(a,b)} ')
    elif inp1 == 5:
        print('gfsdfgsrdgbrs')
        a:float = float(input('podstawa rownolegboloku'))
        b:float = float(input('wysokosc rownolegloboku'))
        print(f'prownolegloboku: {plaskie.kwipro(a,b)}')
    elif inp1 == 6:
        print('gfdfgdg')
        a:float = float(input('podstawa'))
        b:float = float(input('druga podstawa'))
        h:float = float(input('wysokosc'))
        print(f'pole trapezu {plaskie.trap(a,b,h)}')
elif inp == 2:
    print('1 szescian 2 prostopadloscian 3 graniastoslup 4 ostroslup')
    inp2 = int(input())
    if inp2 == 1:
        a:float = float(input('dlugosc krawedzi szescianu'))
        print(f'pszescian {bryly.cude(a)}')
    elif inp2 == 2:
        a:float = float(input('1'))
        b:float = float(input('2'))
        c:float = float(input('3'))
        print(f'pprostopadloscianu lub graniastoslupa prawidlowego {bryly.pros(a,b,c)}')
    elif inp2 == 3:
        a:float = float(input('1'))
        b:float = float(input('2'))
        print(f'p graniastoslupa {bryly.granbokrownpodkw(a,b)}')
