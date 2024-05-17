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

3. **Set up a build system**: To compile and run your C++ code, you need a build system that automates the compilation process. Common build systems for C++ include:

   - Make: A build automation tool that uses Makefiles to specify build rules.
   - CMake: A cross-platform build system generator that simplifies the process of building C++ projects.
   - Visual Studio Build Tools: A set of tools provided by Microsoft for building C++ projects on Windows.

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

Type casting in C++ is the process of converting a variable from one data type to another. It can be done implicitly by the compiler or explicitly by the programmer using casting operators.

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

- **C++ Casting Operators**: `static_cast`, `dynamic_cast`, `const_cast`, `reinterpret_cast`.

	`satic_cast` : It is used to convert one data type to another. It is similar to the C-style cast but provides more type safety.

	```cpp
	double x = 3.14;
	int y = static_cast<int>(x); // Convert double to int
	```

	`dynamic_cast` : It is used for safe downcasting of pointers and references in polymorphic classes.

	```cpp
	class Base {
	public:
		virtual void foo() {}
	};

	class Derived : public Base {};

	int main() {
		Base *base = new Derived;
		Derived *derived = dynamic_cast<Derived*>(base);
		if (derived) {
			derived->foo();
		}
		delete base;
		return 0;
	}
	```

	`const_cast` : It is used to add or remove const or volatile qualifiers from a variable.

	```cpp
	const int x = 42;
	int y = const_cast<int>(x); // Remove const qualifier
	```

	`reinterpret_cast` : It is used to convert one pointer type to another pointer type or to convert a pointer to an integer type.

	```cpp
	#include <iostream>
	int main() {
		int num = 42;
		int *num_ptr = &num;

		// Disguise the integer pointer as a char pointer
		char *char_ptr = reinterpret_cast<char *>(num_ptr);

		for (size_t i = 0; i < sizeof(int); ++i) {
			// Print the individual bytes of the integer as characters
			std::cout << "Byte " << i << ": " << char_ptr[i] << std::endl;
		}

		return 0;
	}
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

### Conditional Compilation

- **Conditional Compilation**: `#ifdef`, `#ifndef`, `#endif`, `#if`, `#else`, `#elif`

### Macros

- **Define Macro**: `#define NAME value`
- **Conditional Macro**: `#ifdef`, `#ifndef`, `#endif`

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

## Memory Model

The memory model in C++ defines how the program stores and accesses data in computer memory. It consists of different segments, such as the Stack, Heap, Data and Code segments. Each of these segments is used to store different types of data and has specific characteristics.

### Stack

- **LIFO Data Structure**: Last In, First Out.
- **Automatic Memory Management**: Memory is allocated and deallocated automatically.
- **Local Variables**: Function parameters and local variables are stored on the stack.
- **Fixed Size**: Stack size is limited and determined at compile time.
- **Faster Access**: Faster access compared to the heap.

```cpp
void foo() {
	int x = 42; // Stored on the stack
}
```

### Heap

- **Dynamic Memory Allocation**: Memory is allocated and deallocated manually.
- **Unlimited Size**: Heap size is limited by available memory.
- **Slower Access**: Slower access compared to the stack.
- **Data Structures**: Objects, arrays, and data structures are stored on the heap.

```cpp
int *ptr = new int; // Allocated on the heap
delete ptr; // Deallocated manually
```

### Data Segment

- **Global and Static Variables**: Global variables and static variables are stored in the data segment.
- **Initialized Data**: Data with static or constant values is stored in this segment.
- **Read-Only Memory**: Data in this segment is read-only and cannot be modified.

```cpp
int globalVar = 42; // Stored in the data segment
static int staticVar = 42; // Stored in the data segment
```

### Code Segment

- **Executable Code**: Machine instructions and program code are stored in the code segment.
- **Read-Only Memory**: Code in this segment is read-only and cannot be modified.
- **Program Instructions**: Instructions for the program execution are stored in this segment.

