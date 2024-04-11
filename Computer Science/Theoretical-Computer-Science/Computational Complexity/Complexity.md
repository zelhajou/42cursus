Complexity in computer science refers to the analysis of the efficiency and resource requirements of algorithms and computational problems. It's a crucial concept for evaluating the performance of algorithms and understanding how they scale with input size. Computer scientists use complexity analysis to make informed decisions about which algorithms to use in various applications and to predict how long an algorithm will take to solve a problem.

**Efficiency of an algorithm depends on two parameters:**

1. **Time Complexity:** Time Complexity is defined as the number of times a particular instruction set is executed rather than the total time is taken. It is because the total time taken also depends on some external factors like the compiler used, processor’s speed, etc.
2. **Space Complexity:** Space Complexity is the total memory space required by the program for its execution

## 1. **Time Complexity:**

- Time complexity measures the amount of time an algorithm takes to run as a function of the input size. It provides an upper bound on the running time.
- Time complexity is typically expressed using [[Big-O notation]] (e.g., O(n), O(n^2), O(log n)), where "n" represents the size of the input.
- Common categories of time complexity include:
    - **Constant Time (O(1)):** The algorithm's runtime is independent of the input size.
   ```c
#include <stdio.h>

void printFirstElement(int arr[], int n) {
    if (n > 0) {
        printf("First element: %d\n", arr[0]);
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    printFirstElement(arr, n);
    return 0;
}

// This code has a time complexity of O(1) because it performs a single operation regardless of the size of the input.
```
    - **Linear Time (O(n)):** The runtime increases linearly with the input size.
      ```c
#include <stdio.h>

void printElements(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    printElements(arr, n);
    return 0;
}
// O(n) - Linear Time Complexity: This code has a time complexity of O(n) because it iterates through the entire array once.

```
    - **Quadratic Time (O(n^2)):** The runtime is proportional to the square of the input size.
    ```c
#include <stdio.h>

void printPairs(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("(%d, %d) ", arr[i], arr[j]);
        }
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    printPairs(arr, n);
    return 0;
}

// This code has a time complexity of O(n^2) because it contains nested loops where the outer loop runs 'n' times, and the inner loop runs 'n' times.

```
    - **Logarithmic Time (O(log n)):** The runtime increases logarithmically with the input size, common in efficient algorithms like binary search.
    ```c
    #include <stdio.h>

int binarySearch(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Element not found
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    int target = 3;
    int index = binarySearch(arr, n, target);
    
    if (index != -1) {
        printf("Element found at index %d\n", index);
    } else {
        printf("Element not found\n");
    }
    
    return 0;
}

// This code has a time complexity of O(log n) because it performs a binary search, dividing the input size in half at each step.

```
    - **Exponential Time (O(2^n)):** The runtime grows exponentially with the input size and is often considered inefficient.
```c
#include <stdio.h>

int recursiveExponential(int n) {
    if (n <= 0) {
        return 1;
    }
    return recursiveExponential(n - 1) + recursiveExponential(n - 1);
}

int main() {
    int n = 5; // Adjust the value of 'n' as needed
    int result = recursiveExponential(n);
    
    printf("Result: %d\n", result);
    
    return 0;
}
```
	
   - **Factorial Time O(n!)**: This is even worse than exponential time and typically only used for theoretical analysis. Algorithms with factorial complexity are extremely slow for moderate input sizes.
   - **Linearithmic Time - O(n log n)** This complexity often appears in efficient sorting algorithms like merge sort and quicksort. It's better than quadratic but worse than linear.
## 2. **Space Complexity:**
    
- Space complexity measures the amount of memory or storage space required by an algorithm as a function of the input size.
- Like time complexity, space complexity is expressed using Big O notation (e.g., O(n), O(1)).
- Algorithms with lower space complexity are generally preferred, especially in resource-constrained environments.

## 3. **Worst-case, Average-case, and Best-case Complexity:**
    
- Algorithms can have different time complexities depending on the nature of the input.
- **Worst-case complexity** considers the maximum time or space required for any input of a given size.
- **Average-case complexity** analyzes the expected time or space usage over all possible inputs.
- **Best-case complexity** represents the minimum time or space required for any input of a given size.
- In practice, worst-case complexity is often the most critical for algorithm selection because it guarantees that the algorithm won't perform worse than a specified limit.

## 4. **Amortized Complexity:**
    
- Some data structures and algorithms exhibit amortized complexity, which considers the average cost of a sequence of operations rather than individual operations. For example, certain dynamic array implementations have amortized constant-time insertion.

## 5. **Complexity Classes:**
    
- Computer scientists classify problems into complexity classes based on their computational difficulty. Two famous classes are P and NP:
	- **P (Polynomial Time):** Problems that can be solved in polynomial time (e.g., O(n), O(n^2)) using a deterministic Turing machine. These problems are considered "easy" to solve.
	- **NP (Nondeterministic Polynomial Time):** Problems for which a proposed solution can be verified in polynomial time but may not be solved quickly. The P vs. NP problem asks whether P = NP, which remains unsolved.
# 6. **Reduction and Completeness:**
    
- Many complexity results involve the reduction of one problem to another. If Problem A can be reduced to Problem B in polynomial time, and Problem B is hard (e.g., NP-hard), then Problem A is also hard.
- Problems that are both in NP and NP-hard are called NP-complete. The Cook-Levin theorem showed that SAT (satisfiability) is NP-complete, and many other problems are proven NP-complete through reductions.

# 7. **Parallel and Distributed Complexity:**
    
- In addition to sequential complexity, computer scientists also study the complexity of parallel and distributed algorithms, where multiple processors or machines work together to solve a problem.

# 8. **Trade-offs and Algorithm Design:**

- Complexity analysis helps in making trade-offs between time and space efficiency, as well as in designing algorithms optimized for specific use cases.

# [[Complexity in other fields]]