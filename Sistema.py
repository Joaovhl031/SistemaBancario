saldo = 0
N_saque: int = 0
deposito: int = 0
limite: int = 3000
extrato = ""
SAQUE_LIMITE = 3

menu = """


    [1] - Saque
    [2] - Extrato
    [3] - Depósito
    [4] - Sair


=> """

while True:
    opcao: int = int(input(menu))

    if opcao == 1:
        valor = float(input("Valor a sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = N_saque > SAQUE_LIMITE

        if excedeu_saldo:
            print("Operação falhou. Voçê não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite.")
        elif excedeu_saque:
            print("Operação falhou. Voçê excedeu o número de saques diarios.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            N_saque += 1
        else:
            print("Operação inválida!")
    elif opcao == 2:
        print("\n================= EXTRATO ==================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")
    elif opcao == 3:
        valor: float = float(input("Valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Voçê depositou: R${valor:.2f}\n"
        else:
            print("Valor inválido.")
    elif opcao == 4:
        break

    else:
        print("Opção invalida.")