```cpp
int main() {
	return 0; // Executable code in the code segment
}
```

## Memory Management

Memory management in C++ is the process of allocating and deallocating memory for program data. It involves managing memory segments, dynamic memory allocation, and avoiding memory leaks and memory corruption.

### Static Memory Allocation

- **Compile-Time Allocation**: Memory is allocated at compile time.
- **Automatic Variables**: Local variables and function parameters are allocated on the stack.
- **Fixed Size**: Stack size is determined at compile time.

```cpp
void foo() {
	int x = 42; // Allocated on the stack
}
```

### Dynamic Memory Allocation

- **Run-Time Allocation**: Memory is allocated at run time using the heap.
- **Manual Management**: Memory must be deallocated manually to avoid memory leaks.


## Input and Output

Input and output operations in C++ are performed using the `iostream` library, which provides classes and objects for reading from and writing to the console, files, and other input/output devices.

### Output (Printing)

- **Standard Output Stream**: `std::cout`
  - **Description**: Used for printing output to the console.
  - **Example**:
    ```cpp
    #include <iostream>
    int main() {
        std::cout << "Hello, world!" << std::endl;
        return 0;
    }
    ```
- **Standard Error Stream**: `std::cerr`
    - **Description**: Used for printing error messages to the console.
    - **Example**:
        ```cpp
        #include <iostream>
        int main() {
            std::cerr << "Error: File not found!" << std::endl;
            return 1;
        }
        ```
- **Standard Log Stream**: `std::clog`
    - **Description**: Used for printing log messages to the console.
    - **Example**:
        ```cpp
        #include <iostream>
        int main() {
            std::clog << "Log: Program started" << std::endl;
            return 0;
        }
        ```
- **Formatting Output**: `std::setw`, `std::setprecision`, `std::fixed`, `std::scientific`
    - **Description**: Used to format the output of numeric values.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <iomanip>
        int main() {
            double pi = 3.14159;
            std::cout << std::fixed << std::setprecision(2) << pi << std::endl;
            return 0;
        }
        ```
- **Output Manipulators**: `std::endl`, `std::setw`, `std::setfill`, `std::setprecision`
    - **Description**: Used to control the formatting of output.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <iomanip>
        int main() {
            int x = 42;
            std::cout << std::setw(10) << std::setfill('*') << x << std::endl;
            return 0;
        }
        ```
### Input (Reading)

- **Standard Input Stream**: `std::cin`
    - **Description**: Used for reading input from the console.
    - **Example**:
        ```cpp
        #include <iostream>
        int main() {
            int number;
            std::cout << "Enter a number: ";
            std::cin >> number;
            std::cout << "You entered: " << number << std::endl;
            return 0;
        }
        ```

