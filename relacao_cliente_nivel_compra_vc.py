# ENTENDER QUAL A RELAÇÃO ENTRE A COMPRA DE VALE CRÉDITO E O NÍVEL DO CLIENTE
import csv
import locale
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

cliente_nivel = {}
dicionario_dados_clientes = {}

with open("clientes_vale_credito.csv", "r") as arquivo_clientes:
    clientes = csv.reader(arquivo_clientes)
    cabecalho = True
    for cliente in clientes:
        if(cabecalho):
            for i in range(len(cliente)):
                dicionario_dados_clientes[cliente[i]] = i
            cabecalho = False
        else:
            cliente_nivel[cliente[dicionario_dados_clientes["ID_PESSOA"]]] = cliente[dicionario_dados_clientes["DESCRICAO_NIVEL"]].upper()

dicionario_dados = {}
nivel_creditos_quantidade = {}
nivel_creditos_valor = {}

with open("movimentacoes_vale_credito.csv", "r") as arquivo:
    linhas = csv.reader(arquivo)
    cabecalho = True
    quantidade_movimentacoes_credito = soma_movimentacoes_credito = 0
    for linha in linhas:
        if(cabecalho):
            for i in range(len(linha)):
                dicionario_dados[linha[i]] = i
            cabecalho = False
        else:
            debito_credito = linha[dicionario_dados["DEBITO_OU_CREDITO"]].upper()
            if(debito_credito == "CREDITO"):
                cliente = linha[dicionario_dados["ID_PESSOA"]]
                # HÁ CLIENTES QUE NÃO ESTÃO RELACIONADOS NO CSV (clientes_vale_credito.csv)
                # A CLASSFICAÇÃO DESSE TIPO DE CLIENTE SERÁ SEM_CLASSIFICAÇÃO
                if(cliente_nivel.get(cliente) is None):
                    nivel_do_cliente = "SEM_CLASSIFICAÇÃO"
                else:
                    nivel_do_cliente = cliente_nivel[cliente]
                valor_movimentado = float(linha[dicionario_dados["VALOR_MOVIMENTADO"]])
                quantidade_movimentacoes_credito += 1
                soma_movimentacoes_credito += valor_movimentado
                if(nivel_creditos_quantidade.get(nivel_do_cliente) is None and nivel_creditos_valor.get(nivel_do_cliente) is None):
                    nivel_creditos_quantidade[nivel_do_cliente] = 1
                    nivel_creditos_valor[nivel_do_cliente] = valor_movimentado
                else:
                    nivel_creditos_quantidade[nivel_do_cliente] += 1
                    nivel_creditos_valor[nivel_do_cliente] += valor_movimentado

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO À QUANTIDADE -- CRÉDITO
print("\n" + "--------------------------------------- PORCENTAGENS PELO NÍVEL DO CLIENTE (QUANTIDADE) ---------------------------------------")
for chave in sorted(nivel_creditos_quantidade, key = nivel_creditos_quantidade.get, reverse = True):
    valor = nivel_creditos_quantidade[chave]
    print("Nível dos clientes: " + " -- " + chave + " -- ")
    print("Quantidade de compras de clientes desse nível:", valor)
    print(f"Porcentagem de quantidade de compras para clientes desse nível: {(100*valor)/quantidade_movimentacoes_credito:.2f} %", end="\n\n")

# PORCENTAGENS POR TIPO DE TRANSAÇÃO EM RELAÇÃO AOS VALORES DE TRANSAÇÕES -- CRÉDITO
print("\n" + "------------------------------------------ PORCENTAGENS PELO NÍVEL DO CLIENTE (VALOR) ------------------------------------------")
for chave in sorted(nivel_creditos_valor, key = nivel_creditos_valor.get, reverse = True):
    valor = nivel_creditos_valor[chave]
    print("Nível dos clientes: " + " -- " + chave + " -- ")
    print("Soma de valores de compras para clientes desse nível: " + locale.currency(valor, grouping=True))
    print(f"Porcentagem em valores de compras para clientes desse nível: {(100*valor)/soma_movimentacoes_credito:.2f} %", end="\n\n")

# OS CLIENTES DIAMANTE SÃO OS QUE MAIS COMPRAM EM QUANTIDADE E EM VALOR (SEM CONTAR OS QUE ESTÃO SEM CLASSIFICAÇÃO)