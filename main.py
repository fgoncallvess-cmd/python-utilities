while True:
    print("\n=============== Python Utilidades ============")
    print("\n1. Tabuada")
    print("2. Conversor")
    print("3. Temperatura")
    print("4. Média de notas")
    print("5. Calculadora")
    print("6. Sair")


    escolha = int(input("\nDigite sua opção: "))

    if escolha == 6:
        print("Saindo...")
        break


    elif escolha == 1:
        x = int(input("Digite: "))
        for i in range(1, 11):
            m = (x * i)
            print(f'\n{x} * {i} = {m}')
     
     
    elif escolha == 2:
        print("\n CONVERSOR")
        km = float(input("Digite KM: "))
        metros = km * 1000

        print(f"{km} km = {metros} metros")

    elif escolha == 3:
        print("\n TEMPERATURA")
        c = float(input("Digite temperatura em Celsius: "))

        f = (c * 9/5) + 32

        print(f"{c}°C = {f:.1f}°F")


    elif escolha == 4:
        print("\nMÉDIA DE NOTAS")

        qtd = int(input("Quantas notas você quer adicionar? "))

        if qtd <= 0:
            print("Quantidade inválida.")
        else:
            soma = 0

            for i in range(1, qtd + 1):
                nota = float(input(f"Digite a nota {i}: "))
                soma += nota

            media = soma / qtd

            print(f"\nMédia final = {media:.2f}")

            if media >= 7:
                print("Status: Aprovado ")
            elif media >= 5:
                print("Status: Recuperação ")
            else:
                print("Status: Reprovado ")

    elif escolha == 5:
        print("\nCALCULADORA")
        a = float(input("Digite o primeiro número: "))
        op = input("Digite a operação (+, -, *, /): ")
        b = float(input("Digite o segundo número: "))

        if op == "+":
            print(f"Resultado: {a + b}")
        elif op == "-":
            print(f"Resultado: {a - b}")
        elif op == "*":
            print(f"Resultado: {a * b}")
        elif op == "/":
            if b == 0:
                print("Erro: divisão por zero.")
            else:
                print(f"Resultado: {a / b}")
        else:
            print("Operação inválida.")

    else:
        print("\nOpção inválida.")     

        