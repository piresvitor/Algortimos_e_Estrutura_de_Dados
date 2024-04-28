from collections import deque

#Criando a Fila
queue = deque()

#Adicioanndo elementos 
queue.append(1)
queue.append(2)
queue.append(3)

#Removendo elementos
print(queue.popleft()) #Saida: 

#impirmindo a fila 
print(queue) #Saida 2,3