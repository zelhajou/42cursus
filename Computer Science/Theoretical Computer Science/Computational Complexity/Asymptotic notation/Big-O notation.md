
Big O notation, often denoted as O(f(n)), is a mathematical notation used in computer science and mathematics to describe the upper bound or worst-case time complexity of an algorithm or the rate of growth of a function. It is a way to express how the runtime or resource usage of an algorithm scales with the size of the input (often denoted as "n").

The term "Big O" itself is derived from the use of "order of" to describe the growth rate of a function. In the context of algorithms and complexity analysis:

- O(f(n)) represents an upper bound on the runtime, where f(n) is a function of the input size "n."
- The Big O notation is used to describe the upper limit of an algorithm's performance, providing an asymptotic (large input size) analysis.

Here are some common Big O notations and their meanings:

1. **O(1) - Constant Time:** This represents an algorithm whose runtime does not depend on the input size. It's considered highly efficient and ideal.
    
2. **O(log n) - Logarithmic Time:** Algorithms with this complexity become more efficient as the input size increases. They often occur in divide-and-conquer or binary search algorithms.
    
3. **O(n) - Linear Time:** In this case, the runtime grows linearly with the input size. Each additional element in the input contributes to an equal increase in runtime.
    
4. **O(n log n) - Linearithmic Time:** This complexity often appears in efficient sorting algorithms like merge sort and quicksort. It's better than quadratic but worse than linear.
    
5. **O(n^2) - Quadratic Time:** Algorithms with quadratic complexity have runtimes proportional to the square of the input size. They can be inefficient for large inputs.
    
6. **O(2^n) - Exponential Time:** This complexity class represents algorithms that become dramatically slower as the input size increases. Such algorithms are generally considered impractical for large inputs.
    
7. **O(n!) - Factorial Time:** This is even worse than exponential time and typically only used for theoretical analysis. Algorithms with factorial complexity are extremely slow for moderate input sizes.
    

It's important to note that Big O notation provides an upper bound on the runtime. An algorithm with a time complexity of O(f(n)) may run faster in practice, but it will not run slower as the input size grows. Additionally, Big O notation disregards constant factors and lower-order terms, focusing solely on the dominant factor that determines the algorithm's growth rate.

Big O notation is a crucial tool for algorithm analysis and selection, as it allows developers to make informed choices about which algorithms to use for specific tasks, considering both efficiency and scalability.

![[Pasted image 20231009100750.png]]

[[Big O Cheat Sheet]]