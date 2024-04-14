# C Programming Language Cheat Sheet

## Table of Contents

1. [Introduction](#introduction)
2. [Hello, World!](#hello-world)
3. [TOKEN](#token)
4. [Keywords](#keywords)
5. [Variables & Data Type](#variables--data-type)
6. [Storage Classes](#storage-classes)
7. [Characters Set](#characters-set)
8. [Operators](#operators)
9. [Control Flow](#control-flow)
10. [Header files](#header-files)
11. [Preprocessor directives](#preprocessor-directives)
12. [Functions](#functions)
13. [File Handling Functions](#file-handling-functions)
14. [Input & Output](#input--output)
15. [Pointers](#pointers)
16. [File Management](#file-management)
17. [Memory Management](#memory-management)
18. [Process management](#process-management)
19. [Synchronization](#synchronization)
20. [Thread Management](#thread-management)
21. [Signal Handling](#signal-handling)
22. [Error Handlling](#error-handling)



## Introduction

<table>

<tr>
<td> <b>Category</b> </td>
<td> <b>Information</b> </td>
</tr>
<tr>
<td>Name</td>
<td>C Programming Language</td>
</tr>
<tr>
<td>Paradigm</td>
<td>Imperative (procedural), structured</td>
</tr>
<tr>
<td>Designed by</td>
<td>Dennis Ritchie</td>
</tr>
<tr>
<td>Developer</td>
<td>Dennis Ritchie & Bell Labs (creators)</td>
</tr>
<tr>
<td>Standardization</td>
<td>ANSI C, ISO C, C99, C11</td>
</tr>
<tr>
<td>First appeared</td>
<td>1972</td>
</tr>
<tr>
<td>Stable release</td>
<td>C18 / June 2018</td>
</tr>
<tr>
<td>Typing discipline</td>
<td>Static, weak, manifest, nominal</td>
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
<td>.c (source code), .h (header files)</td>
</tr>
<tr>
<td>Compilation</td>
<td>Compiled language</td>
</tr>
<tr>
<td>Flow of Program</td>
<td> <i>Source Code</i> -> <i>Preprocessor</i> (e.g., #include) -> <i>Compiler</i> (e.g., gcc) -> <i>Linker (Combines Object Files)</i> -> <i>Executable Program</i> -> <i>Run the Program</i></td>
</tr>

<tr>
<td>Uses</td>
<td>
<ul>
  <li>Operating systems like LINUX, UNIX.</li>
  <li>CAD/ CAM Applications and Word processors.</li>
  <li>Embedded systems like ATMs, printers.</li>
  <li>RDBMS MySQL, Language Compilers and Interpreters, Print Spoolers, Loaders, Linkers, Assemblers, Text Editors, Automation tools, Network Drivers.</li>
</ul>
</td>
</tr>

<tr>
<td>Advantages</td>
<td>
<ul>
  <li>Relatively simple language</li>
  <li>Reliable (able to be trusted)</li>
  <li>Easy to understand and supports a rich set of data types</li>
  <li>Easy to use, write, modify, and debug, and quick to learn</li>
  <li>Can be compiled on a variety of computer platforms</li>
</ul>
</td>
</tr>

<tr>
<td>Key Features</td>
<td>
Simple, Machine Independent or Portable, Mid-level programming language, structured programming language, Rich Library, Memory Management, Fast Speed, Pointers, Recursion, Extensible, Robust, Highly portable
</td>
</tr>
<tr>
<td>Major implementations</td>
<td>K&R C, GCC, Clang, Intel C, C++Builder, Microsoft Visual C++, Watcom C</td>
</tr>
<tr>
<td>Dialects</td>
<td>Cyclone, Unified Parallel C, Split-C, Cilk, C*</td>
</tr>
<tr>
<td>Influenced by</td>
<td>B (BCPL, CPL), ALGOL 68, Assembly, PL/I, FORTRAN</td>
</tr>
<tr>
<td>Influenced</td>
<td>
  AMPL, AWK, csh, C++, C--, C#, Objective-C, D, Go, Java, JavaScript, Julia, Limbo, LPC, Perl,
  PHP, Pike, Processing, Python, Ring, Rust, Seed7, Vala, Verilog (HDL), Nim
</td>
</tr>

<tr>
<td>Development Environments</td>
<td>

<b>IDEs</b>: Visual Studio, Code::Blocks.<br>
<b>Text Editors</b>: Vim, Emacs.<br>
<b>Compilers</b>: GCC (GNU Compiler Collection), Clang.<br>
<b>Debuggers</b>: GDB (GNU Debugger).<br>
<b>Build Systems</b>: <a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Software%20Development%20Practices/Build%20and%20Automation%20Tools/Makefile">Make</a> and CMake.<br>
<b>Documentation</b>: Doxygen<br>
<b>Version Control</b>: git<br>
<b>Libraries</b>: 
<ul>
<li>
Standard C Library:</b> <code>stdio.h</code>, <code>stdlib.h</code>...
</li>
<li>
rnal Libraries:</b> <code>OpenGL</code>, <code>SQLite</code>...</li>
</ul>
</td>
<td>
</tr>


<tr>
<td>C / C++ categorize statements into:</td>
<td>

<ul>
<li><b>Selection<b> [<code>if</code> and <code>switch</code>]</li>
<li><b>Iteration<b> [<code>while</code>, <code>for</code>, <code>do-while</code>]</li>
<li><b>Jump<b> [<code>break</code>, <code>continue</code>, <code>goto</code> and <code>return</code>]</li>
<li><b>Label<b> [<code>case</code> and <code>default</code>]</li>
<li><b>Expression<b> [statements composed of a valid expression]</li>
<li><b>Block<b> [blocks of code. Each block begins with { and ends with } and referred to a compound statements</li>
</ul>
</td>
</tr>


</table>
 



## [Hello, World!](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)

```c
/*
- Multi-line
- Comment.
*/

#include<stdio.h> // Include header files

int main() // main() function must be there
{
printf("Hello, World!\n"); // semicolon after each statement
return 0; // indicate that program ended successfuly
} // program enclosed by curly braces

```


## TOKEN

<li><a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Keywords">Keywords</a></li>
<li>Strings</li>
<li>Operators</li>
<li>Constants</li>
<li>Identifiers</li>
<li>Special Characters</li>



## [Keywords](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Keywords)

```c
auto;		break;		case;		char;	const;		continue
default;	do;		double;		else;	enum;		extern
float;		for;		goto;		if;	int;		long
register;	return;		short;		signed;	sizeof;		static
struct;		switch;		typedef;	union;	unsigned;	void;
volatile;	while
```


## [Variables & Data Type](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Variables%20and%20Data%20Types)

### Rules for writing variable names:
<ul>
<li>Keywords should not be used.</li>
<li>Special characters should not be used as variables</li>
<li>Representing the variable names in lowercase is a virtue programming practice.</li>
<li>There is no limit on the number of characters in a variable name</li>
</ul>

Example:

```c
// Valid variables Invalid variables
char ab = 'A';
int total_mark;
int gross_weight_2020;
int area_of_sphere;

total_mark = 50;
// Invalid variables
char 8ab;
int total mark;
int gross-weight-2020;
int area_ _of_ _sphere;
```

### Primary

```c
int, char, float, double, void;

// Data type modifiers: Signed - unsigned - short - long
signed int, unsigned int, short, long, long long;
bool;
```

### Derived

```c
Function, Array, Pointer, String
```

### User-Defined

```c
struct, union, enum, typedef;
```

### Others

```c
size_t, pid_t, uid_t, gid_t, FILE, DIR, struct timeval, struct tm, struct stat, struct sockaddr, struct sockaddr_in, pthread_t, pthread_mutex_t,
```

### Type Conversion

Implicit Type Conversion:

```c
bool -> char -> short int -> int -> unsigned int -> long -> unsigned long -> long long -> float -> double -> long double
```

Explicit Type Conversion:
```c
(type) expression
```

### Macros
```c
NULL, EOF, stdin, stdout, stderr
```

### Constants
```c
O_RDONLY, O_WRONLY, O_RDWR, O_CREAT, O_APPEND, O_TRUNC, S_IRWXU, S_IRUSR, S_IWUSR, S_IXUSR, S_IRWXG, S_IRGRP, S_IWGRP, S_IXGRP, S_IRWXO, S_IROTH, S_IWOTH, S_IXOTH
```


## [Storage Classes](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Variables%20and%20Data%20Types/Storage%20Classes)

 ```c
auto //Automatic storage duration. Default for local variables.
register //Similar to auto, but suggests to the compiler to store the variable in a register for faster access.
static // Preserves the value of the variable between function calls and has a file scope if declared outside functions.
extern //Declares a variable or function that is defined in another file.
 
 ```


## Characters Set

<b>Alphabets:</b> <i>Upper case</i>, <i>Lower case</i><br>

<b>Digits:</b> <i>[0−9]</i><br>

<b>Special characters:</b>`~`, `!`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `_`, `+`, `|`, `\`, <code>&#96;</code>, `-`, `=`, `{`, `}`, `[`, `]`, `:`, `"`, `;`, `<`, `>`, `?`, `,`, `.`, `/`

<b>White spaces</b>: Blank space, New line, Carriage return, Horizontal tab

<a href="https://simple.m.wikipedia.org/wiki/File:ASCII-Table.svg">ASCII Table</a>


## [Operators](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basics/Operators)


<b>Unary:</b> <code>+</code>,
<code>-</code>,
<code>++</code>,
<code>--</code>,
<code>!</code>,
<code>&</code>,
<code>*</code>,
<code>~</code>,
<code>sizeof</code>

<b>Binary:</b>

- Arithmetic operators: <code>+</code>,
<code>-</code>,
<code>*</code>,
<code>/</code>,
<code>%</code>
- Comparison Operators: <code>==</code>,
<code>!=</code>,
<code><</code>,
<code>></code>,
<code><=</code>,
<code>>=</code>
- Logical operators: <code>&&</code>
<code>||</code>
<code>!</code>
- Assignment Operators:
<code>=</code>,
<code>+=</code>,
<code>-=</code>,
<code>*=</code>,
<code>/=</code>,
<code>%=</code>
- Bitwise Operators:  <code>&</code>,
<code>|</code>,
<code>^</code>(XOR),
<code>~</code>(complement),
<code><<</code>(left shift),
<code>>></code>(right shift)

<b>Ternary:</b> condition <code>?</code> value_if_true <code>:</code> value_if_false

<b>Other Operators:</b><br>

- <a href="https://www.geeksforgeeks.org/sizeof-operator-c/">sizeof</a>: <code>sizeof()</code>
- <a href="https://www.geeksforgeeks.org/comma-in-c/">Comma</a>: <code>( , )</code>
- <a href="https://www.geeksforgeeks.org/dot-operator-in-c-c/">dot (.)</a> and <a href="https://www.geeksforgeeks.org/arrow-operator-in-c-c-with-examples/">arrow (->)</a>: <code>.</code>, <code>-></code>
- <a href="https://www.geeksforgeeks.org/c-typecasting/">Cast Operator</a>
- &,* Operator: Pointer operator & returns the address of a variable

## [Control Flow](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Control%20Flow)

<b>Conditional statements:</b> <code>If-else</code> <code>Switch</code><br>
<b>Loops:</b> <code>for</code> <code>while</code> <code>do-while</code> <code>Break</code> <code>Continue</code> <code>goto</code>

- If pre-test is required, use `while` or `for` loop.
- If post-test is required, use `do-while` loop.
- If the number of iterations is known, use `for` loop.
- If the number of iterations is unknown, use `while` or `do-while` loop.
- If the loop body should be executed at least once, use `do-while` loop.


## Header files

<code>stdio.h</code>
<code>stdlib.h</code>
<code>string.h</code>
<code>math.h</code>
<code>time.h</code>
<code>ctype.h</code>
<code>stdarg.h</code>
<code>stddef.h</code>
<code>stdbool.h</code>
<code>limits.h</code>
<code>float.h</code>
<code>errno.h</code>
<code>assert.h</code>
<code>signal.h</code>
<code>ctype.h</code>
<code>locale.h</code>
<code>setjmp.h</code>


## [Preprocessor directives](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Preprocessor%20directives)

```c
#include
#define
#undef
#ifdef / #ifndef
#if / #elif / #else / #endif
#line
#error
#pragma
```

## [Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Functions)

### [Math Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Functions/Math%20Functions)

```c
abs(x);			sqrt(x);	pow(x, y);	sin(x);
cos(x);			tan(x);		log(x);		ceil(x);
floor(x);		round(x);	fmod(x, y);	fabs(x);
asin(x);		atan(x);	cosh(x);	sinh(x);
tanh(x);		exp(x);		log10(x);	cbrt(x);
hypot(x, y);		fmin(x, y);	fmax(x, y);	isnan(x);
isinf(x);
```

### [Data Conversion Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Functions/Data%20Conversion%20Functions)

```c
atof();		atoi();		atol();		ecvt();
fcvt();		gcvt(); 	itoa();		ltoa();
strtod();	strtol();	strtoul();	ultoa();
```

### [Character Classification Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Functions/Character%20Classification%20Functions)

```c
isalnum();	isalpha();	isdigit();	islower();	isupper();	isspace();
ispunct();	isxdigit();	isprint();	isgraph();	iscntrl();	tolower();	toupper();
```

### [String Manipulation Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Modularity%20and%20Organization/Functions/String%20Manipulation%20Functions)


```c
strlen();	strcpy();	strncpy();	strcat();	strncat();
strcmp();	strncmp();	strchr();	strrchr();	strstr();
strtok();	strspn();	strcspn();	memcpy();	memmove();
memset();	
```

### Time Library Functions

```c
time();  localtime();  asctime();  strftime();
```

### Random Number Generation Library Functions

```c
rand();  srand();
```

## [File Handling Functions](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Input%20and%20Output)

## Input & Output

### Standard I/O (stdio.h)
<b> Formatted:</b>

- Input: <code>scanf()</code>, <code>fscanf()</code>
- Output: <code>printf()</code>, <code>fprintf()</code>

<b> Unformatted:</b>

- Input: <code>getchar()</code> <code>gets()</code>
- Output: <code>putchar()</code> <code>puts()</code>

<b>Format Specifiers:</b>

- <code>%d</code> - Integer
- <code>%ld</code> - Long Integer
- <code>%lld</code> - Long Long Integer
- <code>%u</code> - Unsigned Integer
- <code>%lu</code> - Unsigned Long Integer
- <code>%llu</code> - Unsigned Long Long Integer
- <code>%f</code> - Float
- <code>%lf</code> - Double
- <code>%e, %E</code> - Exponential Notation
- <code>%c</code> - Character
- <code>%s</code> - String
- <code>%p</code> - Pointer
- <code>%x, %X</code> - Hexadecimal (Lowercase, Uppercase)
- <code>%o</code> - Octal
- <code>%g, %G</code> - Float in Shortest Form
- <code>%%</code> - Percentage


<b>Escape Sequences:</b>

- `\n`: Represents a newline character.
- `\t`: Represents a tab character.
- `\r`: Represents a carriage return character.
- `\\`: Represents a backslash character.
- `\'`: Represents a single quote character.
- `\"`: Represents a double quote character.
- `\?`: Represents a question mark character.
- `\a`: Represents an alert (bell) character.
- `\b`: Represents a backspace character.
- `\f`: Represents a form feed character.
- `\v`: Represents a vertical tab character.
- `\0`: Represents a null character.


<b>File Descriptors</b>

- stdin (0)
- stdout (1)
- stderr (2)

<b>Low-level I/O</b>

```c
open(); // Opens a file and returns a file descriptor.
read(); // Reads data from an open file into a buffer.
writ(); // Writes data from a buffer to an open file.
close(); // Closes an open file.
lseek(); // Moves the file pointer associated with an open file.
unlink(); // Removes a file from the file system.
```

<b>Buffered I/O</b>

```c
fopen(); //Opens a file for reading or writing
fclose(); // Closes the specified file stream
fflush(); // Flushes the output buffer of a stream
setvbuf(); // Sets the buffering mode and size for the specified stream
fprintf(); // Writes formatted data to the specified stream
fscanf(); // Reads formatted data from the specified stream
fread(); // Reads data from a stream into the specified buffer
fwrite(); // Writes data from the specified buffer to a stream
```

<b>Terminal I/O Library Functions</b>

```c
printf(); scanf(); getchar(); putchar(); getch(); getche(); 
```

## [Pointers](https://github.com/zelhajou/c-programming-language/tree/main/Pointers)

<b><a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Pointers/Types%20of%20Pointers">Types of Pointers: </a></b> <i>NULL Pointers</i>,
<i>Void Pointers</i>,
<i>Function Pointers</i>,
<i>Array Pointers</i>,
<i>Double Pointe</i>

<b><a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Pointers/Pointer%20Operations">Pointer Operations: </a></b> <i>Declaration and Initialization</i>,
<i>Dereferencing</i>,
<i>Pointer Arithmetic</i>,
<i>Pointer Comparison</i>,
<i>Casting Pointer</i>

<b><a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Pointers/Common%20Pointer%20Usages">Common Pointer Usages: </a></b> <i>Dynamic Memory Allocation</i>,
<i>Passing by Reference</i>,
<i>Array Manipulation</i>,
<i>Data Structures (Linked Lists)</i>,
<i>Callback Functions</i>,
<i>Pointers to Functions</i>,
<i>File Handling (File Pointers)</i>,
<i>Pointer to Structures</i>,
<i>String Manipulation</i>

<b><a href="https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Pointers/Pointer%20Pitfalls">Pointer Pitfalls:</a></b> <i>Null Pointer Dereferencing</i>,
<i>Dangling Pointers</i>,
<i>Memory Leaks</i>,
<i>Uninitialized Pointers</i>,
<i>Pointer Arithmetic Error</i>


## [File Management]()


### File Opening and Closing:

```c
fopen(); // Open a file.
fclose(); // Close a file.
```
### Reading and Writing Data:

```c
fread(); // Read data from a file.
fwrite(); // Write data to a file.
```

### File Positioning:

```c
fseek(); // Move the file pointer to a specified position.
ftell(); // Get the current position of the file pointer.
rewind(); // Move the file pointer to the beginning of the file.
```

### Directory Operations:

```c
opendir(); // Open a directory stream for reading.
readdir(); // Read a directory entry.
closedir(); // Close a directory stream.
getcwd(); // Get the current working directory.
```

### File and Directory Manipulation:

```c
mkdir(); // Create a new directory.
rmdir(); // Remove a directory.
chdir(); // Change the current working directory.
remove(); // Delete a file.
rename(); // Rename a file or directory.
link(); // Create a link to a file.
unlink(); // Remove a link to a file.
stat(); // Get file status.
```

### File Permission Functions:

```c
chmod(); Change file permissions.
access(); Check file accessibility.
```


## [Memory Management]()

### Memory Management
#### Memory Allocation:

- <b>Static Allocation:</b> Memory is allocated at compile-time<br>
- <b>Dynamic Allocation:</b> Memory is allocated at runtime<br>
- <b>Memory Layout:</b> <i>Text Segment</i>, <i>Data Segment</i>, <i>Heap</i>, <i>Stack</i>, <i>Memory Mapping (MMap)</i>, <i>Environment Variables and Command Line Arguments</i>

#### Dynamic Memory Allocation:
```c
malloc();	// Allocate memory dynamically
calloc();	// Allocate contiguous block of memory and initializes it to zero
realloc();	// Reallocate memory dynamically

// Memory Leaks Tool: Valgrind
```

#### Memory Deallocation:

```c
free(); // Deallocate memory
```

#### Memory Management:

```c
brk(); //Set the end of the data segment to the specified value.
mmap(); //Map files or devices into memory.
munmap(); //Unmap files or devices from memory.
```


## Process management

### Process States

- Running
- Ready
- Blocked (or Waiting)
- Terminated

### Process Control Block (PCB)

- Process ID (PID)
- Program counter and CPU registers
- Memory allocation details
- Process state
- Priority and scheduling information
- Open file descriptors
- Parent and child process information


### [Process control]()

```c
fork(); // Create a new process by duplicating the existing process.
exec(); // Replace the current process with a new one.
wait(); // Wait for a child process to terminate.
exit(); // Terminate the current process.

// Information Maintenance
getpid(); // Get the process ID of the current process.
getppid(); // Get the parent process ID.
getuid(); // Get the user ID of the current process.
getgid(); // Get the group ID of the current process.
uname(); // Get system information including the operating system name, version, and more
```

## Synchronization

```c
mutex
semaphore
condition variable
```


## Thread Management

```c
pthread_create(); // Used to start a new thread in the calling process
pthread_join(); // Waits for the thread specified by thread to terminate
pthread_exit(); // Terminates the calling thread.

// Synchronization
pthread_mutex_init()
pthread_mutex_destroy()
pthread_mutex_lock()
pthread_mutex_unlock()
```

## Signal Handling

### Standard Signals

- Termination Signals: <code>SIGABRT</code>, <code>SIGTERM</code>
- Interrupt Signals: <code>SIGINT</code>, <code>SIGQUIT</code>
- Fault Signals: SIGILL, <code>SIGFPE</code>, <code>SIGSEGV</code>
- Alarm Signals: <code>SIGALRM</code>, <code>SIGVTALRM</code>
- I/O Signals: <code>SIGPIPE</code>, <code>SIGPOLL</code>
- Miscellaneous Signals: <code>SIGHUP</code>,
<code>SIGBUS</code>,
<code>SIGCHLD</code>,
<code>SIGCONT</code>,
<code>SIGSTOP</code>,
<code>SIGTSTP</code>,
<code>SIGTTIN</code>,
<code>SIGTTOU</code>,
<code>SIGUSR1</code>,
<code>SIGUSR2</code>,
<code>SIGPROF</code>,
<code>SIGSYS</code>,
<code>SIGTRAP</code>,
<code>SIGURG</code>,
<code>SIGXCPU</code>,
<code>SIGXFSZ</code>
</li>
</ul>

### Real-time Signals
- Real-time Signals: <code>SIGRTMIN</code> to <code>SIGRTMAX</code></li>

### Signal Functions

#### Signal Handling:
```c
signal(); // Establishes a signal handler for a specific signal.
sigaction(); // Examines and changes the action associated with a specific signal.
```

#### Signal Sending:

```c
raise(); // Sends a signal to the calling process.
kill(); // Sends a signal to a specified process or process group.
```

#### Signal Set Manipulation:

```c
sigemptyset(); // Initializes an empty signal set.
sigfillset(); // Initializes a signal set to contain all signals.
sigaddset(); // Adds a specified signal to a signal set.
sigdelset(); // Removes a specified signal from a signal set.
sigismember(); // Checks if a specified signal is a member of a signal set.
```

#### Signal Masking:

```c
sigprocmask(); // Examines and changes the calling process's signal mask.
```

## [Error Handlling](https://github.com/zelhajou/c-programming-language-cheat-sheet/tree/main/Basic/Error%20Handling)

```c
perror();
strerror();
```
