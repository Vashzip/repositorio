#Pedir os 3 números ao usuário
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a > b and a > c: #Caso A seja o maior número
    x = a
    if b > c:
        y = c
        z = b
    else:
        y = b
        z = c
elif b > a and b > c: #Caso B seja o maior número
    x = b
    if a > c:
        y = c
        z = a
    else:
        y = a
        z = c
else: #Caso nem A nem B for o maior número
    x = c
    if a > b:
        y = b
        z = a
    else:
        y = a
        z = b


resultado = 3 * x + 4 * y + z

print("\nO resultado da equação 3X + 4Y + Z é:", resultado)
print("O resultado da equação 3X + 4Y + Z é: {}".format(resultado))

#Não é necessário uso de igualdade nos if's, pois, todas as condições já são atingidas