- **Reading Strings**: `std::getline`
    - **Description**: Used to read a line of text from the console.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <string>
        int main() {
            std::string name;
            std::cout << "Enter your name: ";
            std::getline(std::cin, name);
            std::cout << "Hello, " << name << "!" << std::endl;
            return 0;
        }
        ```
- **Input Validation**: `std::cin.fail()`, `std::cin.clear()`, `std::cin.ignore()`
    - **Description**: Used to handle input errors and clear the input buffer.
    - **Example**:
        ```cpp
        #include <iostream>
        int main() {
            int number;
            while (true) {
                std::cout << "Enter a number: ";
                std::cin >> number;
                if (std::cin.fail()) {
                    std::cin.clear();
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    std::cout << "Invalid input. Please try again." << std::endl;
                } else {
                    std::cout << "You entered: " << number << std::endl;
                    break;
                }
            }
            return 0;
        }
        ```


## File Handling

File handling in C++ is performed using the `fstream` library, which provides classes and objects for reading from and writing to files. The library includes the `ifstream`, `ofstream`, and `fstream` classes for input, output, and input/output operations, respectively.

### Reading from Files

- **Reading from a File**: `std::ifstream`
    - **Description**: Used to read data from a file.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ifstream file("data.txt");
            if (file.is_open()) {
                std::string line;
                while (std::getline(file, line)) {
                    std::cout << line << std::endl;
                }
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### Writing to Files

- **Writing to a File**: `std::ofstream`
    - **Description**: Used to write data to a file.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ofstream file("output.txt");
            if (file.is_open()) {
                file << "Hello, world!" << std::endl;
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### Appending to Files

- **Appending to a File**: `std::ofstream` with `std::ios::app`
    - **Description**: Used to append data to an existing file.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ofstream file("output.txt", std::ios::app);
            if (file.is_open()) {
                file << "Hello, world!" << std::endl;
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### Binary Files

- **Reading/Writing Binary Files**: `std::ios::binary`
    - **Description**: Used to read/write binary data to/from a file.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ofstream file("data.bin", std::ios::binary);
            if (file.is_open()) {
                int data[] = {1, 2, 3, 4, 5};
                file.write(reinterpret_cast<char*>(data), sizeof(data));
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### Error Handling

- **Checking File Status**: `is_open()`, `good()`, `fail()`, `bad()`
    - **Description**: Used to check the status of file operations.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ifstream file("data.txt");
            if (file.is_open()) {
                std::cout << "File opened successfully." << std::endl;
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### File Positioning

- **Seeking in a File**: `seekg`, `seekp`, `tellg`, `tellp`
    - **Description**: Used to move the file pointer to a specific position.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::ifstream file("data.txt");
            if (file.is_open()) {
                file.seekg(5, std::ios::beg);
                std::string line;
                std::getline(file, line);
                std::cout << "Line: " << line << std::endl;
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```
### File Streams

- **File Streams**: `std::ifstream`, `std::ofstream`, `std::fstream`
    - **Description**: Used for input, output, and input/output file operations.
    - **Example**:
        ```cpp
        #include <iostream>
        #include <fstream>
        int main() {
            std::fstream file("data.txt", std::ios::in | std::ios::out);
            if (file.is_open()) {
                std::string line;
                while (std::getline(file, line)) {
                    std::cout << line << std::endl;
                }
                file.close();
            } else {
                std::cerr << "Error: Unable to open file." << std::endl;
            }
            return 0;
        }
        ```


## Data Structures

Data structures in C++ are used to store and organize data in memory. They include arrays, vectors, linked lists, stacks, queues, trees, and graphs, among others. Data structures provide efficient ways to access, insert, delete, and manipulate data.

### Arrays

- **Fixed-Size Collection**: `int arr[5];`
- **Accessing Elements**: `arr[index]`
- **Iterating Over Elements**: `for (int i = 0; i < size; i++)`
- **Multidimensional Arrays**: `int matrix[3][3];`

```cpp
#include <iostream>
int main() {
	int arr[5] = {1, 2, 3, 4, 5};
	for (int i = 0; i < 5; i++) {
		std::cout << arr[i] << std::endl;
	}
	return 0;
}
```

### Strings

- **Character Array**: `char str[] = "Hello";`
- **String Class**: `std::string str = "Hello";`
- **String Operations**: `str.length()`, `str.find()`, `str.substr()`

```cpp
#include <iostream>
#include <string>

int main() {
	std::string str = "Hello, world!";
	std::cout << "Length: " << str.length() << std::endl;
	std::cout << "Substring: " << str.substr(0, 5) << std::endl;
	return 0;
}
```

### Vectors

- **Dynamic Array**: `std::vector<int> vec;`
- **Adding Elements**: `vec.push_back(value);`
- **Accessing Elements**: `vec[index]`
- **Iterating Over Elements**: `for (int i = 0; i < vec.size(); i++)`

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> vec = {1, 2, 3, 4, 5};
	vec.push_back(6);
	for (int i = 0; i < vec.size(); i++) {
		std::cout << vec[i] << std::endl;
	}
	return 0;
}
```

### Linked Lists

- **Dynamic Collection of Nodes**: `struct Node { int data; Node* next; };`
- **Singly Linked List**: `Node* head = nullptr;`
- **Doubly Linked List**: `struct Node { int data; Node* prev; Node* next; };`

```cpp
#include <iostream>

