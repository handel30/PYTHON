#Criando a função 
def longplus(algar):
    A = 0 #valor para receber a soma total
    for i in range(1, algar+1, 1): #laço que conta de 1 até algar
        A += (algar - (i - 1))/i #atualizando o valor de A a cada vez q o laço roda
        print('A = ({}-{})/{} = {:.2f}'.format(algar, i-1, i, A))
    
    return A

#Programa princial
val = int(input('Digite um número:\n'))

res = longplus(val) #chamando a função longplus
print('\nO valor de A é {:.2f}'.format(res), end= '\n\n')

#========================================================
print('-'*39, '\nAluno: Händel Mateus Carvalho Sarmento')


