A C program memory layout in C mainly comprises six components these are :

1. **Text Segment (Code Segment):**

    - This segment contains the executable code of the program.
    - It is typically read-only to prevent accidental modification of the code.
    - It starts at a fixed memory address and contains the machine instructions of the program.
2. **Data Segment:**

    - The data segment is further divided into two parts:
        - **Initialized Data Segment (or Data Section):**
            - This part contains global and static variables that are explicitly initialized by the programmer.
            - It is often called the "data section."
            - Data in this segment has a known initial value, and it's stored in the binary executable.
        - **Uninitialized Data Segment (BSS - Block Started by Symbol):**
            - This part contains global and static variables that are not explicitly initialized by the programmer.
            - It is often called the "bss section."
            - Data in this segment is initialized to zero by the system loader.
3. **Heap:**

    - The heap is a dynamically allocated memory area where dynamic memory allocation functions like `malloc`, `calloc`, and `realloc` allocate memory during program execution.
    - It's used for storing data structures such as linked lists, trees, and user-managed memory.
    - Memory allocation and deallocation on the heap are under the control of the programmer.
4. **Stack:**

    - The stack is used for managing function call frames, local variables, and function parameters.
    - It operates in a last-in-first-out (LIFO) manner, meaning the most recently called function's information is at the top of the stack.
    - The stack's size is typically fixed or limited and is managed by the operating system.
5. **Memory Mapping (MMap):**

    - In some systems, memory-mapped files are used for efficiently reading and writing data between memory and disk storage.
    - This can include memory-mapped I/O and shared memory regions.
6. **Environment Variables and Command Line Arguments:**

    - Environment variables and command line arguments are typically stored in the process's memory space.