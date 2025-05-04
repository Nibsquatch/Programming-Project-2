# Define a node
class Node:
    def __init__(self, data):
        self.data = data                # Store data
        self.next = None                # Pointer to next node
        self.prev = None                # Pointer to the previous node

# Define the linked list
class LinkedList:
    def __init__(self):
        self.head = None                # Pointer to the first node in the LinkedList
        self.tail = None                # Pointer to the last node in the LinkedList

    def addtoEnd(self, data):
        
        # initialize the new node
        newNode = Node(data)

        if self.head == None:           # If the LinkedList is empty update the head
            self.head = newNode
            self.tail = newNode

        else:
            newNode.prev = self.tail    # the newNode's previous element is the old tail
            self.tail.next = newNode    # Link current tail's next to newNode
            self.tail = newNode         # Update the tail to newNode
            


    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return  # Key not found

        prev.next = current.next
        current = None
