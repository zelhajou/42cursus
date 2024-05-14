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
  - [Introduction](#introduction)
  - [Why C++?](#why-c)
  - [Code Example](#code-example)
  - [C vs C++](#c-vs-c)
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
  - [Classes and Objects](#classes-and-objects)
  - [Data Types](#data-types)
  - [Resources](#resources)
  - [Online editors](#online-editors)


## Introduction

- C++ is a powerful and versatile programming language that is widely used in the software development industry. Developed by Bjarne Stroustrup in the early 1980s, C++ is an extension of the C programming language with added features such as object-oriented programming (OOP) capabilities, generic programming support, and improved memory management.

- One of the key features of C++ is its efficiency and performance. It allows low-level manipulation of memory through features like pointers, making it suitable for system programming and applications where performance is critical. At the same time, C++ provides high-level abstractions through OOP, enabling developers to organize and structure their code in a more modular and reusable way.

- C++ has a rich standard library that provides a wide range of functions and data structures, allowing developers to accomplish various tasks without having to reinvent the wheel. Additionally, C++ supports multiple programming paradigms including procedural, object-oriented, and generic programming, giving developers the flexibility to choose the most appropriate approach for their projects.

- C++ is used extensively in industries such as game development, system programming, embedded systems, finance, and high-performance computing. Its popularity stems from its combination of power, flexibility, and performance, making it a preferred choice for many developers and organizations worldwide.

## Why C++?

**Advantages**: of C++ C++ is extremely fast and has the power and extensibility to write large-scale programs and runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX. Most famous software has their backbone in C++ and many programming languages depend on C++'s performance and reliability in their implementation [Examples include: JVM, JavaScript interpreters and Web frameworks]. C++ [a superset of C] is said to use static typing when type checking is performed during compile-time as opposed to run-time.

**Limitation**: Some tasks can be implemented in C++, though not very quickly. For example: designing GUI screens for applications. Other programming languages like VB, Python have GUI design elements built into them. Therefore, they are better suited for GUI type of task.

**Uses**: Used in the development of new programming languages [C#, Java, JavaScript, Perl, PHP, Python and Verilog], Apple Macintosh, PC running Windows, operating systems and Adobe Systems (like Photoshop, Acrobat etc), softwares for MRI machines, high-end CAD/CAM systems. C++ fully supports most important features of object-oriented programming including the four pillars of object-oriented development:
- Encapsulation
- Data hiding
- Inheritance
- Polymorphism

<!-- 1. **Performance**: C++ allows for low-level memory manipulation and direct hardware access, making it highly efficient. This performance is crucial for applications where speed is paramount, such as real-time systems, game engines, and operating system.
2. **Versatility**: C++ supports multiple programming paradigms including procedural, object-oriented, and generic programming. This versatility allows developers to choose the most suitable paradigm for their project, making C++ applicable in a wide range of domains.
3. **Portability**: C++ code can be compiled and executed on various platforms, including Windows, macOS, Linux, and embedded systems. This portability makes C++ a practical choice for developing cross-platform applications and system software.
4. **Scalability**: C++ is well-suited for developing large-scale applications due to its support for modular programming and powerful abstractions. With features like classes, templates, and namespaces, developers can organize and manage complex codebases effectively.
6. **Compatibility with C**: C++ is largely compatible with C, allowing developers to leverage existing C libraries and codebases. This compatibility makes it easier to integrate C++ code with legacy systems and libraries.
7. **Object-Oriented Programming**: C++ supports object-oriented programming (OOP) concepts such as classes, inheritance, polymorphism, and encapsulation. These features enable developers to create reusable and maintainable code, leading to improved productivity and code quality.
8. **Support for low-level and high-level programming**: C++ provides low-level features like pointers and memory management, as well as high-level abstractions like classes and templates. This duality allows developers to write code at different levels of abstraction, depending on the requirements of the project.
5. **Standard Library**: C++ comes with a rich standard library that provides a wide range of functions and data structures. This library simplifies common programming tasks and reduces the need for developers to write code from scratch.
6. **Combination with C languages**: C++ can be used in conjunction with C languages, allowing developers to take advantage of the strengths of both languages. This combination is particularly useful for system programming, embedded systems, and performance-critical applications.
7. **Community and Support**: C++ has a large and active community of developers who contribute to libraries, frameworks, and tools. This ecosystem provides abundant resources, documentation, and support for C++ programmers. -->

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

## C vs C++

- **C**:
  - Procedural programming language
  - Simple and minimalistic syntax
  - No built-in support for classes and objects
  - No exception handling
  - No function overloading
  - No operator overloading
  - No templates
  - No namespaces
  - No references
  - No standard template library (STL)

- **C++**:
  - Multi-paradigm programming language (procedural, object-oriented, generic)
  - Complex syntax with additional features
  - Built-in support for classes and objects
  - Exception handling
  - Function overloading
  - Operator overloading
  - Templates
  - Namespaces
  - References
  - Standard template library (STL)

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

| Keyword     | Description |
| ----------- | ----------- |
| `auto`      | Specifies that the type of a variable should be automatically deduced from its initializer. |
| `break`     | Exits a loop or switch statement. |
| `case`      | Defines a case in a switch statement. |
| `char`      | Declares a character type. |
| `class`     | Defines a class. |
| `const`     | Declares an object as constant. |
| `continue`  | Skips the rest of a loop iteration. |
| `default`   | Defines the default case in a switch statement. |
| `delete`    | Deallocates memory allocated by `new`. |
| `do`        | Starts a do-while loop. |
| `double`    | Declares a double-precision floating-point type. |
| `else`      | Specifies an alternative in an if-else statement. |
| `enum`      | Declares an enumeration type. |
| `explicit`  | Specifies that a constructor is explicit. |
| `extern`    | Declares an external variable or function. |
| `float`     | Declares a floating-point type. |
| `for`       | Starts a for loop. |
| `friend`    | Declares a function or class as a friend
| `goto`      | Transfers control to a labeled statement. |
| `if`        | Starts an if statement. |
| `inline`    | Specifies that a function should be inlined. |
| `int`       | Declares an integer type. |
| `long`      | Declares a long integer type. |
| `mutable`   | Specifies that a member of a class can be modified even if the object is const. |
| `namespace` | Defines a namespace. |
| `new`       | Allocates memory for an object. |
| `operator`  | Declares an operator function. |
| `private`   | Specifies that members of a class are private
| `protected` | Specifies that members of a class are protected. |
| `public`    | Specifies that members of a class are public. |
| `register`  | Declares a register variable. |
| `reinterpret_cast` | Converts a pointer to another type. |
| `return`    | Exits a function and returns a value. |
| `short`     | Declares a short integer type. |
| `signed`    | Declares a signed integer type. |
| `sizeof`    | Returns the size of a type or object. |
| `static`    | Specifies that a variable or function is static. |
| `static_cast` | Converts a value from one type to another. |
| `struct`    | Defines a structure. |
| `switch`    | Starts a switch statement. |
| `template`  | Declares a template. |
| `this`      | Pointer to the current object. |
| `throw`     | Throws an exception. |
| `try`       | Starts a block of code that can throw exceptions. |
| `typedef`   | Defines a type alias. |
| `typeid`    | Returns the type of an expression. |
| `typename`  | Specifies that a name is a type. |
| `union`     | Defines a union. |
| `unsigned`  | Declares an unsigned integer type. |
| `using`     | Specifies a namespace or type to be used. |
| `virtual`   | Specifies that a function is virtual. |
| `void`      | Declares a void type. |
| `volatile`  | Specifies that a variable can be modified by external processes. |
| `wchar_t`   | Declares a wide character type. |
| `while`     | Starts a while loop. |

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
  - **Structures**: `struct`, `class`, `union`, `enum`

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

- **Dynamic Data Types**: Data types that are determined at runtime and can change during program execution. They are typically used in dynamically allocated memory and polymorphic programming.

Example of static data type:

```cpp
int x = 5; // Static data type (integer)
```

Example of dynamic data type:

```cpp
int* ptr = new int(5); // Dynamic data type (pointer to integer)
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

- **If-Else Statement**: Executes a block of code based on a condition.

```cpp
if (condition) {
	// Code to execute if the condition is true
} else {
	// Code to execute if the condition is false
}
```

- **Switch Statement**: Executes different blocks of code based on the value of an expression.
```cpp
switch (expression) {
	case value1:
		// Code to execute if expression equals value1
		break;
	case value2:
		// Code to execute if expression equals value2
		break;
	default:
		// Code to execute if expression does not match any case
}
```

- **While Loop**: Executes a block of code as long as a condition is true.
```cpp
while (condition) {
	// Code to execute while the condition is true
}
```

- **Do-While
```cpp
do {
	// Code to execute at least once
} while (condition);
```

- **For Loop**: Executes a block of code a specified number of times.
```cpp
for (initialization; condition; update) {
	// Code to execute in each iteration
}
```

- **Break Statement**: Exits a loop or switch statement.
```cpp
while (true) {
	if (condition) {
		break; // Exit the loop
	}
}
```

- **Continue Statement**: Skips the rest of a loop iteration.
```cpp
for (int i = 0; i < 10; i++) {
	if (i % 2 == 0) {
		continue; // Skip even numbers
	}
}
```

- **Goto Statement**: Transfers control to a labeled statement.
```cpp
goto label;
// Code to skip
label:
// Code to execute
```

- **Return Statement**: Exits a function and returns a value.
```cpp
int add(int a, int b) {
	return a + b;
}
```


## Functions

Functions in C++ are blocks of code that perform a specific task. They are defined using a return type, name, parameters, and a body of code. Functions can be standalone or part of a class (member functions).

- **Function Declaration**: Specifies the name, return type, and parameters of a function.
```cpp
int add(int a, int b);
```

- **Function Definition**: Implements the functionality of a function.
```cpp
int add(int a, int b) {
	return a + b;
}
```

- **Function Call**: Invokes a function with specified arguments.
```cpp
int sum = add(5, 3);
```

- **Function Overloading**: Defines multiple functions with the same name but different parameters.
```cpp
int add(int a, int b);
double add(double a, double b);
```

- **Default Arguments**: Specifies default values for function parameters.
```cpp
int add(int a, int b = 0);
```

- **Function Prototypes**: Declares a function signature before its definition.
```cpp
int add(int a, int b);
```

- **Recursion**: Calls a function from within itself.
```cpp
int factorial(int n) {
	if (n == 0) {
		return 1;
	}
	return n * factorial(n - 1);
}
```

- **Lambda Expressions**: Defines anonymous functions inline.
```cpp
auto sum = [](int a, int b) { return a + b; };
```
[Lambda expressions in modern C++ (in depth step by step tutorial)](https://youtu.be/MH8mLFqj-n8)

- **Function Pointers**: Stores the address of a function for dynamic invocation.
```cpp
int (*func)(int, int) = add;
int result = func(5, 3);
```

- **Inline Functions**: Expands the function code at the call site for performance.
```cpp
inline int add(int a, int b) {
	return a + b;
}
```

- **Function Templates**: Defines generic functions that work with any data type.
```cpp
template <typename T>
T add(T a, T b) {
	return a + b;
}
```

- **Recursive Lambda**: Defines a lambda function that calls itself.
```cpp
std::function<int(int)> factorial = [&](int n) {
	if (n == 0) {
		return 1;
	}
	return n * factorial(n - 1);
};
```

## Classes and Objects



## Data Types

## Resources

- [cppreference](www.cppreference.com)
- [learncpp](https://www.learncpp.com/)
- [cplusplus](http://www.cplusplus.com/)

- [cpp-cheat-sheet](https://github.com/gibsjose/cpp-cheat-sheet)
- [Modern-CPP-Programming](https://github.com/federico-busato/Modern-CPP-Programming)
