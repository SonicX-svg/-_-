m = list(range(1, 1+int(input('введите длину массива '))))
n = int(input('введите шаг массива '))
i, result = 0, []
while True:
    result.append(m[i:i+n][0])
    print(m[i:i+n]+m[:n-len(m[i:i+n])])
    i = (i+n)%len(m)-bool((i+n)%len(m))
    if m[i:i+n][0] == m[0]:
        print('\nresult = ',result)
        if len(m)%2!=0:
            result.append(m[-1])     
        break
