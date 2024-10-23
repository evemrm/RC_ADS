
'''
#Exercício 1: Crie um algoritmo que solicita ao usuário que insira seu nome e exibe na tela uma mensagem de saudação

nome_usuario = input("Digite o seu nome: ")
print("Olá, " + nome_usuario + ". Seja bem-vindo(a)!")


#Exercício 2: Crie um algoritmo que solicita ao usuário que insira um número decimal e exibe o dobro desse número na tela.

num1 = float(input("Insira um número decimal e utilize ponto no lugar de vírgula: "))
print("O dobro desse número é: " + str(2*num1))


#Exercício 3: Crie um algoritmo que solicite ao usuário que insira um número inteiro e exibe na tela True se ele for par e False se for ímpar.

num1 = int(input("Insira um número inteiro: "))
if num1%2 == 0:
    print("Este número é par"),
else:
    print("Este número é ímpar")

#Exercício 4: Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela True se ele for igual ou acima de zero ou False se menor do que zero.

num1 = float(input("Insira um número: "))
print(num1 >= 0)


#Exercício 5: Crie um algoritmo que solicite ao usuário que insira a temperatura em graus Celsius e exibe na tela a temperatura em Fahrenheit.

temp_c = float(input("Informe a temperatura atual da sua cidade em graus Celcius (ºC): "))
temp_f = ((temp_c*1.8)+32)
print('A temperatura equivalente em Fahreheit é {:.2f}'.format(temp_f))


#Exercício 6: Crie um algoritmo que solicite ao usuário que insira a sua altura em metros e o seu peso em quilogramas e exibe na tela o seu índice de massa corporal (IMC).

altura = float(input("Informe sua altura (em metros): "))
peso = float(input("Informe seu peso (em quilos): "))
imc = (peso/(altura*altura))
print(f'Seu Índice de Massa Corporal (IMC) é: {imc:.2f}')

#Exercício 7: Crie um algoritmo que solicita ao usuário que insira dois números e exibe na tela o resultado da soma, subtração, multiplicação e divisão desses números.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

soma = num1 + num2
subtracao = num1 - num2
mult = num1 * num2
div = num1 / num2

print('Os números informados são: {0} e {1}'.format(num1, num2))
print('A soma é: ', soma)
print('A subtração é: ', subtracao)
print('O produto entre eles é: ', mult)
print('A divisão do primeiro pelo segundo é:', div)

'''
