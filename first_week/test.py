A = int(input())
B = int(input())
print('YES'*(1-(A % B))+'NO'*((((A % B)+2)//((A % B)+1)) % 2))
