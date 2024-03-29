saldo = 0
depositos = []
saques = []
saques_diarios = 0

# Realizar um depósito
valor_deposito = float(input("Digite o valor do depósito: "))
if valor_deposito > 0:
    saldo += valor_deposito
    depositos.append(valor_deposito)
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
else:
    print("Valor de depósito inválido.")

# Realizar um saque
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

# Exibir o extrato
print("Extrato:")
print("Depósitos:")
for deposito in depositos:
    print(f"  - R$ {deposito:.2f}")
print("Saques:")
for saque in saques:
    print(f"  - R$ {saque:.2f}")
print(f"Saldo atual: R$ {saldo:.2f}")
