a = 7
b = 2
c = 8

def triangle_perimeter(a, b, c):
    per = a+b+c
    return per

def triangle_area(a, b, c):
    p = (a+b+c)/2
    ar = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return ar
