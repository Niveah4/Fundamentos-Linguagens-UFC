# Simulador de Conta Bancária

``` python
saldo = 1000.0  # Saldo inicial

def menu():
    print("\n=== Menu Bancário ===")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: "))
        if valor <= 0:
            print("Valor inválido. Tente novamente.")
            continue
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        valor = float(input("Digite o valor para saque: "))
        if valor <= 0:
            print("Valor inválido.")
            continue
        if valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "4":
        print("Encerrando o atendimento. Obrigado por usar nosso sistema.")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 4.")
```

---

# Estruturas de Controle Utilizadas

- **if/elif/else:** decisões com base na opção escolhida.
- **while:** mantém o sistema rodando até o usuário escolher sair.
- **continue:** evita executar lógica com dados inválidos.
- **break:** encerra o programa quando o cliente deseja sair.