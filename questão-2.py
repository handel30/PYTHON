area = float(input("Tamanho da area pintada:\n"))

##numero de litros
vol_tinta = area/6

print('Devem ser comprados {:.2f} litros de tinta'.format(vol_tinta))

##tintas por latas
latas_tintas = vol_tinta//18
if (vol_tinta%18 != 0):
      latas_tintas+=1

custo_lata = latas_tintas * 80
print('Devem ser compradas um total de {:.0f} latas de tinta a um custo de R$ {:.2f}'.format(latas_tintas, custo_lata))  

##tintas por galões
galao_tintas = vol_tinta//3.6
if(vol_tinta%3.6 != 0):
      galao_tintas+=1

custo_galao = galao_tintas * 25
print('Devem ser compradas um total de {:.0f} galoes de tinta a um custo de R$ {:.2f}'.format(galao_tintas, custo_galao))   

#========================================================
print('-'*39, '\nAluno: Händel Mateus Carvalho Sarmento')