#include <stdio.h>
#include <stdlib.h>

int main() {
    int numero, i;

    printf("Digite um número inteiro: ");
    if (scanf("%d", &numero) != 1 || numero < 0) {
        printf("Entrada inválida. Por favor, digite um número inteiro não negativo.\n");
        return 1; // Indica erro
    }

    if (numero == 0) {
        printf("Sequência de Fibonacci até 0: 0\n");
        return 0;
    }
    if (numero == 1) {
        printf("Sequência de Fibonacci até 1: 0, 1\n");
        return 0;
    }

    int *fibonacci = (int *)malloc((numero + 1) * sizeof(int));
    if (fibonacci == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1; // Indica erro
    }

    fibonacci[0] = 0;
    fibonacci[1] = 1;

    for (i = 2; i <= numero; i++) {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }

    printf("Sequência de Fibonacci até %d: ", numero);
    for (i = 0; i <= numero; i++) {
        printf("%d", fibonacci[i]);
        if (i < numero) {
            printf(", ");
        }
    }
    printf("\n");

    free(fibonacci); // Libera a memória alocada
    return 0; // Indica sucesso
}
