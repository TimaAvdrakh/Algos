import random
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