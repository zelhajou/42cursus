
# preprocessor directives

the preprocessor is a phase that occurs before the compilation of the code. The preprocessor directives are special commands that are processed by the preprocessor. They begin with a # symbol and are used to provide instructions to the preprocessor, which then performs certain actions before the actual compilation takes place. Here are some common preprocessor directives in C:


## #include:


Purpose: Used to include the contents of a file in the source code.
Example:

```c
#include <stdio.h>
```

## #define:

Purpose: Defines a macro or a symbolic constant.
Example:

```c
#define PI 3.14159
```

## #undef:

Purpose: Undefines a previously defined macro.
Example:
```c
#undef PI
```

## #ifdef / #ifndef / #else / #endif:

Purpose: Conditional compilation based on whether a macro is defined or not.
Example:

```c
#ifdef DEBUG
// Code included if DEBUG is defined
#else
// Code included if DEBUG is not defined
#endif
```


#if / #elif / #else / #endif:

Purpose: Conditional compilation based on expressions.
Example:

```c
#if DEBUG_LEVEL == 1
// Code included if DEBUG_LEVEL is 1
#elif DEBUG_LEVEL == 2
// Code included if DEBUG_LEVEL is 2
#else
// Code included otherwise
#endif
```

## #line:

Purpose: Changes the line number and file name of the source code.
Example:

```c
#line 50 "my_file.c"
```

## #error:

Purpose: Generates a compiler error message.
Example:

```c
#ifdef OLD_COMPILER
#error This code requires a modern compiler.
#endif
```

## #pragma:

Purpose: Provides compiler-specific directives.
Example:

```c
#pragma warning(disable: 4018)
```