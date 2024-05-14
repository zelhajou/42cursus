# C++ Programming Language cheat sheet

## Table of Contents

- [C++ Programming Language cheat sheet](#c-programming-language-cheat-sheet) 
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Resources](#resources)

## Introduction

C++ is a powerful and versatile programming language that is widely used in the software development industry. Developed by Bjarne Stroustrup in the early 1980s, C++ is an extension of the C programming language with added features such as object-oriented programming (OOP) capabilities, generic programming support, and improved memory management.

One of the key features of C++ is its efficiency and performance. It allows low-level manipulation of memory through features like pointers, making it suitable for system programming and applications where performance is critical. At the same time, C++ provides high-level abstractions through OOP, enabling developers to organize and structure their code in a more modular and reusable way.

C++ has a rich standard library that provides a wide range of functions and data structures, allowing developers to accomplish various tasks without having to reinvent the wheel. Additionally, C++ supports multiple programming paradigms including procedural, object-oriented, and generic programming, giving developers the flexibility to choose the most appropriate approach for their projects.

C++ is used extensively in industries such as game development, system programming, embedded systems, finance, and high-performance computing. Its popularity stems from its combination of power, flexibility, and performance, making it a preferred choice for many developers and organizations worldwide.


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

## References

- [cppreference](www.cppreference.com)
- [learncpp](https://www.learncpp.com/)
- [cplusplus](http://www.cplusplus.com/)

- [cpp-cheat-sheet](https://github.com/gibsjose/cpp-cheat-sheet)
- [Modern-CPP-Programming](https://github.com/federico-busato/Modern-CPP-Programming)



## Online editors

- [cppinsights](https://www.cppinsights.io/)
- [godbolt](https://www.godbolt.org/)