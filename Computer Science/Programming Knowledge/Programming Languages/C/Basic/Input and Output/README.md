# Input and Output

Input and output (I/O) operations are essential aspects of programming, allowing you to interact with users, read from or write to files, and communicate with external devices or networks.


- **Standard I/O Library:** C provides a standard I/O library, including functions like `printf` for output and `scanf` for input. These functions are commonly used for console I/O.
    
- **File I/O:** C supports file input and output operations through functions like `fopen`, `fclose`, `fread`, `fwrite`, `fgets`, and `fputs`. These functions allow you to read from and write to files.
    
- **Formatted I/O:** C provides powerful formatted I/O capabilities using functions like `printf` and `scanf`, which allow you to specify the format of data being read or written.
    
- **Error Handling:** C's I/O functions often return error codes or set the global variable `errno` in case of errors. You can check for errors using conditional statements.

```c
#include <stdio.h>

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("You entered: %d\n", number);
    return 0;
}
```


<h2>C Escape Sequences</h2>

<table>
  <tr>
    <th>Escape Sequence</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>\n</td>
    <td>Newline character</td>
  </tr>
  <tr>
    <td>\t</td>
    <td>Tab character</td>
  </tr>
  <tr>
    <td>\r</td>
    <td>Carriage return</td>
  </tr>
  <tr>
    <td>\\</td>
    <td>Backslash character</td>
  </tr>
  <tr>
    <td>\'</td>
    <td>Single quote</td>
  </tr>
  <tr>
    <td>\"</td>
    <td>Double quote</td>
  </tr>
  <tr>
    <td>\?</td>
    <td>Question mark</td>
  </tr>
  <tr>
    <td>\a</td>
    <td>Alert (bell) character</td>
  </tr>
  <tr>
    <td>\b</td>
    <td>Backspace character</td>
  </tr>
  <tr>
    <td>\f</td>
    <td>Form feed</td>
  </tr>
  <tr>
    <td>\v</td>
    <td>Vertical tab</td>
  </tr>
  <tr>
    <td>\0</td>
    <td>Null character (ASCII 0)</td>
  </tr>
</table>

<h2>C Format Specifiers</h2>

<table>
  <tr>
    <th>Format Specifier</th>
    <th>Data Type</th>
  </tr>
  <tr>
    <td>%d</td>
    <td>int</td>
  </tr>
  <tr>
    <td>%ld</td>
    <td>long</td>
  </tr>
  <tr>
    <td>%lld</td>
    <td>long long</td>
  </tr>
  <tr>
    <td>%u</td>
    <td>unsigned int</td>
  </tr>
  <tr>
    <td>%lu</td>
    <td>unsigned long</td>
  </tr>
  <tr>
    <td>%llu</td>
    <td>unsigned long long</td>
  </tr>
  <tr>
    <td>%f</td>
    <td>float</td>
  </tr>
  <tr>
    <td>%lf</td>
    <td>double</td>
  </tr>
  <tr>
    <td>%e, %E</td>
    <td>Scientific notation</td>
  </tr>
  <tr>
    <td>%c</td>
    <td>char</td>
  </tr>
  <tr>
    <td>%s</td>
    <td>String</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>Pointer</td>
  </tr>
  <tr>
    <td>%x, %X</td>
    <td>Hexadecimal</td>
  </tr>
  <tr>
    <td>%o</td>
    <td>Octal</td>
  </tr>
  <tr>
    <td>%g, %G</td>
    <td>Compact format for float/double</td>
  </tr>
  <tr>
    <td>%%</td>
    <td>Literal % character</td>
  </tr>
</table>