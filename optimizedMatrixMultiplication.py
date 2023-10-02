def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Create matrices for storing minimum scalar multiplications and split positions
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    # Initialize the m matrix diagonally with zeros
    for i in range(1, n):
        m[i][i] = 0

    # Dynamic programming to fill the tables
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')  # Initialize to positive infinity
            for k in range(i, j):
                # Calculate the cost of multiplying matrices from i to k and k+1 to j
                cost = m[i][k] + m[k+1][j] + matrices[i-1][0] * matrices[k][1] * matrices[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  # Record the optimal split position

    # Reconstructing the optimal parenthesization
    def parenthesize(i, j):
        if i == j:
            return f'Matrix {i}'
        else:
            k = s[i][j]
            left_chain = parenthesize(i, k)
            right_chain = parenthesize(k + 1, j)
            return f'({left_chain} × {right_chain})'

    optimal_parenthesization = parenthesize(1, n - 1)
    min_scalar_multiplications = m[1][n - 1]

    return optimal_parenthesization, min_scalar_multiplications

# Input: List of matrices represented by their dimensions
matrices = [(2, 3), (3, 4), (4, 2)]

# Apply the algorithm
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)

# Output the results
print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)