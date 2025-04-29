def pitagoras(co, ca):
    hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
    return print(f'\nO valor da hipotenusa é: {hipotenusa}')


while True:
    print('Calculando o valor da Hipotenusa\n')
        
    co = float(input('Digite o valor do cateto oposto: '))
    ca = float(input('Digite o valor do cateto adjacente: '))
        
    pitagoras(co, ca)

    continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo:  ')
    if continua == 'q' or continua == 'Q':
        break