struct Node {
	int data;
	Node* next;
};

int main() {
	Node* head = nullptr;
	Node* node1 = new Node{1, nullptr};
	Node* node2 = new Node{2, nullptr};
	head = node1;
	node1->next = node2;
	std::cout << head->data << std::endl;
	std::cout << head->next->data << std::endl;
	return 0;
}
```

### Stacks

- **LIFO Data Structure**: Last In, First Out.
- **Operations**: `push()`, `pop()`, `top()`
- **Implementation**: Using arrays or linked lists.

```cpp
#include <iostream>
#include <stack>

int main() {
	std::stack<int> s;
	s.push(1);
	s.push(2);
	s.push(3);
	while (!s.empty()) {
		std::cout << s.top() << std::endl;
		s.pop();
	}
	return 0;
}
```

### Queues

- **FIFO Data Structure**: First In, First Out.
- **Operations**: `push()`, `pop()`, `front()`, `back()`
- **Implementation**: Using arrays or linked lists.

```cpp
#include <iostream>
#include <queue>

int main() {
	std::queue<int> q;
	q.push(1);
	q.push(2);
	q.push(3);
	while (!q.empty()) {
		std::cout << q.front() << std::endl;
		q.pop();
	}
	return 0;
}
```

### Trees

- **Hierarchical Data Structure**: Nodes connected by edges.
- **Binary Tree**: Each node has at most two children.
- **Binary Search Tree**: Left child < parent < right child.

```cpp
#include <iostream>

struct Node {
	int data;
	Node* left;
	Node* right;
};

int main() {
	Node* root = new Node{1, nullptr, nullptr};
	Node* left = new Node{2, nullptr, nullptr};
	Node* right = new Node{3, nullptr, nullptr};
	root->left = left;
	root->right = right;
	std::cout << root->data << std::endl;
	std::cout << root->left->data << std::endl;
	std::cout << root->right->data << std::endl;
	return 0;
}
```

### Graphs

- **Non-Linear Data Structure**: Vertices connected by edges.
- **Directed Graph**: Edges have a direction.
- **Undirected Graph**: Edges have no direction.

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<std::vector<int>> graph = {
		{0, 1, 1, 0},
		{1, 0, 1, 1},
		{1, 1, 0, 1},
		{0, 1, 1, 0}
	};
	for (int i = 0; i < graph.size(); i++) {
		for (int j = 0; j < graph[i].size(); j++) {
			std::cout << graph[i][j] << " ";
		}
		std::cout << std::endl;
	}
	return 0;
}
```

## Algorithms

Algorithms in C++ are step-by-step procedures for solving problems or performing tasks. They include searching, sorting, graph traversal, and other common operations. C++ provides standard algorithms in the `<algorithm>` header and data structures in the `<vector>`, `<list>`, and `<map>` headers.

### Searching Algorithms

- **Linear Search**: `std::find()`
- **Binary Search**: `std::binary_search()`
- **Search in Sorted Containers**: `std::lower_bound()`, `std::upper_bound()`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
	std::vector<int> vec = {1, 2, 3, 4, 5};
	auto it = std::find(vec.begin(), vec.end(), 3);
	if (it != vec.end()) {
		std::cout << "Element found at index: " << it - vec.begin() << std::endl;
	} else {
		std::cout << "Element not found." << std::endl;
	}
	return 0;
}
```

### Sorting Algorithms

- **Sort Range**: `std::sort()`
- **Partial Sort**: `std::partial_sort()`
- **Heap Operations**: `std::make_heap()`, `std::push_heap()`, `std::pop_heap()`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
	std::vector<int> vec = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
	std::sort(vec.begin(), vec.end());
	for (int num : vec) {
		std::cout << num << " ";
	}
	std::cout << std::endl;
	return 0;
}
```


