  
System calls are a crucial part of the interaction between user-level programs and the operating system (OS). They provide an interface for user programs to request services from the OS, such as file operations, process management, network communication, and more.

# **1. What are System Calls?**

System calls are functions or routines that allow user-level processes (applications) to communicate with the kernel (core part) of the operating system. When a program needs to perform privileged operations or interact with hardware, it uses system calls as an interface to request the OS to perform these tasks on its behalf.

# **2. Purpose of System Calls:**

- **Abstraction:** System calls provide an abstraction layer between user-level programs and the underlying hardware and kernel.
- **Security:** They ensure that user programs do not have direct access to privileged instructions or hardware, preventing unauthorized actions.
- **Isolation:** System calls maintain process isolation, preventing one process from interfering with or accessing the memory or resources of another process.

# **3. Types of System Calls:**

- ## 1. [[Process Control]] (fork, exec, exit, wait)
- ## 2. **[[File Management]]** (open, read, write, close, seek, unlink)
- ## 3. **[[Memory Management]]** (malloc, calloc, realloc, free)
