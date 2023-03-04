class Node:
    def __init__(self,value):
        self.value = value
        self.next=None


class Pila:
    def __init__(self):
        self.height = 0

    def push(self,value):
        new_nodo=Node(value)
        if self.height==0:
            self.top=new_nodo
        else:
            new_nodo.next=self.top
            self.top=new_nodo

        self.height +=1
        return
    def print_stack(self):
        tem=self.top
        while tem is not None:
            print(tem.value)
            tem=tem.next
        return

    def pop(self):
        tem=self.top
        self.top=tem.next
        tem.next=None
        self.height+=1
        return tem.value

my_pila=Pila()
my_pila.push(1)
my_pila.push(2)
my_pila.push(3)
my_pila.print_stack()
print("----------------------------------")
my_pila.pop()
print("----------------------------------")
print(my_pila.top.value)
print("----------------------------------")
my_pila.print_stack()





















