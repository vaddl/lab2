#5
a=int(input('vvedit chislo'))
if a>=0 :
    print('nylove chislo')
if a<0 and a/2:
    print('videmne parne chislo')
if a>0 and a%2:
     print('dodatne ne parne chislo')

    #11
def check(a, b, c):
    if a > b and b > c:
        a, b, c = a * 2, b * 2, c * 2
    else:
        a, b, c = -a, -b, -c
    return a, b, c

print('vvedit х, у, z:')
x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))
r = check (x, y, z)
print(r)

#13
a = int( input('1=') )
b = int( input('2=') )
c = int( input('3=') )
if a + b <= c:
    print('nemojlivo')
if c*pow(2) == ( a*pow(2) ) + ( b*pow(2) ):
    print('pryamokytny')
if (( a*pow(2) ) + ( b*pow(2) ) - ( c*pow(2)) / ( 2 * a * b )) > 0:
    print('gostry')
else:
    print('typiy')
