import random

def generate_connected_graph(n, extra_edges, max_weight):
    """
    Generate a connected undirected graph with n nodes.

    Parameters:
        n           : number of vertices (int)
        extra_edges : number of additional random edges (int)
        max_weight  : maximum weight for any edge (int)

    Returns:
        List of edges in (weight, u, v) format
    """
    edges = []
    connected = set([0])

    # Ensure connectivity by building a spanning tree
    for i in range(1, n):
        u = i
        v = random.choice(list(connected))
        weight = random.randint(1, max_weight)
        edge = (weight, min(u, v), max(u, v))
        edges.append(edge)
        connected.add(u)

    # Track existing edges for duplicate checking
    existing_edges = set((min(u, v), max(u, v)) for _, u, v in edges)

    # Precompute all possible edges
    all_possible_edges = {(min(u, v), max(u, v)) for u in range(n) for v in range(u + 1, n)}

    # Remove already existing edges
    remaining_edges = list(all_possible_edges - existing_edges)

    # If we request more extra edges than possible limit it
    extra_edges = min(extra_edges, len(remaining_edges))

    # Sample from the remaining edges
    sampled_edges = random.sample(remaining_edges, extra_edges)

    # Add the sampled edges with random weights
    for u, v in sampled_edges:
        weight = random.randint(1, max_weight)
        edges.append((weight, u, v))

    return edges

from Sorting import BucketSort, QuickSort

def KruskalsAlgorithm(edges, n, m,  compress = True, Bucket = True):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree.
    
    Parameters:
        edges: List of edges in {(u, v): weight} format
        n: Number of vertices in the graph
    
    Returns:
        mst_edges: List of edges in the Minimum Spanning Tree
    """
    parent = list(range(n))
    rank = [0] * n
    
    # Find set of vertex with compression if specified
    def find(x):
        if compress:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        else:
            if parent[x] != x:
                return find(parent[x])
            return x

    
    # Union sets by rank
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
    
    mst_edges = []
    mst_weight = 0

    # Perform either BucketSort or QuickSort as specified
    if Bucket:
        BucketSort(edges, m)
    else:
        QuickSort(edges, 0, n - 1)
    
    for weight, u, v in edges:
        if find(u) != find(v):  # If including this edge doesn't form a cycle
            union(u, v)  # Include it in the MST
            mst_edges.append({(u, v): weight})
            mst_weight += weight
            
            # MST will have n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges, mst_weight


# We will use this block to analyze how the runtime is affected by path compression. Code was ran in a jupyter notebook for speed and results were recorded in excel for varying sizes of n
# Define graph parameters
n = 1000
max_weight = 999

# Generate connected graph
A = generate_connected_graph(n, 1000, max_weight)

import time

# iterables
n_test = 5
runs = []

for _ in range(n_test):

    # Keep track of starting time
    start = time.time()

    # Run Kruskal's Algorithm with optional argument compress set to False
    MST, MST_weight = KruskalsAlgorithm(A, n, max_weight, compress = False)

    # Record the finish time and calculate the total runtime
    runs.append(time.time() - start)

print(f"Kruskal's algorithm without path compression took on average {sum(runs)/n_test} seconds to run.")

runs2 = []

for _ in range(n_test):

    # Keep track of starting time
    start = time.time()

    # Run Kruskal's Algorithm with path compression
    MST, MST_weight = KruskalsAlgorithm(A, n, max_weight)

    # Record the finish time and calculate the total runtime
    runs2.append(time.time() - start)

print(f"Kruskal's algorithm with path compression took on average {sum(runs2)/n_test} seconds to run.")

# We will use this block to analyze how the runtime is affected by sorting method. Code was ran in a jupyter notebook for speed and results were recorded in excel for varying sizes of n
# Define graph parameters
n = 1000
max_weight = 999

# Generate connected graph
A = generate_connected_graph(n, n, max_weight)

# iterables
n_test = 5
runs = []

for _ in range(n_test):

    # Keep track of starting time
    start = time.time()

    # Run Kruskal's Algorithm with optional argument Bucket ss set to False
    MST, MST_weight = KruskalsAlgorithm(A, n, max_weight, Bucket = False)

    # Record the finish time and calculate the total runtime
    runs.append(time.time() - start)

print(f"Kruskal's algorithm with QuickSort took on average {sum(runs)/n_test} seconds to run.")

runs2 = []

for _ in range(n_test):

    # Keep track of starting time
    start = time.time()

    # Run Kruskal's Algorithm with BucketSort
    MST, MST_weight = KruskalsAlgorithm(A, n, max_weight)

    # Record the finish time and calculate the total runtime
    runs.append(time.time() - start)

print(f"Kruskal's algorithm with BucketSort took on average {sum(runs2)/n_test} seconds to run.")

# We will use this block to analyze how the runtime is affected by graph density. Code was ran in a jupyter notebook for speed and results were recorded in excel for varying sizes of n
# Define graph parameters
n = 100
max_weight = 999

# Generate connected graph
A = generate_connected_graph(n, n*n, max_weight)

# iterables
n_test = 5
runs = []

for _ in range(n_test):

    # Keep track of starting time
    start = time.time()

    # Run Kruskal's Algorithm with path compression
    MST, MST_weight = KruskalsAlgorithm(A, n, max_weight)

    # Record the finish time and calculate the total runtime
    runs.append(time.time() - start)

print(f"Kruskal's algorithm on a dense graph took on average {sum(runs)/n_test} seconds to run.")