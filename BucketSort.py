from LinkedList import Node, LinkedList

# Define a Function to Implement BucketSort
def BucketSort(A, m):
    
    # create an empty array with m empty LinkedLists
    B = [LinkedList()] * m

    n = len(A)

    for i in range(n):
        
        # pull the key for element i in A
        key = A[i].key

        # add A[i] to the end the list B[A[i].key]
        B[key].addtoEnd(A[i])

    # concatenate the LinkedLists to return the array in sorted order
    i = 0

    # for each LinkedList in B
    for j in range(m):
        # for each elelement in LinkedList j
        for k in range(B[j].numelements):
            A[i] = B[j].removeFront()
            i += 1

    return A
