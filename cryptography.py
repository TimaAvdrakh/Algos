import random
def ceasar(s,key):
    key = int(key)
    res=''
    for i in range(len(s)):
        num=(ord(s[i])+key-97) %26
        res += chr(num+97)
    return res

s = 'asqdasadzqzqzq'

print(ord('a'))
print(ceasar(s,3))


def makecipher():
    st = set('abcdefghijklmnopqrstuvwxyz')
    s = []
    one=random.sample(st,26)

    return one

def encrupt(s, two):
    l =  len(s)
    new_s = ''
    for i in range(l):
        num = ord(s[i])-97
        new_s += two[num]
    return new_s

two = makecipher()
encrypted = encrupt('absd',two)
print(two)
print(encrypted)