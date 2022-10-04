#crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

'''
num = float(input('Digite um número: '))
print(f'O dobro de {num} é {num*2} \n o triplo é {num*3} \n e a raiz quadrada é %.2f' % (pow(num,0.5)))
'''

#ou

'''
num = float(input('Digite um número: '))
dob = num * 2
trip = num * 3
raiz_qdr = pow(num,0.5)
print(f'O dobro de {num} é {dob}')
print(f'O triplo é {trip}')
print('a raiz quadrada é {:.2f}'.format(raiz_qdr))
'''
