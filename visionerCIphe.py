
def vishiner(st, key):
    l = len(st)
    result = ''
    new_key = lengthKey(l, key)
    # print(new_key)
    new_st = ''
    for i in range(l):
        n = (ord(st[i])-97+ord(new_key[i])-97) % 26

        n = n + 97
        new_st += chr(n)
        # print(new_st)
    return new_st

def lengthKey(num, key):
    l = len(key)
    times = num//l
    left = num % l
    new_s = ''
    # print(times)
    # print(left)
    for i in range(times):
        new_s += key

    for i in range(left):
        new_s += key[i]
    return new_s

print(vishiner('temirlan','oneol'))


