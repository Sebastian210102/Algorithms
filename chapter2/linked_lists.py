# In this script i will do 

class Node: 
    def __init__(self, data):
        self.data = data #Actual value 
        self.next = None #Is a pointer to the next value


class linkedList:
    def __init__(self):
        self.head  = None #The list beggins empty
        self.tail = None
    def append(self, data): #Add a elemet at the final of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next =  new_node
        self.tail = new_node

        
        
        
        #If there are elements we need to go over all the list
        
        #This is with a O(n) notation
        # current = self.head
        # while current.next is not None: 
        #     current = current.next

        # current.next = new_node


    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end= "->")
            current = current.next
        print("None")


#Example 

linked_list = linkedList()


#Add Values 
linked_list.append(5)
linked_list.print_list()
linked_list.append(6)
linked_list.append(8)
linked_list.append(10)
linked_list.print_list()