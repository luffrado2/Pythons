import math

print('\nCalculadora')

while True:
  opc= int(input('Digite a opção de cálculo: \n 1 - ADIÇÃO \n 2 - SUBTRAÇÃO \n 3 - MULTIPLICAÇÃO  \n 4 - DIVISÃO  \n 5 - EXPOENTE \n 6 - RAIZ QUADRADA \n'))
  
  match opc:
    case 1:
      n1= float(input('Digite o 1º número= '))
      n2= float(input('Digite o 2º número= '))
      resp = n1+n2
      print(f'A resposta é {resp}')
    case 2:
      n1= float(input('Digite o 1º número= '))
      n2= float(input('Digite o 2º número= '))
      resp = n1-n2
      print(f'A resposta é {resp}')
    case 3:
      n1= float(input('Digite o 1º número= '))
      n2= float(input('Digite o 2º número= '))
      resp = n1*n2
      print(f'A resposta é {resp}')
    case 4:
      n1= float(input('Digite o 1º número= '))
      n2= float(input('Digite o 2º número= '))
      resp = n1/n2
      print(f'A resposta é {resp}')
    case 5:
      n1= float(input('Digite o 1º número= '))
      n2= float(input('Digite o 2º número= '))
      resp = math.pow(n1,n2)
      print(f'A resposta é {resp}')
    case 6:
      n1= float(input('Digite um número= '))
      resp = math.sqrt(n1)
      if resp % 1 == 0:
        print(f'A raiz de {n1} é %.f' % (resp))
      else:
        print(f'A raiz de {n1} é aproximadamente %.2f' % (resp))

  cont = input('Deseja continuar? S/N= \n')
  if cont == 'N' or cont == 'n':
      break
print('Obrigado por usar :)!!!')
