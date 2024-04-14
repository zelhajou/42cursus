File I/O is a fundamental aspect of working with files on a computer's file system, and it allows you to read data from files, write data to files, and perform various file-related operations.

# 1. **Standard I/O (stdio.h):**

- Standard Input (stdin), Standard Output (stdout), and Standard Error (stderr): These are predefined streams in C that allow you to read input from the keyboard and write output to the screen or another output destination.
- Functions like `printf`, `scanf`, `fprintf`, and `fscanf` are commonly used for standard I/O operations.
```c
#include <stdio.h>

int main() {
    char name[50];
    
    printf("Enter your name: ");
    scanf("%s", name);

    printf("Hello, %s!\n", name);
    
    return 0;
}
```
# 2. **File Descriptors:**

- In Unix-like operating systems, file descriptors are small non-negative integers that represent open files. They are used to interact with files and other I/O resources.
- Standard file descriptors are usually associated with stdin (0), stdout (1), and stderr (2).

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;
    char buffer[] = "Hello, File I/O!\n";

    // Open a file for writing (create if it doesn't exist)
    fd = open("example.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

    // Write data to the file
    write(fd, buffer, sizeof(buffer));

    // Close the file
    close(fd);

    return 0;
}
```

One of the first things a UNIX programmer learns is that every running program starts with three files already opened.

| Descriptive Name | Short name | File Number | Description |
|-|-|-|-|
| Standrad In | stdin| 0 | Input from the keyboard |
| Standard out| stdout | 1 | Output to console |
| Standard Error | stderr| 2 | Error output to the console|


![[Pasted image 20230925130344.png]]

this raises the question of what an open file represents. the value returned by an **open** call is termed a file descriptor and is essentially an index into an any of open files kept by the kernel.

### Abstraction:

![[Pasted image 20230925130415.png]]
File descriptors are an index into a file descriptor table stored by the kernel. The kernel creates a file descriptor in response to an **open** call and associates the file descriptor with some abstraction of an underlying file-like object, be that an actual hardware device, or a file system else entirely. consequently a process's **read** or **write** calls that reference that file descriptor are routed to the correct place by the kernel to ultimately do something

```
In short, the file discriptor is the geteway into the kernel's abstructions of underlying hardware.
```



# 3. **Low-level I/O (open, read, write, close, lseek):**

- Low-level file I/O functions provide more control and flexibility over file operations.
- `open`: Opens a file and returns a file descriptor.
- `read`: Reads data from an open file into a buffer.
- `write`: Writes data from a buffer to an open file.
- `close`: Closes an open file.
- `lseek`: Repositions the file pointer within

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int source_fd, dest_fd;
    char buffer[1024];
    ssize_t bytes_read;

    // Open source file for reading
    source_fd = open("source.txt", O_RDONLY);

    // Open destination file for writing (create if it doesn't exist)
    dest_fd = open("destination.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

    // Read from source and write to destination
    while ((bytes_read = read(source_fd, buffer, sizeof(buffer))) > 0) {
        write(dest_fd, buffer, bytes_read);
    }

    // Close files
    close(source_fd);
    close(dest_fd);

    return 0;
}
```

# 4. **Buffered I/O:**

- Buffered I/O functions (e.g., `fopen`, `fclose`, `fread`, `fwrite`) provide a higher-level interface for file operations.
- These functions use an internal buffer to optimize I/O operations for performance.
- They are typically easier to use than low-level I/O functions.



```c
#include <stdio.h>

int main() {
    FILE *file;
    char buffer[1024];

    // Open a file for reading
    file = fopen("example.txt", "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Read data from the file using buffered I/O
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);

    return 0;
}
```

<table>
  <tr>
    <th>Function</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>FILE *fopen(const char *filename, const char *mode);</td>
    <td>Opens a file for reading or writing</td>
  </tr>
  <tr>
    <td>int fclose(FILE *stream);</td>
    <td>Closes the specified file stream</td>
  </tr>
  <tr>
    <td>int fflush(FILE *stream);</td>
    <td>Flushes the output buffer of a stream</td>
  </tr>
  <tr>
    <td>int setvbuf(FILE *stream, char *buffer, int mode, size_t size);</td>
    <td>Sets the buffering mode and size for the specified stream</td>
  </tr>
  <tr>
    <td>int fprintf(FILE *stream, const char *format, ...);</td>
    <td>Writes formatted data to the specified stream</td>
  </tr>
  <tr>
    <td>int fscanf(FILE *stream, const char *format, ...);</td>
    <td>Reads formatted data from the specified stream</td>
  </tr>
  <tr>
    <td>size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);</td>
    <td>Reads data from a stream into the specified buffer</td>
  </tr>
  <tr>
    <td>size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);</td>
    <td>Writes data from the specified buffer to a stream</td>
  </tr>
</table>


File I/O is essential for tasks such as reading configuration files, parsing data from files, writing log files, and interacting with external data sources. Understanding how to perform these operations efficiently and handle errors is crucial for system programming in C. Additionally, proper file handling is critical for ensuring the integrity and security of data in a system.