class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#criando nós
node1 = Node(1)
node2 = Node(1)
node3 = Node(3)

#Ligando nós
node1.next = node2
node2.next = node3
