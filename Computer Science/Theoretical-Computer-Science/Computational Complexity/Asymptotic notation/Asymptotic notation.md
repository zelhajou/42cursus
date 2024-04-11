Asymptotic notation is a mathematical framework used in computer science and mathematics to describe the behavior of functions as they approach certain limits, typically as their input values become very large or very small. It provides a way to express how the performance or complexity of algorithms scales with input size. The three most common asymptotic notations are Big O notation (O()), Omega notation (Ω()), and Theta notation (Θ()):

1. **Big O Notation (O()):**

- **Definition:** Big O notation represents an upper bound on the growth rate of a function. It describes the worst-case behavior of an algorithm or function.
- **Usage:** O(f(n)) indicates that the function's growth rate is at most proportional to f(n) for large enough input values.
- **Example:** If an algorithm has a time complexity of O(n^2), it means that its runtime grows no faster than n^2 as the input size (n) increases. It is an upper limit on performance.
- **Formally:** O(f(n)) = {g(n) : there exist positive constants C and n₀ such that 0 ≤ g(n) ≤ C * f(n) for all n ≥ n₀}

2. **Omega Notation (Ω()):**
    
    - **Definition:** Omega notation represents a lower bound on the growth rate of a function. It describes the best-case behavior of an algorithm or function.
    - **Usage:** Ω(f(n)) indicates that the function's growth rate is at least proportional to f(n) for large enough input values.
    - **Example:** If an algorithm has a time complexity of Ω(n), it means that its runtime is at least linear, and it cannot perform better than linear time for large inputs.
    - **Formally:** Ω(f(n)) = {g(n) : there exist positive constants C and n₀ such that 0 ≤ C * f(n) ≤ g(n) for all n ≥ n₀}
2. **Theta Notation (Θ()):**
    
    - **Definition:** Theta notation represents a tight bound on the growth rate of a function. It describes both the upper and lower bounds and provides a precise characterization of the function's behavior.
    - **Usage:** Θ(f(n)) indicates that the function's growth rate is exactly proportional to f(n) for large enough input values.
    - **Example:** If an algorithm has a time complexity of Θ(n), it means that its runtime is linear, and it exhibits the best-case and worst-case behavior within a constant factor.
    - **Formally:** Θ(f(n)) = {g(n) : there exist positive constants C₁, C₂, and n₀ such that 0 ≤ C₁ * f(n) ≤ g(n) ≤ C₂ * f(n) for all n ≥ n₀}

In addition to these three main asymptotic notations, there are other notations like Little O notation (o()), which describes an upper bound that is not tight, and Little Omega notation (ω()), which describes a lower bound that is not tight. However, Big O, Omega, and Theta notations are the most commonly used.

> [!SUMMARY] Asymptotic notation 
> Asymptotic notation is a powerful tool for algorithm analysis and complexity theory. It allows computer scientists and mathematicians to focus on the fundamental characteristics of algorithms and functions without getting bogged down in specific constant factors or low-level details. It helps in making informed decisions about algorithm selection and understanding how algorithms will behave as input sizes grow.