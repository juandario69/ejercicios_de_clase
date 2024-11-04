def suma(x,y):
    resultado =x+y
    return resultado
print(suma(4,5))

def resta(a,b):
    resultado2=a*b
    return resultado2 
print(resta(10,5))

def multiplicacion(c,d):
    resultado3 =c*d
    return resultado3
print(multiplicacion(2,5))

def siguiente(p):
    resultado4=p+1
    return resultado4   
print(siguiente(1))

def mayor(e,f):
    res = -1
    if(e > f):
        res = e
    else:
        res = f
    return res

def mayordetresnumeros(g,h,i):
   if (g > h) and (g > i):
    return  g
   if (h > g)and (h > i):
    return  h
   if ( i > g )and ( i > h):
     return  i
   print(mayordetresnumeros(7,3,8))

