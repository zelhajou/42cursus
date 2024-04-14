Memory management is a fundamental aspect of computer systems and programming languages. It involves the allocation and deallocation of memory resources in a way that maximizes the efficient use of a computer's memory while minimizing memory leaks, fragmentation, and other potential issues. 

# 1. Memory Resources:
- A computer's memory resources include both main memory (RAM) and secondary storage (such as hard drives or SSDs).
- Main memory is fast but limited in size, while secondary storage is slower but provides larger storage capacity.

# 2. Memory Hierarchy:
- Computer memory is organized into a hierarchy with different levels, each with varying speed and capacity. Common levels include registers, cache, main memory, and secondary storage.
- Memory management aims to optimize the use of these memory levels to improve program performance.

# 3. Memory Allocation:

# 4. Dynamic Memory Allocation:

- Dynamic memory allocation is a crucial aspect of memory management, particularly in languages like C and C++.
- It involves requesting and releasing memory as the program runs, allowing for efficient use of resources.
- Memory allocation functions (e.g., `malloc`, `calloc`, `realloc`) are used to request memory from the heap (a region of memory reserved for dynamic allocation).
# 5. Memory Deallocation:

- Memory deallocation is the process of releasing memory that is no longer needed.
- Failure to deallocate memory leads to memory leaks, where allocated memory becomes inaccessible, wasting resources.
- Memory deallocation functions (e.g., `free`) are used to release memory back to the system.
# 6. Memory Fragmentation:

- Memory fragmentation occurs when memory becomes divided into small, non-contiguous chunks.
- Two types of fragmentation:
    - **Internal Fragmentation:** Occurs when memory allocated to a process is larger than what is needed, wasting memory.
    - **External Fragmentation:** Occurs when there are enough total free memory blocks, but they are scattered in a way that makes it impossible to allocate a contiguous block for a specific request.

# 7. Memory Management Units (MMUs):

- Modern computer systems use Memory Management Units to handle memory allocation and access.
- MMUs map virtual memory addresses used by programs to physical memory addresses in RAM.
- They allow multiple programs to share memory and provide memory protection to prevent unauthorized access.

# 8. Garbage Collection:

- Some programming languages, like Java and C#, use automatic memory management through garbage collection.
- Garbage collection automatically reclaims memory that is no longer accessible, reducing the need for manual memory allocation and deallocation.

# 9. Memory Optimization:

- Memory management aims to optimize memory usage by minimizing overhead and maximizing the efficient use of memory resources.
- Techniques like memory pooling, caching, and optimizing data structures play a role in memory optimization.



# 10. Memory Mapping:

- Memory mapping, often done with the `mmap` function, allows a process to map files or devices into its address space, treating them as if they were memory.
- Memory mapping is useful for efficiently reading and writing large files, as well as for inter-process communication.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    // Create or open a file for memory mapping
    int fd = open("mapped_file.txt", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    // Determine the file's size
    struct stat file_stat;
    if (fstat(fd, &file_stat) == -1) {
        perror("fstat");
        close(fd);
        exit(1);
    }

    // Size of the mapped region (in this example, we map the entire file)
    off_t file_size = file_stat.st_size;

    // Create a memory mapping
    void *mapped_data = mmap(NULL, file_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped_data == MAP_FAILED) {
        perror("mmap");
        close(fd);
        exit(1);
    }

    // Close the file descriptor since it's no longer needed for mapping
    close(fd);

    // Now, you can work with the memory-mapped file as if it were an array
    char *file_content = (char *)mapped_data;

    // Modify the content
    strcpy(file_content, "Hello, Memory Mapping!");

    // Synchronize the changes back to the file
    if (msync(mapped_data, file_size, MS_SYNC) == -1) {
        perror("msync");
        munmap(mapped_data, file_size);
        exit(1);
    }

    // Unmap the memory
    if (munmap(mapped_data, file_size) == -1) {
        perror("munmap");
        exit(1);
    }

    return 0;
}
```

In this example:

1. We create or open a file named "mapped_file.txt" for memory mapping.
2. We determine the size of the file using `fstat`.
3. We use `mmap` to map the entire file into memory, allowing us to work with the content of the file as if it were an array.
4. After mapping, we can read and modify the content as needed.
5. We use `msync` to synchronize the changes back to the file.
6. Finally, we unmap the memory using `munmap`.



## Useful links 
- [MIT 6.004 L15: The Memory Hierarchy](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
- [MIT 6.004 L16: Cache Issues](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)
