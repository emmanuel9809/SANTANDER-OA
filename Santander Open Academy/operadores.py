a=10 #operadores aritmeticos.
b=3

suma= (a+b)
print(suma)

resta=(a-b)
print(resta)

multiplicacion=(a*b)
print(multiplicacion)

div_decimal=(a/b)
print(div_decimal)

div_sin_decimal=(a//b)
print(div_sin_decimal)

exponenciacion=(a**b)
print(exponenciacion)

#operadores de comparacion

igual= (a == b) # False
print(igual)


diferente=( a != b)   # True
print(diferente)

mayor_que= (a > b )  # True
print(mayor_que)


menor_que= (a < b)   # False
print(menor_que)

mayor_igual= ( a >= b)   # True
print(mayor_que)


menor_igual= (a <= b)   # False
print(menor_igual)


#operadores logicos

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False