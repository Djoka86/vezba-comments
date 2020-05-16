'''
user_word = input("unesite rec, da poveriye da li je palindrom:   ")

user_word = str(user_word)

rev_user_word = user_word[::-1]

if user_word == rev_user_word:
    print("jestte palindrom")
else:
    print("nije palindrom:   " + rev_user_word)
'''
'''
a = [1, 2, 4, 5, 6, 10, 8]
b =  []


for a1 in a:
    if a1 % 2 == 0:
      b.append(a1)

print(b)
'''
'''
import math

pi = math.pi

a = input("unesite polu-precnik kruznice::")
rezultat = float(a)**2*pi
print (rezultat)
------------------------------------------------
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + 
       str(r) + " is: " + str(pi * r**2))
'''
'''
a = input("unesite brojev::::")
list = a.split(",")
tuple = tuple(list)
print("Lista:::",list)
print("Tupla:::",tuple)
'''

'''
# %
lista_boja = ["crvena", "zelena", "plava", "crna"]
print("%s %s" % (lista_boja[-1], lista_boja[0]))

import turtle

from datetime import datetime

nxow = datetime.now()
print(nxow)


def count_hi(str):
    conter = 0
    for char in range(len(str)):
        if char == "hi":
            conter += 1
    return conter
  #  print(count_hi("hi fdsfhi nke hieck"))
'''
'''
def count_hi(st):
    count = 0
    for i in range(len(st)-1):
        if  st[i] == 'h' and st[i+1] == 'i':
            count +1
      #  count += st[i] == 'h' and st[i+2] == 'i'

#            brojac += 1
    return count + 1

print(count_hi("heihoihiias"))
'''
'''
def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
        if str[0:3] == "xyz":
            return True
        else:
            return False
print(xyz_there('xyzhhh.xyz'))
#for i in range(len(str)):
 #       if str[i::] =='.xyz':
  #          return False

   #     if str[i] == 'x' and str[i+1]=='y' and str[i+2]=='z':
    #        return True

print(xyz_there('yzzyz.xyz'))
'''

'''

def end_other(a, b):
    b = b.lower()
    a = a.lower()
    return (b.endswith(a) or a.endswith(b))
#zavrsava sa...

print(end_other('sadddsad', 'sad'))
'''
'''
def love6(a, b):
    if a==6 or b==6 or (a + b)==6 or abs(a-b)==(6):
        return True
    else:
        return False
print(love6(1,7))
'''

'''
def sorta_sum(a, b):
    c= a+b
    if  10 <= c <= 19:
        return 20
    else:
        return c
print(sorta_sum(1,9))
'''
'''
def lucky_sum(a, b, c):
        sum = 0
        list = [a,b,c,13]
        for n in list [:list.index(13)]:
            sum += n
        return sum

print(lucky_sum(1,1,1))
'''

'''
def list_ends():
    a = [2, 3, 5, 7, 8, 9, 55, 44]
    b = []
    b += a[0], a[-1]
    return b
print(list_ends())
#ili ovako
def list_ends2(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
print(list_ends2([1,2,3]))
'''

'''
# FIBONACI
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    elif count > 2:
        fib = [1, 1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1])
            i = i + 1
    return fib
print(gen_fib())
'''
'''
osoba = {'ime' : 'dzon', 'god' : '23'}
recenica = 'ja se zovem {} , i imam {}'.format(osoba['ime'], osoba['god'])
print(recenica)
'''
'''
fac = 1
num1 = int(input('unesite broj za faktorijal:  '))
for i in range(1,num1+1):
    fac = fac * i
print('faktorijal je: ' , fac)
'''

'''
#igra pogadjanja

import random
user = 0
brojac = 0
pc = random.randint(0, 100)
while user != pc and user != 'exit':
    user = input('koji je vas broj:  ')
    if user == 'exit':
        break

    user = int(user)
    brojac += 1

    if user > pc:
        print('vas broj je veci')
    if user < pc:
        print('vas broj je manji')
    if user == pc:
        print('pogodili ste iz ' + str(brojac) + ' pokusaja')
        break
'''
'''
# todo return ispod petlje ili ispod metode
def has23(nums):
    for n in nums:
        if n == 2 or n == 3:
            return True
        #return False
    return False
print(has23([4,3]))
'''

'''
def count_code(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            count += 1
    return count
print(count_code('cokefgcjlocolehh'))
'''

'''
def xyz_there(str):
    if str[:3] == "xyz":
        return True

    for i in range(2, len(str) - 2):
        if str[i - 1] != "." and str[i:i + 3] == "xyz":
            return True

    return False

def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
    if str[0:3] == "xyz":
        return True
    return False

print(xyz_there('sdbdbfs.xyznndxyz.'))
'''
'''
def caught_speeding(speed, is_birthday):
    while is_birthday == True:
        speed -=5
        if speed <= 60:
            return 0
        if 61 <= speed <= 80:
            return 1
        if speed >= 80:
            return 2

print(caught_speeding(60,True))
'''

'''

def count_events(nums):
    count = 0
    for i in range(len(nums)):
        if i%2 == 0:
            count +=1
    return count
'''

def tower_builder(n_floor):
    a = '*'
    b = 1
    c= 0
    result = []
    num=range(1, n_floor+1)

    # * to increment by odd number
    for x in num:
        c = a
        result.append(c)
        a += str('**')
    return result

print(tower_builder(1))


def __init__(self):
    pass

#---------------------------------------\
def tower_builder(self, n_floors):
    """
    """
    floors = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

    return floors


if __name__ == '__main__':
    #sol = Solution()

    print(repr(sol.tower_builder(6)))














