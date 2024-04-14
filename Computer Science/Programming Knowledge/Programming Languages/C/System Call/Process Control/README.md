Process control system calls are used to manage processes in an operating system. These system calls allow you to create, manipulate, and control processes.

# 1. **fork():** Create a new process.

- - **Description:** The `fork()` system call is used to create a new process, known as the child process. The child process is an identical copy of the parent process, with the same code, data, and program counter.
- **Return Value:** In the parent process, it returns the child's process ID (PID), while in the child process, it returns 0. On error, it returns -1.
- **Example (in C):**
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t child_pid = fork();
    if (child_pid == 0) {
        // This code runs in the child process.
        printf("Child process\n");
    } else if (child_pid > 0) {
        // This code runs in the parent process.
        printf("Parent process\n");
    } else {
        perror("Fork failed");
        return 1;
    }
    return 0;
}
```

# 2. **exec():**

- **Description:** The `exec()` system call is used to replace the current process's image with a new program. It loads a new program into the current process's memory space and starts its execution.
- **Parameters:**
    - `path`: The path to the executable file.
    - `arg`: A null-terminated array of pointers to string arguments.
- **Return Value:** Only returns on error. If successful, it doesn't return because the process image is replaced
- **Example (in C):**
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    execl("/bin/ls", "ls", "-l", NULL);
    // The code after execl won't execute if successful.
    perror("execl failed");
    return 1;
}
```


# 3. **exit():**

- **Description:** The `exit()` system call is used to terminate the current process. It can also return an exit status code to the parent process.
- **Parameters:**
    - `status`: An integer exit status code (0 for success, non-zero for failure).
- **Return Value:** Does not return to the calling process.
- **Example (in C):**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Hello from the process\n");
    exit(0);
}
```

# 4. **wait():**

- **Description:** The `wait()` system call is used by a parent process to wait for one of its child processes to terminate. It can also retrieve the exit status of the terminated child process.
- **Parameters:**
    - `status`: A pointer to an integer where the exit status of the child process is stored.
- **Return Value:** Returns the PID of the terminated child process, or -1 on error.
- **Example (in C):**
```c
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t child_pid = fork();
    if (child_pid == 0) {
        // This code runs in the child process.
        printf("Child process\n");
        sleep(2);
    } else if (child_pid > 0) {
        // This code runs in the parent process.
        printf("Parent process waiting for the child...\n");
        int status;
        wait(&status);
        printf("Child process terminated with status: %d\n", WEXITSTATUS(status));
    } else {
        perror("Fork failed");
        return 1;
    }
    return 0;
}
```

## Useful links
 - [Understanding fork() system call for new process creation](https://www.youtube.com/watch?v=PwxTbksJ2fo)
 - [fork() and exec() System Calls](https://www.youtube.com/watch?v=IFEFVXvjiHY)
 - [The fork() function in C](https://www.youtube.com/watch?v=cex9XrZCU14)
