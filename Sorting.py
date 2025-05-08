from LinkedList import Node, LinkedList

# Define a Function to Implement BucketSort
def BucketSort(A, m):
    
    # create an empty array with m empty LinkedLists
    B = [LinkedList() for _ in range(m + 1)]

    n = len(A)

    for i in range(n):
        
        # pull the key (weight) for element i in A
        weight = A[i][0]
                   
        # add A[i] to the end the list B[A[i].key]
        B[weight].addtoEnd(A[i])

    # concatenate the LinkedLists to return the array in sorted order
    i = 0

    # for each LinkedList in B
    for j in range(m):
        # for each elelement in LinkedList j
        for k in range(B[j].numelements):
            A[i] = B[j].removeFront()
            i += 1

    return A

# Define a Function to Implement QuickSort
def QuickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # Recursion calls for smaller elements
        # and greater or equals elements
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pv = arr[high]  # Pivot element
    i = low - 1     # Initialize the index of smaller element

    # Traverse through the array segment
    for j in range(low, high):
        if arr[j][0] < pv[0]:  # Assuming tuples or lists in arr
            i += 1
            swap(arr, i, j)
    
    # Place the pivot element in its correct sorted position
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

