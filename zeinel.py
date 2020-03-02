
def sidel(arr):
    x_last=0
    y_last=0
    z_last=0
    counter=0
    eps = 0.001
    if abs(arr[0][2])+abs(arr[0][1])>abs(arr[0][0]):
        return False
    if abs(arr[1][0])+abs(arr[1][2])>abs(arr[1][1]):
        return False
    if abs(arr[2][0])+abs(arr[2][1])>abs(arr[2][2]):
        return False
    times = 0
    first = True
    second = True
    third = True
    while first or second or third:
        times +=1
        x = (arr[0][3] - arr[0][1]*(y_last) - arr[0][2]*z_last) / arr[0][0]
        y = (arr[1][3] - arr[1][0]*x - arr[1][2]*z_last) / arr[1][1]
        z = (arr[2][3] - arr[2][0]*x - arr[2][1]*y) / arr[2][2]

        if abs(x - x_last) <= eps:
            first = False
        else:
            x_last = x

        if abs(y - y_last) <= eps:
            second = False
        else:
            y_last = y

        if abs(y - y_last) <= eps:
            third = False
        else:
            z_last = z

    new_array=[]
    new_array.append(x_last)
    new_array.append(y_last)
    new_array.append(z_last)
    new_array.append(times)


    return new_array

arr=[[10,2,-1,5],
     [-2,-6,-1,24.42],
     [1,-3,12,36]]

print(sidel(arr))


