default_radius = 5

def circle_perimeter(r):
    r = input('Input the radius: ')
    if r =='' or int(r) == 0:
        r = 5
    per = 2*3.14*int(r)
    print(per)
    return per

def circle_area():
    r = input('Input the radius: ')
    if r =='' or int(r) == 0:
        r = 5
    ar = 3.14*(int(r)**2)
    print(ar)
    return ar