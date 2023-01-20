a = 7
b = 2
c = 8

def triangle_perimeter():
    a = int(input('Input first side: '))
    b = int(input('Input second side: '))
    c = int(input('Input third side: '))
    if a == 0 or b == 0 or c == 0:
        a = 7
        b = 2
        c = 8
    elif a+b+c >= a or a+b+c >= b or a+b+c >= c:
        return print('Does not exist.')
    per = a+b+c
    print(per)
    return per

def triangle_area():
    a = int(input('Input first side: '))
    b = int(input('Input second side: '))
    c = int(input('Input third side: '))
    if a == 0 or b == 0 or c == 0:
        a = 7
        b = 2
        c = 8
    elif a+b+c >= a or a+b+c >= b or a+b+c >= c:
        return print('Does not exist.')
    p = (a+b+c)/2
    ar = (p*(p-a)*(p-b)*(p-c))**0.5
    print(ar)
    return ar
