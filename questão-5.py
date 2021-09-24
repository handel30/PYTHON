# Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string no formato DD de mesPorExtenso de AAAA. Valide a data e
# retorne NULL caso a data seja inválida.

#1 - função para receber a data e devolver a string
def calendaranalisys():
    data = str(input('Digite a data no formato DD/MM/AAAA:\n'))
    div = data.split("/")
    dia = int(div[0]) 
    mes = int(div[1])
    ano = int(div[2])

    #==========================================================
    #2 - validação da data
    if (dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1):
        return None 
    
    else:
        #dicionário para relacionar meses(em número) com seus nomes
        nome_mes = {1 : "janeiro", 2 : "fevereiro", 3 : "março", 4 : "abril", 5 : "maio", 6 : "junho", 7 : "julho", 8 : "agosto", 9 : "setembro", 10 : "outubro", 11 : "novembro", 12 : "dezembro" }

        extenso = '{} de {} de {}'.format(dia, nome_mes[mes], ano)
        return extenso
    
    
datanumer = calendaranalisys()
print(datanumer)

#========================================================
print('-'*39, '\nAluno: Händel Mateus Carvalho Sarmento')