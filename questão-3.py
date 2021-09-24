"""Faça um algoritmo para ler o saldo de 10 (dez) clientes de um banco. Calcular e
imprimir:
• o saldo médio dos clientes
• a porcentagem de clientes com saldo devedor
• o número de clientes com saldo credor"""
#criando variáveis para armazenar os respectivos valores
saldo_total = 0
saldo_medio = 0
num_dev = 0
num_cred =  0 

#pegando o saldo de cada cliente e fazendo as respectivas contagens
for i in range(1, 10+1, 1):
    print('Digite o saldo do cliente {}'.format(i))
    val = int(input())
    saldo_total += val
    if (val < 0):
        num_dev += 1 #contando os devedores
    elif (val > 0):
        num_cred += 1 #contando os credores

saldo_medio = saldo_total/10 #calculando o saldo medio

percent_dev = (num_dev/10)*100

print('='*40,'\nSaldo médio dos clientes: R${:.2f}'.format(saldo_medio))
print('O percentual de devedores eh {:.1f}%'.format(percent_dev))
print('O numero de clientes credores eh: {:.2f}'.format(num_cred))

#========================================================
print('-'*39, '\nAluno: Händel Mateus Carvalho Sarmento')