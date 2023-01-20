asq = 15


def square_perimeter():
    asq = input('Input the side: ')
    if asq =='' or int(asq) == 0:
        asq = 5
    per = int(asq)*4
    print(per)
    return per

def square_area():
    asq = input('Input the side: ')
    if asq =='' or int(asq) == 0:
        asq = 5
    ar = int(asq)**2
    print(ar)
    return ar