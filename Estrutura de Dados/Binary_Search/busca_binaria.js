function busca_binaria(lista, item) {
    let baixo = 0;
    let alto = lista.length - 1;
  
    while (baixo <= alto) {
      const meio = Math.floor((baixo + alto) / 2);
      const palpite = lista[meio];
  
      if (palpite === item) {
        return meio;
      } 
      else if (palpite > item) {
        alto = meio - 1;
      } 
      else {
        baixo = meio + 1;
      }
    }
    return null;
  }
  
  const minha_lista = [1, 3, 5, 7, 9];
  
  console.log(busca_binaria(minha_lista, 3)); // 1
  console.log(busca_binaria(minha_lista, -1)); // null
