
def gaus(arr):
    print(arr)
    for i in range(3):
        dev = arr[i][0]
        for j in range(4):
            arr[i][j] = arr[i][j] / dev

    print(arr)

    for i in range(1,3):
        for j in range(4):
            arr[i][j] = arr[i][j] - arr[0][j]

    print(arr)

    for i in range(1,3):
        dev = arr[i][1]
        for j in range(1,4):
            arr[i][j] = arr[i][j] / dev
    print(arr)

    for i in range(2,3):
        for j in range(1,4):
            arr[i][j] = arr[i][j] - arr[1][j]
    print(arr)
    if arr[2][2]==0 and arr[2][3]!=0:
        return False

    x3 = arr[2][3] / arr[2][2]
    x2 = arr[1][3] - arr[1][2]*x3
    x1 = arr[0][3]- arr[0][2]*x3 - arr[0][1]*x2

    ans = []
    ans.append(x1)
    ans.append(x2)
    ans.append(x3)
    return ans

arr = [[10,1,1,12],
       [2,10,1,13],
       [2,2,10,14],
]


print(gaus(arr))