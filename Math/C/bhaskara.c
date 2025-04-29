#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void bhaskara(double a, double b, double c) {
    double delta = (b * b) - (4 * a * c);
    double x1, x2;

    printf("\nO valor de delta: %.2f\n", delta);

    if (delta >= 0) {
        x1 = (-b + sqrt(delta)) / (2 * a);
        x2 = (-b - sqrt(delta)) / (2 * a);
        printf("Valor de x1: %.2f\n", x1);
        printf("Valor de x2: %.2f\n", x2);
    } else {
        printf("A equação não possui raízes reais (delta negativo).\n");
    }
}

int main() {
    double a, b, c;
    char continua[2];

    while (1) {
        printf("Calculando as raízes de uma equação de 2º grau\n\n");

        printf("Digite um valor para A: ");
        if (scanf("%lf", &a) != 1) {
            printf("Entrada inválida para A. Saindo.\n");
            break;
        }

        printf("Digite um valor para B: ");
        if (scanf("%lf", &b) != 1) {
            printf("Entrada inválida para B. Saindo.\n");
            break;
        }

        printf("Digite um valor para C: ");
        if (scanf("%lf", &c) != 1) {
            printf("Entrada inválida para C. Saindo.\n");
            break;
        }

        bhaskara(a, b, c);

        printf("\nDeseja sair? Digite q ou Q para sair ou pressione Enter para um novo cálculo: ");
        if (fgets(continua, sizeof(continua), stdin) != NULL) {
            // Limpar o buffer de entrada se mais caracteres foram digitados
            if (continua[0] == 'q' || continua[0] == 'Q') {
                break;
            }
            // Consumir a quebra de linha deixada pelo fgets
            while (getchar() != '\n');
        } else {
            printf("Erro na leitura da entrada. Saindo.\n");
            break;
        }
    }

    return 0;
}
