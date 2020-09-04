length = int(input())
array = input()

array = array.split()

def merge_sort(arr: list, n: int):
    if n <= 1:
        return arr

    a_length = n // 2
    b_length = n - n //2

    a = merge_sort(arr[:n // 2], a_length)
    b = merge_sort(arr[n // 2:], b_length)
    c = []

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

    return c

print(' '.join(merge_sort(array, length)) + ' ')  # have to add space at end of line
