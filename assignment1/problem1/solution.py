list_1 = input()
list_2 = input()

m = list_1[0]
n = list_2[0]

if m == '0' and n == '0':
    print('0')
elif m == '0':
    print(list_2)
elif n == '0':
    print(list_1)
else:
    a = list_1[2:].split()
    print(a)
    b = list_2[2:].split()
    print(b)
    c = [str(int(m) + int(n))]

    while a or b:
        if not b:
            c.append(a.pop(0))
        elif not a:
            c.append(b.pop(0))
        else:
            if int(a[0]) < int(b[0]):
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))

    print(' '.join(c))
