def randAngram(s, n):
    l = len(s)
    m = l//n + 1
    k = 0


    arr = []
    new_arr = [[0]*n for i in range(m) ]
    for i in range(0,m):
        arrs = []
        for j in range(0,n):
            # print(str(i) + " " + str(j))
            # arrs.append(s[k])
            new_arr[i][j] = s[k]
            # print(arr)
            # print(s[k])

            k += 1
            if k >= l:
                break
    print(new_arr)
    s1 = ""
    for i in range(0, n):
        for j in range(0, m):
            if new_arr[j][i] != 0:
                s1 += str(new_arr[j][i])

    return s1

s='temirlanone'

print(randAngram(s, 4))

