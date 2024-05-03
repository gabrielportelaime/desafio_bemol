# ENTENDER QUAL A RELAÇÃO ENTRE AS COMPRAS DE VALE CRÉDITO E AS LOJAS
import csv
import locale
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

dicionario_dados = {}
creditos_quantidade_por_loja = {}
creditos_valor_por_loja = {}

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
                loja = linha[dicionario_dados["UNIDADE"]]
                valor_movimentado = float(linha[dicionario_dados["VALOR_MOVIMENTADO"]])
                quantidade_movimentacoes_credito += 1
                soma_movimentacoes_credito += valor_movimentado
                if(creditos_quantidade_por_loja.get(loja) is None and creditos_valor_por_loja.get(loja) is None):
                    creditos_quantidade_por_loja[loja] = 1
                    creditos_valor_por_loja[loja] = valor_movimentado
                else:
                    creditos_quantidade_por_loja[loja] += 1
                    creditos_valor_por_loja[loja] += valor_movimentado

# LISTAGEM DE LOJAS E SUAS RESPECTIVAS VENDAS DE VALE CRÉDITO (QUANTIDADE DE VENDAS DE VALE CRÉDITO)
print("\n" + "--------------------------------------- LOJA - QUANTIDADE VENDIDA ---------------------------------------")
for chave in sorted(creditos_quantidade_por_loja, key = creditos_quantidade_por_loja.get, reverse = True):
    valor = creditos_quantidade_por_loja[chave]
    print("Loja: " + str(chave) + " - " + str(valor) + " VC vendidos")

# LISTAGEM DE LOJAS E SUAS RESPECTIVAS VENDAS DE VALE CRÉDITO (VALOR TOTAL DE VENDAS DE VALE CRÉDITO)
print("\n" + "--------------------------------------- LOJA - VALOR TOTAL VENDIDO ---------------------------------------")
for chave in sorted(creditos_valor_por_loja, key = creditos_valor_por_loja.get, reverse = True):
    valor = creditos_valor_por_loja[chave]
    print("Loja: " + str(chave) + " - " + locale.currency(valor, grouping=True) + " de VC vendidos")