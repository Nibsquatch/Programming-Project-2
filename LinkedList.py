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
        self.numelements = 0            # Stores the number of elements in the list

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

        self.numelements += 1
            
    def deleteFront(self):
        
        if self.numelements == 0:       # return None if the list is empty
            return None
        
        front = self.head.data          # Save the data to return
        
        if self.numelements == 1:       # If only one element was in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next   # Move head to next node
            self.head.prev = None        # Remove reference to old head

        self.numelements -= 1
        return front