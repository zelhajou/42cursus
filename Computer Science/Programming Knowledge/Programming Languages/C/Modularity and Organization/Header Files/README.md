 Header files in C are used to declare and define functions, variables, and macros that can be shared across multiple source code files (.c files). Header files typically have a `.h` extension and contain function prototypes, data type definitions, and macro definitions. They play a crucial role in modularizing C code and facilitating code reuse. 

## 1. Header Files:

- In C, header files are included using the `#include` preprocessor directive.
- Header files contain declarations of functions, variables, and macros that are shared across multiple source files.
- Header files are paired with corresponding source files (implementation files) to provide function prototypes
```c
// MathFunctions.h (Header file)
#ifndef MATH_FUNCTIONS_H
#define MATH_FUNCTIONS_H

// Function prototypes
int add(int a, int b);
int subtract(int a, int b);

#endif
```

```c
// MathFunctions.c (Implementation file)
#include "MathFunctions.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

```

| **Header File** | **Purpose**                                                        |
|-----------------|--------------------------------------------------------------------|
| stdio.h         | Input/output operations, including file operations.                |
| stdlib.h        | General utilities, including memory allocation and random numbers. |
| string.h        | String manipulation functions.                                     |
| math.h          | Mathematical functions and constants.                              |
| time.h          | Date and time functions.                                           |
| ctype.h         | Character classification and conversion functions.                 |
| stdarg.h        | Variable arguments handling.                                       |
| stddef.h        | Common definitions, such as `NULL` and `size_t`.                   |
| stdbool.h       | Boolean type and values.                                           |
| limits.h        | Implementation-specific limits on integer types.                   |
| float.h         | Implementation-specific limits on floating-point types.            |
| errno.h         | Error handling via the global variable `errno`.                    |
| assert.h        | Macros for debugging purposes.                                     |
| signal.h        | Signal handling functions.                                         |
| ctype.h         | Character handling functions.                                      |
| locale.h        | Locale-specific information.                                       |
| setjmp.h        | Non-local jumps for error handling.                                |
