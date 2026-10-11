def atualizar_saldo(saldo, valor, operacao):
    operacao = operacao.lower()
    if operacao == "deposito":
        saldo = saldo + valor
    elif operacao == "saque":
        saldo = saldo - valor
    return saldo

saldo = float(input("Digite o saldo atual: "))
valor = float(input("Digite o valor da operação: "))
operacao = input('Digite o tipo da operação ("deposito" ou "saque"): ')

novo_saldo = atualizar_saldo(saldo, valor, operacao)
print("Novo saldo:", novo_saldo)