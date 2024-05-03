# CALCULAR PORCENTAGENS POR TIPO DE COMPRA (DÉBITO E CRÉDITO)
import csv
import locale
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

dicionario_dados = {}
porcentagens_debitos_quantidade = {}
porcentagens_creditos_quantidade = {}
porcentagens_debitos_valor = {}
porcentagens_creditos_valor = {}

with open("movimentacoes_vale_credito.csv", "r") as arquivo:
    linhas = csv.reader(arquivo)
    cabecalho = True
    quantidade_movimentacoes_credito = quantidade_movimentacoes_debito = 0
    soma_movimentacoes_credito = soma_movimentacoes_debito = 0
    for linha in linhas:
        if(cabecalho):
            for i in range(len(linha)):
                dicionario_dados[linha[i]] = i
            cabecalho = False
        else:
            tipo_transacao = linha[dicionario_dados["TIPO_TRANSACAO_VC"]].upper()
            valor_movimentado = abs(float(linha[dicionario_dados["VALOR_MOVIMENTADO"]]))
            debito_credito = linha[dicionario_dados["DEBITO_OU_CREDITO"]].upper()
            if(debito_credito == "CREDITO"):
                quantidade_movimentacoes_credito += 1
                soma_movimentacoes_credito += valor_movimentado
                if(porcentagens_creditos_quantidade.get(tipo_transacao) is None and porcentagens_creditos_valor.get(tipo_transacao) is None):
                    porcentagens_creditos_quantidade[tipo_transacao] = 1
                    porcentagens_creditos_valor[tipo_transacao] = valor_movimentado
                else:
                    porcentagens_creditos_quantidade[tipo_transacao] += 1
                    porcentagens_creditos_valor[tipo_transacao] += valor_movimentado
            elif(debito_credito == "DEBITO"):
                quantidade_movimentacoes_debito += 1
                soma_movimentacoes_debito += valor_movimentado
                if(porcentagens_debitos_quantidade.get(tipo_transacao) is None and porcentagens_debitos_valor.get(tipo_transacao) is None):
                    porcentagens_debitos_quantidade[tipo_transacao] = 1
                    porcentagens_debitos_valor[tipo_transacao] = valor_movimentado
                else:
                    porcentagens_debitos_quantidade[tipo_transacao] += 1
                    porcentagens_debitos_valor[tipo_transacao] += valor_movimentado

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO À QUANTIDADE -- CRÉDITO
print("\n" + "--------------------------------------- PORCENTAGENS DE CRÉDITO (QUANTIDADE) ---------------------------------------")
for chave in sorted(porcentagens_creditos_quantidade, key = porcentagens_creditos_quantidade.get, reverse=True):
    valor = porcentagens_creditos_quantidade[chave]
    print("Tipo de compra: " + " -- " + chave + " -- ")
    print("Quantidade de compras desse tipo:", valor)
    print(f"Porcentagem de compras desse tipo: {(100*valor)/quantidade_movimentacoes_credito:.2f} %", end="\n\n")

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO AOS VALORES DE TRANSAÇÕES -- CRÉDITO
print("\n" + "------------------------------------------ PORCENTAGENS DE CRÉDITO (VALOR) ------------------------------------------")
for chave in sorted(porcentagens_creditos_valor, key=porcentagens_creditos_valor.get, reverse=True):
    valor = porcentagens_creditos_valor[chave]
    print("Tipo de compra: " + " -- " + chave + " -- ")
    print("Soma de valores de compras desse tipo: " + locale.currency(valor, grouping=True))
    print(f"Porcentagem em valores de compras desse tipo: {(100*valor)/soma_movimentacoes_credito:.2f} %", end="\n\n")

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO À QUANTIDADE -- DÉBITO
print("\n" + "--------------------------------------- PORCENTAGENS DE DÉBITO (QUANTIDADE) ---------------------------------------")
for chave in sorted(porcentagens_debitos_quantidade, key=porcentagens_debitos_quantidade.get, reverse=True):
    valor = porcentagens_debitos_quantidade[chave]
    print("Tipo de compra: " + " -- " + chave + " -- ")
    print("Quantidade de compras desse tipo:", valor)
    print(f"Porcentagem de compras desse tipo: {(100*valor)/quantidade_movimentacoes_credito:.2f} %", end="\n\n")

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO AOS VALORES DE TRANSAÇÕES -- DÉBITO
print("\n" + "------------------------------------------ PORCENTAGENS DE DÉBITO (VALOR) ------------------------------------------")
for chave in sorted(porcentagens_debitos_valor, key=porcentagens_debitos_valor.get, reverse=True):
    valor = porcentagens_debitos_valor[chave]
    print("Tipo de compra: " + " -- " + chave + " -- ")
    print("Soma de valores de compras desse tipo: " + locale.currency(valor, grouping=True))
    print(f"Porcentagem em valores de compras desse tipo: {(100*valor)/soma_movimentacoes_credito:.2f} %", end="\n\n")