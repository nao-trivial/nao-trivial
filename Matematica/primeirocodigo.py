numero = int(input("forneca um numero inteiro que sera elevado a n-esima potencial: "))
nesima = int(input(f"Forneça o valor de n conforme {numero}^n: "))


for i in range(nesima):
    numero *= numero
    
print(numero)