public class BuscaBinaria {

    private static Integer buscaBinaria(int[] lista, int item) {
        int baixo = 0;
        int alto = lista.length - 1;

        while (baixo <= alto) {
            int meio = (baixo + alto) / 2;
            int palpite = lista[meio];
            if (palpite == item) {
                return meio;
            }
            if (palpite > item) {
                alto = meio - 1;
            } else {
                baixo = meio + 1;
            }
        }
        return null;
    }
    public static void main(String[] args) {
        int[] minhaLista = {1, 3, 5, 7, 9};

        System.out.println(buscaBinaria(minhaLista, 3)); // 1
        System.out.println(buscaBinaria(minhaLista, -1)); // null
    }
}