### Graph Algorithms

- **Depth-First Search (DFS)**: Recursive traversal of a graph.
- **Breadth-First Search (BFS)**: Iterative traversal of a graph.
- **Shortest Path Algorithms**: Dijkstra's, Bellman-Ford, Floyd
- **Minimum Spanning Tree**: Prim's, Kruskal's

```cpp
#include <iostream>
#include <vector>
#include <queue>

void bfs(std::vector<std::vector<int>>& graph, int start) {
	std::vector<bool> visited(graph.size(), false);
	std::queue<int> q;
	q.push(start);
	visited[start] = true;
	while (!q.empty()) {
		int node = q.front();
		q.pop();
		std::cout << node << " ";
		for (int neighbor : graph[node]) {
			if (!visited[neighbor]) {
				q.push(neighbor);
				visited[neighbor] = true;
			}
		}
	}
}

int main() {
	std::vector<std::vector<int>> graph = {
		{1, 2},
		{0, 2, 3},
		{0, 1, 3},
		{1, 2}
	};
	bfs(graph, 0);
	std::cout << std::endl;
	return 0;
}
```

### Dynamic Programming

- **Memoization**: Caching results of subproblems.
- **Tabulation**: Bottom-up approach to dynamic programming.
- **Optimal Substructure**: Decomposing a problem into subproblems.

```cpp
#include <iostream>
#include <vector>

int fibonacci(int n) {
	std::vector<int> dp(n + 1, 0);
	dp[1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	return dp[n];
}

int main() {
	int n = 10;
	std::cout << "Fibonacci(" << n << ") = " << fibonacci(n) << std::endl;
	return 0;
}
```

### Backtracking

- **Recursive Approach**: Generate all possible solutions.
- **Pruning**: Eliminate invalid solutions early.
- **State Space Tree**: Representing all possible states.

```cpp
#include <iostream>
#include <vector>

void generateSubsets(std::vector<int>& nums, std::vector<int>& subset, int index) {
	if (index == nums.size()) {
		for (int num : subset) {
			std::cout << num << " ";
		}
		std::cout << std::endl;
		return;
	}
	subset.push_back(nums[index]);
	generateSubsets(nums, subset, index + 1);
	subset.pop_back();
	generateSubsets(nums, subset, index + 1);
}

int main() {
	std::vector<int> nums = {1, 2, 3};
	std::vector<int> subset;
	generateSubsets(nums, subset, 0);
	return 0;
}
```

### Greedy Algorithms

- **Greedy Choice Property**: Make the locally optimal choice.
- **Optimal Substructure**: Decompose problem into subproblems.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int coinChange(std::vector<int>& coins, int amount) {
	std::sort(coins.begin(), coins.end(), std::greater<int>());
	int count = 0;
	for (int coin : coins) {
		count += amount / coin;
		amount %= coin;
	}
	return amount == 0 ? count : -1;
}

int main() {
	std::vector<int> coins = {1, 2, 5};
	int amount = 11;
	std::cout << "Minimum coins: " << coinChange(coins, amount) << std::endl;
	return 0;
}
```

### Divide and Conquer

- **Divide**: Break problem into smaller subproblems.
- **Conquer**: Solve subproblems recursively.
- **Combine**: Merge solutions of subproblems.

```cpp
#include <iostream>
#include <vector>

