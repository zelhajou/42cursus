# C++ Programming Language cheat sheet

<table>
<tr>
<td> <b>Category</b> </td>
<td> <b>Information</b> </td>
</tr>
<tr>
<td>Name</td>
<td>C++ Programming Language</td>
</tr>
<tr>
<td>Paradigm</td>
<td>Multi-paradigm: procedural, functional, object-oriented, generic</td>
</tr>
<tr>
<td>Designed by</td>
<td>Bjarne Stroustrup</td>
</tr>
<tr>
<td>Developer</td>
<td>Bjarne Stroustrup and various contributors</td>
</tr>
<tr>
<td>Standardization</td>
<td>ISO/IEC 14882:1998 (C++98), ISO/IEC 14882:2003 (C++03), ISO/IEC 14882:2011 (C++11), ISO/IEC 14882:2014 (C++14), ISO/IEC 14882:2017 (C++17), ISO/IEC 14882:2020 (C++20)</td>
</tr>
<tr>
<td>First appeared</td>
<td>1985</td>
</tr>
<tr>
<td>Stable release</td>
<td>C++20 / December 2020</td>
</tr>
<tr>
<td>Typing discipline</td>
<td>Static, nominative, partially inferred</td>
</tr>
<tr>
<td>OS</td>
<td>Cross-platform</td>
</tr>
<tr>
<td>Syntax Style</td>
<td>C-like</td>
</tr>
<tr>
<td>File Extension</td>
<td>.C, .cc, .cpp, .cxx, .c++, .h, .hh, .hpp, .hxx, .h++</td>
</tr>
<tr>
<td>Compilation</td>
<td>Compiled language</td>
</tr>
<tr>
<td>Uses</td>
<td>
<ul>
  <li>Application software</li>
  <li>Systems software</li>
  <li>Device drivers</li>
  <li>Client-server applications</li>
  <li>Embedded firmware</li>
</ul>
</td>
</tr>

<tr>
<td>Advantages</td>
<td>
<ul>
  <li>Highly versatile</li>
  <li>Performance efficiency</li>
  <li>Rich standard library</li>
  <li>Strong abstraction capabilities</li>
  <li>Compatibility with C</li>
</ul>
</td>
</tr>

<tr>
<td>Key Features</td>
<td>
Object-oriented, Generic programming, Metaprogramming, Exception handling, Standard Template Library (STL), Standardization, Smart pointers, Multi-threading support, Lambda expressions, Move semantics, Rvalue references, Strong typing
</td>
</tr>
<tr>
<td>Major implementations</td>
<td>GNU Compiler Collection (GCC), Clang, Microsoft Visual C++, Intel C++ Compiler</td>
</tr>
<tr>
<td>Influenced by</td>
<td>C, Simula 67, Algol 68, Ada, ML</td>
</tr>
<tr>
<td>Influenced</td>
<td>
  D, Objective-C++, Java, C#, Swift, Rust, PHP, Perl, Python, JavaScript, Go
</td>
</tr>

</table>

## Table of Contents

