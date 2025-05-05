class PesquisaBinaria():

  def busca_iterativa(self, lista, item):
    # baixo e alto mantêm o controle de qual parte da lista irá ser pesquisada.
    baixo = 0
    alto = len(lista) - 1

    # Enquanto você não reduziu a busca a um elemento ...
    while baixo <= alto:
      # ... verifique o elemento do meio
      meio = (baixo + alto) // 2
      palpite = lista[meio]
      # Item encontrado.
      if palpite == item:
        return meio
      # O palpite era muito alto.
      if palpite > item:
        alto = meio - 1
      # O palpite era muito baixo.
      else:
        baixo = meio + 1
    # O item não existe
    return None

  def busca_recursiva(self, lista, baixo, alto, item):
    # Verifique o caso base
    if alto >= baixo:

        meio = (alto + baixo) // 2
        palpite = lista[meio]
  
        # Se o elemento está presente no meio
        if palpite == item:
            return meio
        # Se o elemento é menor que o meio, então ele só pode estar presente no subarray da esquerda
        elif palpite > item:
            return self.busca_recursiva(lista, baixo, meio - 1, item)
        # Caso contrário, o elemento só pode estar presente no subarray da direita
        else:
            return self.busca_recursiva(lista, meio + 1, alto, item)
  
    else:
        # Elemento não está presente no array
        return None

if __name__ == "__main__":
  pb = PesquisaBinaria()
  minha_lista = [1, 3, 5, 7, 9]

  print(pb.busca_iterativa(minha_lista, 3)) # => 1

  print(pb.busca_iterativa(minha_lista, -1)) # => None

  print(pb.busca_recursiva(minha_lista, 0, len(minha_lista)-1,5)) # =>1