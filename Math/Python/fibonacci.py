def calcular_fibonacci():
    try:
        numero_str = input("Digite um número inteiro: ")
        numero = int(numero_str)

        if numero < 0:
            print("Entrada inválida. Por favor, digite um número inteiro não negativo.")
            return

        fibonacci = [0, 1]
        for i in range(2, numero + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        print(f"Sequência de Fibonacci até {numero}: {', '.join(map(str, fibonacci[:numero + 1]))}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

calcular_fibonacci()
