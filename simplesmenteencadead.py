class SimplesmenteEncadeada:
    def_init_(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
    else:
        current = self.head
    while current.next:
        current = current.next
    current.next = new_node
    
    def display(self):
        current = self.head
    while current:
        print(current.data, end= " -> ")
        current = current.next
    print("None")
    
    linked_list= SimplesmenteEncadeada()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    
    linked_list.display()
    