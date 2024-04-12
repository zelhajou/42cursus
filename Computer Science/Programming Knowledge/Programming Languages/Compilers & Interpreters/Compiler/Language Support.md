
# [[C]] and [[C++]] 

C and C++  have compilers like GCC (GNU Compiler Collection) and Clang

#### C compilation process:

1. **Writing C Source Code:** You start by writing your C program in a plain text file with a `.c` extension using a text editor or integrated development environment (IDE). This file contains the human-readable source code.

2. **Preprocessing:** In this stage, the C preprocessor (`cpp`) is invoked. It handles preprocessor directives, which are lines in your code starting with `#`. Common directives include `#include` for including header files and `#define` for macros. The preprocessor performs tasks like file inclusion and macro substitution. The result is a modified source code file, often with a `.i` extension.
   Example:
```c
#include <stdio.h>
#define PI 3.14159
```

3. **Compilation:** The modified source code is passed to the compiler (`gcc` for the GNU C Compiler). The compiler translates the C source code into assembly code or an intermediate representation (e.g., abstract syntax tree or AST).

4. **Assembly (Optional):** In this step, the compiler generates assembly code from the intermediate representation. This is an optional step, and many modern compilers can directly generate machine code. If assembly code is generated, it's typically saved in a file with a `.s` extension.

5. **Assembly to Object Code:** If assembly code was generated, it needs to be assembled into machine code. This is done using an assembler (`as`). The result is one or more object files (`.o` or `.obj`).

6. **Linking:** If your program uses functions or code from external libraries or other source files, the linker (`ld`) is responsible for resolving references to these external symbols and combining all object files into an executable program. This step produces an executable file, often with no extension (e.g., `a.out` on Unix-like systems).
   Example (Compiling and Linking Multiple Source Files):
```bash
gcc -o my_program file1.c file2.c   
```

7. **Execution:** Finally, you can run the compiled program from the command line or within an integrated development environment (IDE). The operating system loads the program into memory, and it starts executing.
   Example (Running the Compiled Program):
```bash
./my_program
```

##### Warning flags :
When compiling a C program, you can use warning flags to enable the compiler to provide you with warnings about potential issues in your code. These warnings help you catch common mistakes and improve the quality of your code.

