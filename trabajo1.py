# Verificar que digito es el mayor de los tres ingresados.


print("------------------------------------------")
print("-----------CUAL ES EL VALOR MAYOR---------")
print("------------------------------------------")

#input
A = int(input("DIGITE EL VALOR de A: "))
B = int(input("DIGITE EL VALOR de B: "))
C = int(input("DIGITE EL VALOR de C: "))
print("-------------------------------")
print("-------------------------------")

#condicion o validacion
print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if (A>B):
    r = A
else:
    r = B

if (r>C):
    print("El numero " + str(r) + " es el numero mayor de todos")
else:
    print("El numero " + str(C) + " es el numero mayor de todos")