#include <stdio.h>
#include <math.h>

void pitagoras(double co, double ca) {
    double hipotenusa = sqrt(ca * ca + co * co);
    printf("\nO valor da hipotenusa é: %.2f\n", hipotenusa);
}

int main() {
    double co, ca;
    char continua[2];

    while (1) {
        printf("Calculando o valor da Hipotenusa\n\n");

        printf("Digite o valor do cateto oposto: ");
        if (scanf("%lf", &co) != 1) {
            printf("Entrada inválida para o cateto oposto. Saindo.\n");
            break;
        }

        printf("Digite o valor do cateto adjacente: ");
        if (scanf("%lf", &ca) != 1) {
            printf("Entrada inválida para o cateto adjacente. Saindo.\n");
            break;
        }

        pitagoras(co, ca);

        printf("\nDeseja sair? Digite q ou Q para sair ou pressione Enter para um novo cálculo: ");
        if (fgets(continua, sizeof(continua), stdin) != NULL) {
            if (continua[0] == 'q' || continua[0] == 'Q') {
                break;
            }
            while (getchar() != '\n'); // Limpar o buffer de entrada
        } else {
            printf("Erro na leitura da entrada. Saindo.\n");
            break;
        }
    }

    return 0;
}
