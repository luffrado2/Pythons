#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângula retângulo, calcule e mostre o comprimento da hipotenusa

import math

print('Vamos calcular a hipotenusa! \n')
cat_oposto = float(input('Digite qual o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.pow(cat_oposto,2) + math.pow(cat_adjacente,2)
print(f'O valor da hipotenusa é: {hipotenusa} \n')

while True:
  opc = input('Deseja calcular SENO, COSSENO E TANGENTE? S/N: ')
  match(opc):
    case opc if opc == 's' or opc == 'S':
      calc = int(input('\n Escolha a opção de calculo: \n 1 - SENO \n 2 - COSSENO \n 3 - TANGENTE \n'))
    case opc if opc == 'n' or opc == 'N':
      break
  match(calc):
    case calc if calc == 1:
      sen = cat_oposto/hipotenusa
      print(f'O seno é {sen}')
      
    case calc if calc == 2:
      cos = cat_adjacente/hipotenusa
      print(f'O cosseno é {cos}')
       
    case calc if calc == 3:
      tang = cat_oposto/cat_adjacente
      print(f'A tangente é {tang}')
      
print('Obrigado por usar!')
