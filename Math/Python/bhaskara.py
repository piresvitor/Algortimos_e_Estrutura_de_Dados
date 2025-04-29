def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    
    print('\nO valor de delta: {0}'.format(delta))
    print('\nValor de x1: {0}\n'.format(x1))
    print('Valor de x2: {0}'.format(x2))


while True:
    print('Calculando as raízes de uma equação de 2º grau\n')
        
    a = float(input('Digite um valor para A: '))
    b = float(input('Digite um valor para B: '))
    c = float(input('Digite um valor para C: '))
        
    bhaskara(a, b, c)

    continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo:  ')
    if continua == 'q' or continua == 'Q':
        break
