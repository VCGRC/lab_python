a,b,c = [int(x) for x in input().split()]

d = b**2 - 4*a*c
if d<0:
    print('no roots')
elif d==0:
    print(f'x1=x2={-b/2*a}')
else:
    print(f'x1={(-b-d**0.5)/2*a}  x2={(-b+d**0.5)/2*a}')