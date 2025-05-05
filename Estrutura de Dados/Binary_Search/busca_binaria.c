#include <stdio.h>

// Declaração da função de busca binária
int buscaBinaria(int[], int, int);

int main()
{
    // Lista de números inteiros
    int minhaLista[] = {1, 3, 5, 7, 9};

    // Calcula o tamanho da lista
    int len = sizeof(minhaLista) / sizeof(minhaLista[0]);

    // Executa a busca binária e imprime o resultado
    printf("%d\n", buscaBinaria(minhaLista, 3, len));  // Saída: 1 (posição do elemento)
    printf("%d\n", buscaBinaria(minhaLista, -1, len)); // Saída: -1 (elemento não encontrado)
    return 0;
}

// Implementação da função de busca binária
int buscaBinaria(int lista[], int item, int len)
{
    int baixo = 0;
    int alto = len;
    while (baixo <= alto)
    {
        int meio = (baixo + alto) / 2; 
        int palpite = lista[meio];

        // Verifica se o palpite está correto
        if (palpite == item)
        {
            return meio; // Retorna o índice do elemento encontrado
        }
        // Ajusta o limite superior se o palpite for maior que o item
        else if (palpite > item)
        {
            alto = meio - 1;
        }
        // Ajusta o limite inferior se o palpite for menor que o item
        else
        {
            baixo = meio + 1;
        }
    }
    return -1; // Retorna -1 se o número não for encontrado
}
