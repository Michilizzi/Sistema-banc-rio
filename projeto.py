menu = """
======== Conta Bancária ========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""
saldo = 0
limite = 1000
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido")
        
    elif opcao == 2:
        valor = float(input("Qual valor deseja sacar: "))
        acima_saldo = valor > saldo
        acima_limite = valor > limite
        acima_saque = numero_saque >= limite_saque
        
        if acima_saldo:
            print("Saldo insuficiente")
        
        elif acima_limite:
            print("Limite de saque excedido")
        
        elif acima_saque:
            print("Limite de saque diário excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saque += 1
            print("Saque realizado com sucesso!")
        
        else:
            print("O valor é inválido")
    
    elif opcao == 3:
        print("----- Extrato -----")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("=============================")

    elif opcao == 4:
            print("Obrigado por utilizar um dos nossos terminais!")
            break
    
    else:
        print("Opção inválida, digite uma das opções do menu")