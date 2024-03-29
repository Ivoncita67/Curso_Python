saldo = 0
depositos = []
saques = []
saques_diarios = 0

def realizar_deposito():
    global saldo, depositos
    valor_deposito = float(input("Digite o valor do depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        depositos.append(valor_deposito)
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def realizar_saque():
    global saldo, saques, saques_diarios
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= 0:
        print("Valor de saque inválido.")
    elif saques_diarios >= 3:
        print("Limite diário de saques alcançado.")
    elif valor_saque > 500:
        print("Limite de saque por operação é de R$ 500.00")
    elif valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor_saque
        saques.append(valor_saque)
        saques_diarios += 1
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")

def exibir_extrato():
    global saldo, depositos, saques
    print("Extrato:")
    print("Depósitos:")
    for deposito in depositos:
        print(f"  - R$ {deposito:.2f}")
    print("Saques:")
    for saque in saques:
        print(f"  - R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Loop principal do programa
while True:
    print("\n1. Realizar depósito")
    print("2. Realizar saque")
    print("3. Exibir extrato")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        realizar_deposito()
    elif opcao == 2:
        realizar_saque()
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 4:
        print("Obrigado por utilizar nosso sistema!")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
