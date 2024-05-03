# CALCULAR TICKET MÉDIO
import csv
import locale
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
dicionario_dados = {}
with open("movimentacoes_vale_credito.csv", "r") as arquivo:
    linhas = csv.reader(arquivo)
    cabecalho = True
    quantidade_movimentacoes = soma_movimentacoes = soma_absoluta_movimentacoes = 0
    for linha in linhas:
        if(cabecalho):
            for i in range(len(linha)):
                dicionario_dados[linha[i]] = i
            cabecalho = False
        else:
            quantidade_movimentacoes += 1
            soma_movimentacoes += float(linha[dicionario_dados["VALOR_MOVIMENTADO"]])
            soma_absoluta_movimentacoes += abs(float(linha[dicionario_dados["VALOR_MOVIMENTADO"]]))

valor_total_transacionado = locale.currency(soma_absoluta_movimentacoes/quantidade_movimentacoes, grouping=True)
ticket_medio = locale.currency(soma_movimentacoes/quantidade_movimentacoes, grouping=True)
soma_movimentacoes = locale.currency(soma_movimentacoes, grouping=True)
soma_absoluta_movimentacoes = locale.currency(soma_absoluta_movimentacoes, grouping=True)

# QUANTIDADE TOTAL DE TRANSAÇÕES FEITAS
print("\n" + "Quantidade total de movimentações:", quantidade_movimentacoes)
# SOMA DE TODAS AS TRANSAÇÕES, CONSIDERANDO SEUS VALORES (ENTRADAS/CRÉDITOS - POSITIVO) (SAÍDAS/DÉBITOS - NEGATIVO)
print("Soma total dos valores das movimentações: " + soma_movimentacoes)
# SOMA DE TODAS AS TRANSAÇÕES, CONSIDERANDO SEUS VALORES ABSOLUTOS
print("Soma de valores absolutos de todas as movimentações: " + soma_absoluta_movimentacoes)
# TICKET MÉDIO CONSIDERANDO OS VALORES (ENTRADAS/CRÉDITOS - POSITIVO) (SAÍDAS/DÉBITOS - NEGATIVO)
print("Ticket médio: " + ticket_medio)
# VALOR MÉDIO TOTAL POR TRANSAÇÃO
print("Valor médio transacionado: " + valor_total_transacionado + "\n")