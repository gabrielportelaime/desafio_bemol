# ENTENDER QUAL A RELAÇÃO ENTRE AS COMPRAS DE VALE CRÉDITO PELO TEMPO
import csv
from datetime import datetime
import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
            7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

dicionario_dados = {}
creditos_por_mes_quantidade = {}
creditos_por_mes_valor = {}
debitos_por_mes_quantidade = {}
debitos_por_mes_valor = {}

with open("movimentacoes_vale_credito.csv", "r") as arquivo:
    linhas = csv.reader(arquivo)
    cabecalho = True
    quantidade_movimentacoes_credito = soma_movimentacoes_credito = 0
    quantidade_movimentacoes_debito = soma_movimentacoes_debito = 0
    for linha in linhas:
        if(cabecalho):
            for i in range(len(linha)):
                dicionario_dados[linha[i]] = i
            cabecalho = False
        else:
            debito_credito = linha[dicionario_dados["DEBITO_OU_CREDITO"]].upper()
            valor_movimentado = abs(float(linha[dicionario_dados["VALOR_MOVIMENTADO"]]))
            data_movimentacao = datetime.strptime(linha[dicionario_dados["DATA_DA_MOVIMENTACAO"]], "%Y-%m-%d")
            mes_analisado = data_movimentacao.month
            if(debito_credito == "CREDITO"):                
                quantidade_movimentacoes_credito += 1
                soma_movimentacoes_credito += valor_movimentado
                if(creditos_por_mes_quantidade.get(mes_analisado) is None and creditos_por_mes_valor.get(mes_analisado) is None):
                    creditos_por_mes_quantidade[mes_analisado] = 1
                    creditos_por_mes_valor[mes_analisado] = valor_movimentado
                else:
                    creditos_por_mes_quantidade[mes_analisado] += 1
                    creditos_por_mes_valor[mes_analisado] += valor_movimentado
            elif(debito_credito == "DEBITO"):
                quantidade_movimentacoes_debito += 1
                soma_movimentacoes_debito += valor_movimentado
                if(debitos_por_mes_quantidade.get(mes_analisado) is None and debitos_por_mes_valor.get(mes_analisado) is None):
                    debitos_por_mes_quantidade[mes_analisado] = 1
                    debitos_por_mes_valor[mes_analisado] = valor_movimentado
                else:
                    debitos_por_mes_quantidade[mes_analisado] += 1
                    debitos_por_mes_valor[mes_analisado] += valor_movimentado

# LISTAGEM DOS MESES QUE MAIS VENDERAM (ENTRADAS) EM QUANTIDADE DE VENDAS DE VALE CRÉDITO
print("\n" + "--------------------------------------- MES - QUANTIDADE CREDITADA ---------------------------------------")
for chave in sorted(creditos_por_mes_quantidade, key = creditos_por_mes_quantidade.get, reverse = True):
    valor = creditos_por_mes_quantidade[chave]
    print("Mês: " + str(meses[int(chave)]) + " - " + str(valor) + " vale créditos vendidos")

# LISTAGEM DOS MESES QUE MAIS VENDERAM (ENTRADAS) EM VALORES TOTAIS DE VALE CRÉDITO
print("\n" + "--------------------------------------- MES - VALOR TOTAL CREDITADO ---------------------------------------")
for chave in sorted(creditos_por_mes_valor, key = creditos_por_mes_valor.get, reverse = True):
    valor = creditos_por_mes_valor[chave]
    print("Mês: " + str(meses[int(chave)]) + " - " + locale.currency(valor, grouping=True) + " de vale créditos vendidos")

# LISTAGEM DOS MESES QUE EM QUANTIDADE MAIS HOUVE DÉBITOS DE VALE CRÉDITOS (SAÍDAS)
print("\n" + "--------------------------------------- MES - QUANTIDADE DEBITADO ---------------------------------------")
for chave in sorted(debitos_por_mes_quantidade, key = debitos_por_mes_quantidade.get, reverse = True):
    valor = debitos_por_mes_quantidade[chave]
    print("Mês: " + str(meses[int(chave)]) + " - " + str(valor) + " vale créditos vendidos")

# LISTAGEM DOS MESES QUE EM VALOR MAIS HOUVE DÉBITOS DE VALE CRÉDITOS (SAÍDAS)
print("\n" + "--------------------------------------- MES - VALOR TOTAL DEBITADO ---------------------------------------")
for chave in sorted(debitos_por_mes_valor, key = debitos_por_mes_valor.get, reverse = True):
    valor = debitos_por_mes_valor[chave]
    print("Mês: " + str(meses[int(chave)]) + " - " + locale.currency(valor, grouping=True) + " de vale créditos vendidos")