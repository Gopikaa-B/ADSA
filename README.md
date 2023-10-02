Name	:  Gopika B
Register Number 	:  22CS053
Department	:  Computer Science and Engineering

Bubble Sort Implementation:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
•	Time Complexity: The worst-case time complexity of Bubble Sort is O(n2) because it involves nested loops. In the best-case scenario (when the array is already sorted), it can be O(n) if you use a flag to detect that no swaps occurred in a pass.
•	Stability: Bubble Sort is a stable sort because it does not change the relative order of equal elements.
•	Already Sorted: Bubble Sort performs well in this case, with a best-case time complexity of O(n).
•	Reverse Sorted: It performs poorly, with a worst-case time complexity of O(n2).
•	Random Data: It has an average-case time complexity of O(n2).

Comparison with Other Sorting Algorithms:
                        Bubble Sort is generally not preferred for large datasets due to its worst-case time complexity. Instead, Quick Sort and Merge Sort are preferred for larger datasets because they have an average time complexity of O(n log n). Python's built-in sorted function uses a highly optimized sorting algorithm that's typically faster than Bubble Sort and is suitable for most use cases. The choice of sorting algorithm depends on the specific requirements and dataset sizes:
•	For small datasets or nearly sorted data, Bubble Sort may be acceptable.
•	For large datasets, Quick Sort or Merge Sort are more efficient.
•	Python's built-in sorted function should be used for most general-purpose sorting tasks as it's highly optimized and easy to use.


Optimized Matrix Multiplication:
Explanation of the Dynamic Programming Approach:
We create a 2D table dp where dp[i][j] represents the minimum number of scalar multiplications required to multiply matrices from i to j.
We initialize the diagonal elements of the table to 0 because multiplying a matrix by itself doesn't require any additional multiplications.
We then fill in the table using a bottom-up approach. We iterate over the chain length and for each chain length, we consider all possible splits and compute the cost of multiplication at each split.
The recurrence relation used is dp[i][j] = min(dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]) where k represents the split point.
Finally, we reconstruct the optimal parenthesization by tracing back through the table to find the split points.

Time Complexity Analysis:
The time complexity of this algorithm is O(n^3) where n is the number of matrices, as we fill in a 2D table of size n x n.
Space Complexity Analysis:
The space complexity is O(n^2) for the dp table.
Efficiency for Large Instances:
This dynamic programming approach is efficient for solving large instances of the problem because of its polynomial time complexity. It can handle a significant number of matrices efficiently.

N - Queen problem:
Explanation of the Backtracking Approach:
solve_n_queens function takes an integer n as input and returns a list of all possible solutions to the N-Queens problem for an N×N chessboard.
is_safe function checks if it's safe to place a queen at a given row and column by verifying that no other queens threaten it.
backtrack function recursively explores the possibilities of placing queens on each row while maintaining the safety conditions. When it reaches the last row (i.e., a valid solution is found), it adds the solution to the solutions list.
The main function initializes an empty chessboard, starts the backtracking process from the first row, and collects all solutions.
print_solutions function prints the solutions in a human-readable format.

Time Complexity Analysis:
The time complexity of this backtracking algorithm is exponential, specifically O(N!). In the worst case, it explores all possible permutations of queen placements, which is factorial in nature. This complexity grows rapidly with larger values of N, making it inefficient for very large boards. However, for moderately sized boards (e.g., N ≤ 12), the algorithm performs reasonably well.
Efficiency for Larger N Values:
As mentioned, the algorithm's efficiency decreases significantly as N grows due to the exponential time complexity. For N values larger than 12, the computation time becomes impractical, and alternative methods, such as heuristic or optimization algorithms, are usually employed to find solutions efficiently.