int binarySearch(std::vector<int>& nums, int target) {
	int left = 0, right = nums.size() - 1;
	while (left <= right) {
		int mid = left + (right - left) / 2;
		if (nums[mid] == target) {
			return mid;
		} else if (nums[mid] < target) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	return -1;
}

int main() {
	std::vector<int> nums = {1, 2, 3, 4, 5};
	int target = 3;
	std::cout << "Index: " << binarySearch(nums, target) << std::endl;
	return 0;
}
```

### Randomized Algorithms

- **Randomized Choices**: Make random decisions.
- **Monte Carlo Algorithms**: Use random sampling.
- **Las Vegas Algorithms**: Randomized with deterministic guarantees.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

int randomPartition(std::vector<int>& nums, int left, int right) {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<int> dis(left, right);
	int pivotIndex = dis(gen);
	int pivotValue = nums[pivotIndex];
	std::swap(nums[pivotIndex], nums[right]);
	int i = left;
	for (int j = left; j < right; j++) {
		if (nums[j] < pivotValue) {
			std::swap(nums[i], nums[j]);
			i++;
		}
	}
	std::swap(nums[i], nums[right]);
	return i;
}

void quickSort(std::vector<int>& nums, int left, int right) {
	if (left < right) {
		int pivot = randomPartition(nums, left, right);
		quickSort(nums, left, pivot - 1);
		quickSort(nums, pivot + 1, right);
	}
}

int main() {
	std::vector<int> nums = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
	quickSort(nums, 0, nums.size() - 1);
	for (int num : nums) {
		std::cout << num << " ";
	}
	std::cout << std::endl;
	return 0;
}
```

## Exception Handling

Exception handling in C++ is a mechanism for handling runtime errors and abnormal conditions. It allows you to catch and handle exceptions, propagate errors, and clean up resources in case of failures.

### Basics

- **Throwing Exceptions**: `throw exception;`
- **Catching Exceptions**: `try { /* code */ } catch (ExceptionType e) { /* handler */ }`
- **Rethrowing Exceptions**: `throw;`

```cpp
#include <iostream>

int divide(int a, int b) {
    if (b == 0) {
        throw "Division by zero!";
    }
    return a / b;
}

int main() {
    int num1, num2;

    std::cout << "Enter two numbers for division: ";
    std::cin >> num1 >> num2;

    try {
        int result = divide(num1, num2);
        std::cout << "The result is: " << result << std::endl;
    } catch (const char* msg) {
        std::cerr << "Error: " << msg << std::endl;
    }

    return 0;
}
```

### Standard Exceptions

C++ provides a set of standard exceptions that can be used to handle common error conditions. These exceptions are defined in the `<stdexcept>` header.

- **std::exception**: Base class for all standard exceptions.
- **std::runtime_error**: Exception for runtime errors.
- **std::logic_error**: Exception for logical errors.
- **std::invalid_argument**: Exception for invalid arguments.
- **std::out_of_range**: Exception for out-of-range errors.

```cpp
#include <iostream>
#include <stdexcept>

int divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Division by zero!");
    }
    return a / b;
}

int main() {
    int num1, num2;

    std::cout << "Enter two numbers for division: ";
    std::cin >> num1 >> num2;

    try {
        int result = divide(num1, num2);
        std::cout << "The result is: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```

### Custom Exceptions






## Compilers

A compiler is a software tool that translates source code written in a high-level programming language into machine code that can be executed by a computer. C++ compilers are used to compile C++ programs and generate executable files that can run on various platforms.

### Popular C++ Compilers

- **GCC (GNU Compiler Collection)**: A free and open-source compiler that supports multiple programming languages, including C++.
- **Clang**: A compiler front end for the C, C++, and Objective-C programming languages.
- **Microsoft Visual C++**: A compiler provided by Microsoft for Windows development.
- **Intel C++ Compiler**: A commercial compiler from Intel that supports C++ and other languages.

### Compilation Process

- **Preprocessing**: The preprocessor processes the source code and handles directives such as `#include` and `#define`.
- **Compilation**: The compiler translates the preprocessed code into object code (machine code).
- **Linking**: The linker combines the object code with libraries to create an executable file.
- **Loading**: The operating system loads the executable file into memory and starts execution.

### Compiler Flags

- **Optimization Flags**: `-O0`, `-O1`, `-O2`, `-O3`
- **Debugging Flags**: `-g`, `-ggdb`, `-g3`
- **Warning Flags**: `-Wall`, `-Wextra`, `-Werror`
- **Include Directories**: `-I<path>`
- **Library Directories**: `-L<path>`
- **Linker Flags**: `-l<library>`
- **Preprocessor Definitions**: `-D<name>=<value>`
- **Output File**: `-o <output>`
- **Compile Only**: `-c`

### IDEs and Text Editors

- **Visual Studio**: A full-featured IDE from Microsoft that provides comprehensive C++ development tools.
- **Visual Studio Code**: A lightweight and versatile code editor with C++ support through extensions.
- **CLion**: A cross-platform C++ IDE from JetBrains that offers advanced code analysis and refactoring features.
- **Code::Blocks**: An open-source IDE that supports multiple compilers and platforms.
- **Eclipse**: An extensible IDE that supports C++ development through plugins.

### Online Compilers

- **Compiler Explorer**: An online tool that allows you to explore the assembly output of C++ code.
- **repl.it**: An online platform that provides a C++ compiler and editor for writing and running code.
- **Ideone**: An online compiler and debugging tool that supports multiple programming languages.
- **[cppinsights](https://www.cppinsights.io/)**: An online tool that shows the transformation of C++ code to assembly code.
- **[godbolt](https://www.godbolt.org/)**: An online compiler explorer that shows the assembly output of C++ code.

## Debugging

Debugging is the process of identifying and fixing errors in a program. C++ provides various tools and techniques for debugging code, including print statements, breakpoints, and debugging tools.

### Debugging Techniques

- **Print Statements**: Use `std::cout` to print debug messages to the console.
- **Assertions**: Use `assert` to check conditions and halt the program if they are false.
- **Logging**: Use logging libraries to record debug information to a file.
- **Debugging Tools**: Use IDEs and debuggers to set breakpoints, inspect variables, and step through code.


### Debugging Tools

- **GDB (GNU Debugger)**: A command-line debugger that supports various features for debugging C++ programs.
- **LLDB**: A debugger provided by LLVM that supports debugging C++ code on macOS and Linux.
- **Visual Studio Debugger**: A graphical debugger provided by Microsoft for debugging C++ programs on Windows.
- **Valgrind**: A memory debugging tool that helps identify memory leaks and other memory-related errors.

### Debugging Tips

- **Start Small**: Debug small sections of code at a time to isolate errors.
- **Use Breakpoints**: Set breakpoints to pause execution and inspect variables.
- **Check Inputs**: Verify input data and function parameters for correctness.
- **Review Code**: Review code for logical errors and common mistakes.
- **Use Version Control**: Use version control systems to track changes and revert to previous versions.

## Build Systems

Build systems are tools that automate the process of compiling, linking, and packaging software projects. They manage dependencies, build configurations, and target platforms to generate executable files from source code.

### Build Tools

- **Make**: A build automation tool that uses Makefiles to specify build rules.
- **CMake**: A cross-platform build system generator that simplifies the process of building C++ projects.
- **Ninja**: A fast and lightweight build tool that can be used with CMake.
- **Bazel**: A build system from Google that supports large-scale projects and multiple languages.

### GNU Make

A Makefile is a file that specifies build rules and dependencies for a project. It contains targets, dependencies, variables, and phony targets that define how to build specific files or executables.

- **Makefile**: A file that specifies build rules and dependencies for a project.
- **Targets**: Rules that define how to build specific files or executables.
- **Dependencies**: Files or targets that must be built before a target can be built.
- **Variables**: Values that can be used to customize the build process.
- **Phony Targets**: Targets that do not correspond to actual files but perform specific actions.

```makefile
# Variables
CXX = g++
CXXFLAGS = -Wall -Iinclude
SRC = src/main.cpp
OBJ = main.o
EXE = my_program

# Rules
$(EXE): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(EXE) $(OBJ)

$(OBJ): $(SRC)
	$(CXX) $(CXXFLAGS) -c $(SRC)

# Phony targets
.PHONY: clean
clean:
	rm -f $(OBJ) $(EXE)
```


## languge Concepts

### Undefine Behaviour

Undefined behavior in C++ refers to code constructs and operations that do not have well-defined semantics according to the C++ standard. It can lead to unpredictable program behavior, crashes, and security vulnerabilities. Avoiding undefined behavior is essential for writing safe and reliable code.

#### Examples of Undefined Behavior

- **Null Pointer Dereference**: Accessing or dereferencing a null pointer.
- **Buffer Overflow**: Writing to or reading from memory outside the bounds of an array.
- **Uninitialized Variables**: Using variables before they are initialized.
- **Signed Integer Overflow**: Overflowing a signed integer value.
- **Division by Zero**: Dividing an integer by zero.

#### Handling Undefined Behavior

- **Avoid Undefined Behavior**: Write safe and well-defined code to prevent undefined behavior.
- **Use Static Analysis Tools**: Use tools that analyze code for potential undefined behavior.
- **Compiler Warnings**: Enable compiler warnings to catch potential issues at compile time.
- **Testing and Debugging**: Test code thoroughly and use debugging tools to identify issues.

### Macros

Macros in C++ are preprocessor directives that define symbolic constants, functions, or code snippets. They are used to simplify code, improve readability, and enable conditional compilation.

#### Defining Macros

- **Object-like Macros**: `#define PI 3.14159`
- **Function-like Macros**: `#define SQUARE(x) ((x) * (x))`
- **Conditional Macros**: `#ifdef`, `#ifndef`, `#else`, `#endif`

```cpp
#include <iostream>
#define PI 3.14159
#define SQUARE(x) ((x) * (x))

int main() {
	double radius = 5.0;
	double area = PI * SQUARE(radius);
	std::cout << "Area: " << area << std::endl;
	return 0;
}
```
#### Macros vs. Constants

- **Macros**: Processed by the preprocessor and replaced in the code.
- **Constants**: Typed values that are stored in memory and have a defined scope.
- **Benefits of Macros**: Flexibility, code reuse, conditional compilation.
- **Drawbacks of Macros**: Lack of type safety, potential side effects, readability issues.

### Argument Dependent Lookup (ADL)

Argument-dependent lookup (ADL) in C++ is a mechanism that allows functions and operators to be found by the compiler based on the types of arguments passed to them. It is also known as Koenig lookup after its creator Andrew Koenig.

#### Example of ADL

```cpp
#include <iostream>

namespace my_namespace {
	struct MyType {};
	void foo(MyType) {
		std::cout << "ADL: foo(MyType)" << std::endl;
	}
}

int main() {
	my_namespace::MyType obj;
	foo(obj); // ADL: foo(MyType)
	return 0;
}
```

### Inline Functions

Inline functions in C++ are functions that are expanded in place at the call site instead of being called through a function call. They are used to reduce function call overhead and improve performance by eliminating the function call stack.

#### Defining Inline Functions

- **Inline Functions**: `inline return_type function_name(parameters) { /* code */ }`
- **Header-Only Libraries**: Define functions in header files to allow inlining.
- **Benefits of Inlining**: Reduced function call overhead, improved performance, reduced code size.
- **Drawbacks of Inlining**: Increased code size, reduced cache locality, longer compile times.

```cpp
#include <iostream>
inline int add(int a, int b) {
	return a + b;
}


## Resources

- [cppreference](www.cppreference.com)
- [learncpp](https://www.learncpp.com/)
- [cplusplus](http://www.cplusplus.com/)
- [cpp-cheat-sheet](https://github.com/gibsjose/cpp-cheat-sheet)
- [Modern-CPP-Programming](https://github.com/federico-busato/Modern-CPP-Programming)
