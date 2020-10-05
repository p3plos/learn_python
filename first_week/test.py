a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('rectangular')
    elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        print('obtuse')
    else:
        print('acute')
else:
    print('impossible')
