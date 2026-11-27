class Node:

    def __init__(self, data):
        self.data = data
        self.previous = None


class Stack:
    
    def __init__(self):
        self.top = None

    # Insert into the stack
    def push_stack(self, data):
        new_data = Node(data)
    
        
        new_data.previous = self.top
        self.top = new_data

    def pop_stack(self):
        if self.top is None:
            return "Lista vacia"
        
        value_pop = self.top.data
        self.top = self.top.previous
        return value_pop

         

    
    # Print the stack
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.data, end= '->')
            current = current.previous
        print("None")




nuevo_stack = Stack()

print(nuevo_stack.pop_stack())
nuevo_stack.print_stack()

nuevo_stack.push_stack(5)
nuevo_stack.print_stack()
nuevo_stack.push_stack(8)
nuevo_stack.print_stack()
nuevo_stack.push_stack(4)
nuevo_stack.print_stack()
nuevo_stack.push_stack(3)
nuevo_stack.print_stack()
print(nuevo_stack.pop_stack())
print(nuevo_stack.pop_stack())
print(nuevo_stack.pop_stack())
print(nuevo_stack.pop_stack())
print(nuevo_stack.pop_stack())
nuevo_stack.push_stack(10)
nuevo_stack.print_stack()