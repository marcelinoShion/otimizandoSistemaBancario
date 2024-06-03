def menu(): 
    menu = """
        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [q]  Sair
        [nu] Novo Usuario
        [nc] Nova Conta
    """
    return input(menu)
def depositar (valor , saldo,extrato,/):
    if valor >= 0 :
        saldo += valor 
        extrato += f"Foi depositado : R${valor} \n"
        return saldo, extrato
    else:
        print("Valor de Deposito invalido")
def sacar (*,saldo,valor,extrato,limite,numeroDeSaques,limiteDeSaques):
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
        return saldo ,extrato , numeroDeSaques
    return saldo ,extrato ,numeroDeSaques
def exibirExtrato (saldo,/,*,extrato):
    print(extrato +"\n" + f"O saldo é de : R${'%.2f' %saldo}")
def criarUsuario(usuarios):
    cpf = input("Informe o cpf (somente numero) ")
    usuario = filtrarUsuario(cpf,usuarios)
    if usuario :
        print("Usuario ja existe")
        return
    nome = input("Informe o nome ")
    dataDeNascimento = input ("Informe a data de nascimento ")
    endereco = input("Informe o endereço (logradouro , rua , bairro , cidade/sigla do estado) ")
    usuarios.append({"nome":nome ,"dataDeNascimento":dataDeNascimento ,"endereco":endereco , "cpf":cpf})

def filtrarUsuario(cpf , usuarios):
    for usuario in usuarios:
        print(usuario)
        if(usuario["cpf"] == cpf):
            return usuario
    return None
def criarConta(Agencia,numeroDaConta,usuarios):
    cpf = input("Insira o cpf do usuario")
    usuario = filtrarUsuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia":Agencia ,"numeroDaConta":numeroDaConta ,"usuario":usuario}
    print("Usuario não encontrado")
def main ():
    Agencia = "0001"
    saldo = 0
    limite = 500 
    extrato = ""
    numeroDeSaques = 0
    limiteDeSaques = 3
    usuarios = []
    contas = []
    numeroDaConta = 1
    while True :
        opcao = menu()
        if opcao == "d":
            valor = float(input("Insira o valor que deseja depositar "))
            saldo , extrato = depositar(valor,saldo,extrato)
            
        elif opcao == "s":
            valor = float(input("Insira o valor que deseja sacar "))
            saldo , extrato ,numeroDeSaques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numeroDeSaques=numeroDeSaques,limiteDeSaques=limiteDeSaques)
            
        elif opcao == "e":
            exibirExtrato(saldo,extrato=extrato)
        elif opcao == "nu":
            criarUsuario(usuarios)
        elif opcao == "nc":

            conta = criarConta(Agencia , numeroDaConta ,usuarios)
            if conta :
                contas.append(conta)
                numeroDaConta += 1
        elif opcao == "q":
            break
        else:
            print("Opçao invalida por favor selecione novamente a operacao desejada")
main()           