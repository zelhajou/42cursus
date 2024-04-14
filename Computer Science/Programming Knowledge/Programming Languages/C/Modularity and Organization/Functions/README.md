# Functions:

Function in General Programming:** In a general sense, a function refers to a reusable block of code that performs a specific task. Functions are used to encapsulate a set of instructions into a single unit that can be called and executed multiple times. Functions are a fundamental concept in programming and are used in various programming languages.

- Functions in C are a way to encapsulate a sequence of statements into a reusable block of code.
- They have a return type, a name, and a parameter list.

```c
#include <stdio.h>

// Function declaration
int add(int a, int b);

int main() {
    int result = add(5, 3); // Function call
    printf("C: Result is %d\n", result);
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
```