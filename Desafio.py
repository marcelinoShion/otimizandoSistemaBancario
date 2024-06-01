menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
 """

saldo = 0
limite = 500 
extrato = ""
numeroDeSaques = 0
limiteDeSaques = 3

while True :
    opcao = input(menu)
    if opcao == "d":
        valor = int(input("Insira o valor que deseja depositar "))
        if valor >= 0 :
            saldo += valor 
            extrato += f"Foi depositado : R${valor} \n"
        else:
            print("Valor de Deposito invalido")
    elif opcao == "s":
        valor = int(input("Insira o valor que deseja sacar "))
        if numeroDeSaques == limiteDeSaques :
            print("Limite de saques alcançado")
        elif valor > limite :
            print("O valor do saque não pode ser superior a R$500")
        elif valor > saldo :
            print("Saldo insuficiente")
        else:
            numeroDeSaques += 1
            saldo -= valor
            extrato += f"Foi sacado : R${valor} \n"
    elif opcao == "e":
        print(extrato +"\n" + f"O saldo é de : R${'%.2f' %saldo}")
    elif opcao == "q":
        break
    else:
        print("Opçao invalida por favor selecione novamente a operacao desejada")