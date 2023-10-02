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
