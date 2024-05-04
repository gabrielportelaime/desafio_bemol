# ENTENDER QUAL A RELAÇÃO ENTRE A COMPRA DE VALE CRÉDITO E O NÍVEL DO CLIENTE 
# SERÁ USADO OS DADOS DO CSV - CLIENTES_VALE_CRÉDITO, POIS AO ANALISAR O CSV MOVIMENTACOES_VALE_CREDITO 
# NOTA-SE QUE HÁ ALGUNS CLIENTES QUE ESTÃO NO CSV - MOVIMENTACOES_VALE_CREDITO E NÃO CONSTAM NO CSV - CLIENTES_VALE_CRÉDITO
import csv
import locale
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

cliente_nivel_quantidade_de_clientes = {}
cliente_nivel_saldo_dos_clientes = {}
cliente_nivel_saldo_medio = {}
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
            nivel_do_cliente = cliente[dicionario_dados_clientes["DESCRICAO_NIVEL"]]
            # ALGUNS CLIENTES POSSUEM SALDO NEGATIVO NA CONTA VC 
            # SERÁ CONSIDERADO OS VALORES NÃO ABSOLUTOS (NEGATIVO - DEVENDO) (POSITIVO - SALDO)
            saldo_do_cliente = float(cliente[dicionario_dados_clientes["SALDO_VC"]])
            if(cliente_nivel_quantidade_de_clientes.get(nivel_do_cliente) is None and cliente_nivel_saldo_dos_clientes.get(nivel_do_cliente) is None):
                cliente_nivel_quantidade_de_clientes[nivel_do_cliente] = 1
                cliente_nivel_saldo_dos_clientes[nivel_do_cliente] = saldo_do_cliente
            else:
                cliente_nivel_quantidade_de_clientes[nivel_do_cliente] += 1
                cliente_nivel_saldo_dos_clientes[nivel_do_cliente] += saldo_do_cliente

for chave, valor in cliente_nivel_saldo_dos_clientes.items():
    cliente_nivel_saldo_medio[chave] = valor/cliente_nivel_quantidade_de_clientes[chave]

# QUANTIDADE TOTAL DE CLIENTES POR NÍVEL - DE FORMA ORDENADA DO MAIOR PARA O MENOR EM QUANTIDADE
print("\n" + "--------------------------------------- QUANTIDADE DE CLIENTES POR NÍVEL ---------------------------------------")
for chave in sorted(cliente_nivel_quantidade_de_clientes, key = cliente_nivel_quantidade_de_clientes.get, reverse = True):
    valor = cliente_nivel_quantidade_de_clientes[chave]
    print("Nível dos clientes: " + " -- " + chave + " -- ")
    print("Quantidade de clientes nesse nível:", valor, end="\n\n")

# VALORES EM SALDO DOS CLIENTES POR NÍVEL - DE FORMA ORDENADA DO MAIOR PARA O MENOR SALDO POR NÍVEL
print("\n" + "------------------------------------------ SALDO DOS CLIENTES POR NÍVEL DO CLIENTE ------------------------------------------")
for chave in sorted(cliente_nivel_saldo_dos_clientes, key = cliente_nivel_saldo_dos_clientes.get, reverse = True):
    valor = cliente_nivel_saldo_dos_clientes[chave]
    print("Nível dos clientes: " + " -- " + chave + " -- ")
    print("Soma do saldo dos clientes desse nível: " + locale.currency(valor, grouping=True), end="\n\n")

# VALORES MÉDIOS DE SALDO DOS CLIENTES POR NÍVEL - DE FORMA ORDENADA DO MAIOR PARA O MENOR EM MÉDIA DE SALDO
print("\n" + "------------------------------------------ MÉDIA DE SALDO DOS CLIENTES POR NÍVEL DO CLIENTE ------------------------------------------")
for chave in sorted(cliente_nivel_saldo_medio, key = cliente_nivel_saldo_medio.get, reverse = True):
    valor = cliente_nivel_saldo_medio[chave]
    print("Nível dos clientes: " + " -- " + chave + " -- ")
    print("Média de saldo dos clientes desse nível: " + locale.currency(valor, grouping=True), end="\n\n")