- [C++ Programming Language cheat sheet](#c-programming-language-cheat-sheet) 
  - [Table of Contents](#table-of-contents)
  - [Code Example](#code-example)
  - [Installation and Setup](#installation-and-setup)
  - [Process of C++ Program execution](#process-of-c-program-execution)
  - [Hello World Program](#hello-world-program)
    - [Header Files and Preprocessor Directives](#header-files-and-preprocessor-directives)
    - [Comments](#comments)
    - [Main Function](#main-function)
    - [Output Statement](#output-statement)
    - [Return Statement](#return-statement)
  - [keywords](#keywords)
  - [Operators](#operators)
  - [Control Structures](#control-structures)
  - [Functions](#functions)
  - [Data Types](#data-types)
  - [Resources](#resources)


## Code Example

```cpp
#include <iostream>

// A simple function to add two numbers
int add(int a, int b) {
    return a + b;
}

class Calculator {
public:
    // A member function to multiply two numbers
    int multiply(int a, int b) {
        return a * b;
    }
};

int main() {
    int x = 5;
    int y = 3;

    // Using the standalone function 'add'
    int sum = add(x, y);
    std::cout << "Sum: " << sum << std::endl;

    // Using a class and member function
    Calculator calc;
    int product = calc.multiply(x, y);
    std::cout << "Product: " << product << std::endl;

    return 0;
}
```

## Installation and Setup

Before you can start programming in C++, you need to set up your development environment. Here are the basic steps to get started:

1. **Install a C++ compiler**: You need a C++ compiler to compile and run your C++ code. Some popular C++ compilers include:
   - GCC (GNU Compiler Collection): A free and open-source compiler available on Linux, macOS, and Windows.
   - Clang: Another open-source compiler that supports C++ and is known for its fast compilation times.
   - Microsoft Visual C++: A compiler provided by Microsoft for Windows development.

2. **Choose a text editor or IDE**: You can write C++ code in any text editor, but using an Integrated Development Environment (IDE) can make your coding experience more productive. Some popular C++ IDEs include:
   - Visual Studio Code: A lightweight and versatile code editor with C++ support through extensions.
   - Visual Studio: A full-featured IDE from Microsoft that provides comprehensive C++ development tools.
   - CLion: A cross-platform C++ IDE from JetBrains that offers advanced code analysis and refactoring features.
   
   **Online editors**:
   - [cppinsights](https://www.cppinsights.io/)
   - [godbolt](https://www.godbolt.org/)

3. **Set up a build system**: To compile and run your C++ code, you need a build system that automates the compilation process. Common build systems for C++ include:

   - Make: A build automation tool that uses Makefiles to specify build rules.
   - CMake: A cross-platform build system generator that simplifies the process of building C++ projects.
   - Visual Studio Build Tools: A set of tools provided by Microsoft for building C++ projects on Windows.

## Process of C++ Program execution

1. **Preprocessing**: The preprocessor processes the source code before compilation. It handles directives such as `#include`, `#define`, and `#ifdef`.

2. **Compilation**: The compiler translates the preprocessed source code into object code (machine code) for the target platform.

3. **Linking**: The linker combines the object code with any necessary libraries to create an executable file.

4. **Loading**: The operating system loads the executable file into memory and starts executing it.

5. **Execution**: The program runs, and the operating system manages its resources and interactions with the hardware.

## Hello World Program

```cpp
#include <iostream> // Preprocessor directive to include the iostream header file
int main() { // Main function directive
    std::cout << "Hello, World!" << std::endl; // Output statement
    return 0; // Return statement
}
```
Save the above code in a file named `hello.cpp` and compile it using a C++ compiler. For example, if you are using GCC, you can compile the code with the following command:

```bash
g++ hello.cpp -o hello
```

This will generate an executable file named `hello`. Run the executable to see the output:

```bash
./hello
```

You should see the output `Hello, World!` printed to the console.

### Header Files and Preprocessor Directives

- **Header Files**: Header files in C++ contain declarations of functions, classes, and variables that are used in a program. They typically have a `.h` or `.hpp` extension and are included in the source code using the `#include` directive.

- **Preprocessor Directives**: Preprocessor directives in C++ are commands that are processed by the preprocessor before compilation. They start with a `#` symbol and are used to include header files, define macros, and conditionally compile code.

in the `hello world` program, the `#include <iostream>` directive includes the `iostream` header file, which provides input and output functionality in C++. The `std::cout` statement is used to print the output `Hello, World!` to the console.

### Comments

Comments in C++ are used to document code and improve its readability. They are ignored by the compiler and do not affect the program's execution.

- **Single-line comments**: Single-line comments in C++ start with `//` and continue until the end of the line. They are used to add explanatory notes or disable code temporarily.

- **Multi-line comments**: Multi-line comments in C++ start with `/*` and end with `*/`. They can span multiple lines and are used for longer comments or to comment out blocks of code.

### Main Function

- The `main()` function is the entry point of a C++ program. It is called automatically when the program is executed and is responsible for controlling the program's flow.

- The `int` before `main()` indicates that the function returns an integer value. By convention, a return value of `0` indicates successful execution, while a non-zero value indicates an error.

### Output Statement

- The `std::cout` object is used to output data to the console in C++. It is part of the `iostream` standard library and is used with the insertion operator `<<` to display text, variables, and expressions.

- The `std::endl` manipulator is used to insert a newline character and flush the output buffer. It is equivalent to `\n` but ensures that the output is displayed immediately.

### Return Statement

- The `return` statement is used to exit a function and return a value to the caller. In the `main()` function, returning `0` indicates successful program execution, while returning a non-zero value indicates an error.

## keywords

C++ has a set of reserved keywords that have special meanings and cannot be used as identifiers (such as variable names, function names, or class names). These keywords are used to define the syntax and structure of the language and should not be used for other purposes.

[Keywords in C++ | List of all keywords in C++ ( Full Explanation )](https://www.scholarhat.com/tutorial/cpp/keywords-in-cpp)

## Data Types

Data types in C++ specify the type of data that a variable can hold. They define the size, range, and operations that can be performed on the data. C++ provides a variety of built-in data types, including primitive types, derived types, and user-defined types.

- **Primitive Data Types**: Basic data types that are directly supported by the language. They include integers, floating-point numbers, characters, and booleans.

  - **Integer Types**: `int`, `short`, `long`, `long long`, `unsigned int`, `unsigned short`, `unsigned long`, `unsigned long long`, `char`, `bool`
  - **Floating-Point Types**: `float`, `double`, `long double`
  - **Character Types**: `char`, `wchar_t`, `char16_t`, `char32_t`
  - **Boolean Type**: `bool`

- **Derived Data Types**: Data types that are derived from primitive types or other derived types. They include pointers, arrays, references, and functions.

  - **Pointers**: `int*`, `char*`, `double*`, `void*`
  - **Arrays**: `int[]`, `char[]`, `double[]`
  - **References**: `int&`, `char&`, `double&`
  - **Functions**: `int(*)(int, int)`, `void(*)(int)`

- **User-Defined Data Types**: Data types that are defined by the user using classes, structures, and enumerations.

  - **Classes**: User-defined data types that encapsulate data and functions into a single entity.
  - **Structures**: User-defined data types that group related data items together.
  - **Enumerations**: User-defined data types that define a set of named constants.

- **Standard Library Data Types**: Data types provided by the C++ standard library that offer additional functionality and features.

  - **Strings**: `std::string`, `std::wstring`, `std::u16string`, `std::u32string`
  - **Containers**: `std::vector`, `std::list`, `std::map`, `std::set`
  - **Iterators**: `std::iterator`, `std::reverse_iterator`, `std::move_iterator`
  - **Algorithms**: `std::sort`, `std::find`, `std::transform`, `std::accumulate`

- **User-Defined Literals**: Custom data types that can be defined by the user to extend the language's syntax and functionality.

  - **User-Defined Literals**: `42s`, `3.14f`, `100ms`, `2h`

- **Type Modifiers**: Keywords that modify the properties of data types, such as signedness, size, and volatility.

  - **Type Modifiers**: `signed`, `unsigned`, `short`, `long`, `const`, `volatile`

- **Type Aliases**: Custom names given to existing data types to improve code readability and maintainability.

  - **Type Aliases**: `using`, `typedef`, `alias`

- **Type Inference**: Mechanism that allows the compiler to deduce the type of a variable based on its initializer.

  - **Type Inference**: `auto`, `decltype`, `std::decay`, `std::common_type`

- **Type Traits**: Template classes that provide information about the properties of data types at compile time.

  - **Type Traits**: `std::is_integral`, `std::is_floating_point`, `std::is_pointer`, `std::is_array`

### Static and Dynamic Data Types

- **Static Data Types**: Data types that are known at compile time and do not change during program execution. They are determined by the compiler based on the variable declaration.

Example:
```cpp
int x = 42; // Static data type (int)
```

- **Dynamic Data Types**: Data types that are determined at runtime and can change during program execution. They are typically used in dynamically allocated memory and polymorphic programming.

Example:
```cpp
int *ptr = new int; // Dynamic data type (int*)
```



### Type Casting

- **Implicit Type Casting**: Automatic conversion of data types by the compiler when compatible.

```cpp
int x = 5;
double y = x; // Implicit type casting from int to double
```

- **Explicit Type Casting**: Manual conversion of data types using casting operators.

```cpp
double x = 3.14;
int y = static_cast<int>(x); // Explicit type casting from double to int
```

- **C-Style Casting**: Traditional casting method that can be used to convert between data types.

```cpp
double x = 3.14;
int y = (int)x; // C-style casting from double to int
```

- **Type Conversion Functions**: Functions provided by the standard library to convert between data types.

```cpp
std::string str = std::to_string(42); // Convert int to string
int num = std::stoi("42"); // Convert string to int
```

## Operators

Operators in C++ are symbols that perform specific operations on one or more operands. They can be classified into various categories based on their functionality and usage.

- **Arithmetic Operators**: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus)

- **Assignment Operators**: `=` (assignment), `+=` (addition assignment), `-=` (subtraction assignment), `*=` (multiplication assignment), `/=` (division assignment), `%=` (modulus assignment)

- **Comparison Operators**: `==` (equal to), `!=` (not equal to), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to)

- **Logical Operators**: `&&` (logical AND), `||` (logical OR), `!` (logical NOT)

- **Bitwise Operators**: `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), `>>` (right shift)

- **Increment and Decrement Operators**: `++` (increment), `--` (decrement)

- **Conditional Operator**: `? :` (ternary operator)

- **Comma Operator**: `,` (comma operator)

- **Member Access Operators**: `.` (dot operator), `->` (arrow operator)

- **Sizeof Operator**: `sizeof` (size of an object or data type)

- **Pointer Operators**: `*` (dereference operator), `&` (address-of operator)

- **Scope Resolution Operator**: `::` (scope resolution operator)

- **Type Cast Operators**: `static_cast`, `dynamic_cast`, `const_cast`, `reinterpret_cast`

- **New and Delete Operators**: `new` (allocate memory), `delete` (deallocate memory)

- **Function Call Operator**: `()` (function call operator)

- **Array Subscript Operator**: `[]` (array subscript operator)

- **Reference Operator**: `&` (reference operator)

## Control Structures

Control structures in C++ are used to alter the flow of a program based on certain conditions or loops. They include if-else statements, switch statements, loops, and jump statements.

### Conditional Statements

- **if Statement**: `if (condition) { /* code */ }`
- **if-else Statement**: `if (condition) { /* code */ } else { /* code */ }`
- **Nested if Statements**: `if (condition1) { if (condition2) { /* code */ } }`

### Switch Statement

- **Switch Case**: `switch (expression) { case value1: /* code */ break; case value2: /* code */ break; default: /* code */ }`

### Loops

- **for Loop**: `for (initialization; condition; update) { /* code */ }`
- **while Loop**: `while (condition) { /* code */ }`
- **do-while Loop**: `do { /* code */ } while (condition);`

### Jump Statements

- **break Statement**: Exits loop or switch statement.
- **continue Statement**: Skips current iteration of loop.
- **return Statement**: Exits function and optionally returns a value.

### Conditional Operator

- **Ternary Operator**: `condition ? expression1 : expression2`

### Control Flow

- **Goto Statement**: `goto label;` (use sparingly, can lead to spaghetti code)

### Exception Handling

- **try-catch Block**: `try { /* code */ } catch (exceptionType e) { /* handler code */ }`

## Short-circuit Evaluation

- **Short-circuit Evaluation of Logical Operators**: `if (x != nullptr && *x > 0) { /* code */ }`

## Conditional Compilation

- **Conditional Compilation**: `#ifdef`, `#ifndef`, `#endif`, `#if`, `#else`, `#elif`

## Macros

- **Define Macro**: `#define NAME value`
- **Conditional Macro**: `#ifdef`, `#ifndef`, `#endif`

## Range-based for Loop (C++11)

- **Iterating Over Containers**: `for (auto element : container) { /* code */ }`

## Using Statements

- **Using Directives**: `using namespace std;`
- **Using Declarations**: `using std::cout;`

## Basic Input/Output

- **Input**: Reading data from the user or external sources.

```cpp
int x;
std::cin >> x; // Read an integer from the console
```

- **Output**: Displaying data to the user or external destinations.

```cpp

std::cout << "Hello, World!" << std::endl; // Print a message to the console
```

- **Formatted Output**: Specifying the format of output data.

```cpp
int x = 42;
double y = 3.14;
std::cout << "Value of x: " << x << ", Value of y: " << y << std::endl;
```

## Command Line Arguments

Command-line arguments are parameters passed to a program when it is executed from the command line. In C++, the `main()` function can accept command-line arguments as arguments.

```cpp
int main(int argc, char* argv[]) {
    for (int i = 0; i < argc; i++) {
        std::cout << "Argument " << i << ": " << argv[i] << std::endl;
    }
    return 0;
}
```
the `argc` parameter is an integer that represents the number of command-line arguments passed to the program, and `argv` is an array of strings that contains the actual arguments.

## Functions

Functions in C++ are blocks of code that perform a specific task. They are defined using a return type, name, parameters, and a body of code. Functions can be standalone or part of a class (member functions).

### Function Basics

- **Declaration**: `returnType functionName(parameters);`
- **Definition**: `returnType functionName(parameters) { /* body */ }`
- **Invocation**: `functionName(arguments);`

### Function Parameters

- **Pass by Value**: `void foo(int x);`
- **Pass by Reference**: `void foo(int &x);`
- **Pass by Pointer**: `void foo(int *x);`

### Return Types

- **Returning Value**: `return value;`
- **Returning Void**: `return;`

### Return Multiple Values

- **Using References**: `void foo(int &result1, int &result2);`

### Function Overloading

- **Multiple Functions with Same Name**: `void foo(int x);` `void foo(double x);`

### Default Arguments

- **Specifying Default Values**: `void foo(int x, int y = 0);`

### Inline Functions

- **Inlining**: `inline returnType functionName(parameters) { /* body */ }`

### Recursion

- **Function Calling Itself**: `void recursiveFunc(int n) { if (n > 0) recursiveFunc(n-1); }`

### Function Pointers

- **Pointer to Function**: `returnType (*ptrName)(parameters);`

### Lambda Expressions (C++11)

- **Anonymous Functions**: `[capture](parameters) { /* body */ }`

### Function Templates

- **Generic Functions**: `template <typename T> void swap(T &a, T &b) { T temp = a; a = b; b = temp; }`

### Function Objects

A function object is an object that can be called like a function. It is a class that overloads the function call operator `operator()`. Function objects are also known as functors.

```cpp
class Add {
public:
    int operator()(int a, int b) {
        return a + b;
    }
};

int main() {
    Add add;
    int sum = add(5, 3);
    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
```

### Variadic Functions (C++11)

- **Functions with Variable Number of Arguments**: `void variadicFunc(int arg1, ...);`

## Pointers and References

Pointers and references are used in C++ to store memory addresses and access data indirectly. They are essential for dynamic memory allocation, function calls, and efficient data manipulation.

**Pointers**: is a variable that stores the memory address of another variable. It allows direct access to the memory location of a variable.

**References**: is an alias for a variable that provides an alternative name for the same memory location. It allows indirect access to the variable.

### Basics

- **Declaration**: `type *ptr;`
- **Initialization**: `int *ptr = &variable;`
- **Dereferencing**: `*ptr` retrieves the value pointed to by `ptr`.
- **Address-of Operator**: `&variable` gets the memory address of `variable`.

### Pointer Arithmetic

- **Increment/Decrement**: `ptr++`, `ptr--`.
- **Arithmetic Operations**: `ptr + n`, `ptr - n`.

### Dynamic Memory Allocation

- **Allocation**: `type *ptr = new type;`
- **Deallocation**: `delete ptr;`
- **Array Allocation**: `type *arr = new type[size];`
- **Array Deallocation**: `delete[] arr;`

### Pointer and Arrays

- **Array Name as Pointer**: Arrays decay into pointers to their first element.
- **Accessing Array Elements**: `*(arr + i)` or `arr[i]`.

### Pointers and Functions

- **Passing Pointers to Functions**: `void foo(int *ptr)`.
- **Returning Pointers from Functions**: `int* foo()`.
- **Pointer to Functions**: `returnType (*ptrName)(parameters);`.

### Pointer and Classes

- **Pointer to Object**: `ClassName *ptr = new ClassName;`
- **Accessing Members**: `ptr->member` or `(*ptr).member`.

### Pointer to Pointer (Double Pointer)

- **Declaration**: `type **ptr;`
- **Initialization**: `type **ptr = &anotherPtr;`
- **Use**: `**ptr` retrieves the value pointed to by another pointer.

### Null Pointers

- **Null Pointer**: `nullptr`.
- **Checking Null Pointers**: `if (ptr == nullptr)`.

### Pointer Casting

- **Casting Pointers**: `type *ptr = reinterpret_cast<type*>(anotherPtr);`

### Pointer and Const

- **Constant Pointers**: `const type *ptr;` or `type *const ptr;`.
- **Pointer to Constant**: `const int *ptr;` (value is constant, pointer is not) or `int *const ptr;` (pointer is constant, value is not).

### Smart Pointers (C++11)

- **Unique Pointer**: `std::unique_ptr<type> ptr;`.
- **Shared Pointer**: `std::shared_ptr<type> ptr;`.
- **Weak Pointer**: `std::weak_ptr<type> ptr;`.

##

## Resources

- [cppreference](www.cppreference.com)
- [learncpp](https://www.learncpp.com/)
- [cplusplus](http://www.cplusplus.com/)
- [cpp-cheat-sheet](https://github.com/gibsjose/cpp-cheat-sheet)
- [Modern-CPP-Programming](https://github.com/federico-busato/Modern-CPP-Programming)
