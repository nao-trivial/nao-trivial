def binomial_coefficient(n, k):
    if k==0 or k ==n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

def print_binomial_coefficients(n):
    for i in range(n+1):
        print(binomial_coefficient(n, i), end=" ")
    print()

def print_binomial_expression(n):
    print("(a + b)^{} = ".format(n), end="")
    for i in range(n+1):
        coef = binomial_coefficient(n, i)
        a_term = "a^{}".format(n-i) if n-i > 1 else "a" if n-i == 1 else ""
        b_term = "b^{}".format(i) if i > 1 else "b" if i == 1 else ""
        print("{}{}{}".format(coef, a_term, b_term), end="")
        if i < n:
            print(" + ", end="")
    print()

# Instruções de uso:
# 1. Substitua o valor de 'n' na última linha do código para o número desejado.
# 2. Execute o código.
# 3. O código imprimirá o n-ésimo binômio de Newton e a expressão algébrica correspondente.

# Exemplo de uso:
n = 8  # Substitua 5 pelo número desejado
print_binomial_coefficients(n)
print_binomial_expression(n)
