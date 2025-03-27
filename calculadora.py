def main():
    print("Calculadora Simples!")

    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Vamos realizar uma soma simples.")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    multiplicacao = num1 * num2
    subtracao = num1 - num2
    
    print(f"{nome}, o resultado da soma é: {soma}")
    print(f"{nome}, o resultado da multiplicação é: {multiplicacao}")
    print(f"{nome}, o resultado da subtração é: {subtracao}")

if __name__ == "__main__":
    main()
