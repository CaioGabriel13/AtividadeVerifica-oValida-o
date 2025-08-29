def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    try:
        numero = int(input("Digite número inteiro para verificar se é primo:"))
        resultado = is_prime(numero)
        
        if resultado:
            print(f"Número {numero} É PRIMO")
        else:
            print(f"Número {numero} NÃO É PRIMO.")
            
    except ValueError:
        print("Por favor, digite apenas números inteiros válidos.")
