# Strings

Strings are a fundamental data type used to represent and manipulate text in programming languages. They consist of sequences of characters, such as letters, numbers, symbols, or spaces.

Strings in C are sequences of characters represented as arrays of characters, terminated by a null character ('\0') **When the compiler finds a sequence of characters enclosed within the double quotation marks, it adds a null character (\0) at the end by default.**.
C does not have a built-in string data type like some other programming languages, such as C++ or Python. Instead, C treats strings as character arrays.

### 1. **String Declaration and Initialization**:

In C, you can declare and initialize strings in several ways:

**Example**
```c
char str1[] = "Hello, World!"; // Automatically computes the size of the array
char str2[15] = "Hello, World!"; // Explicitly specify the size of the array
char str2[15] = "Hello, World!"; // Explicitly specify the size of the array
```

A <ins>string literal</ins> is a sequence of zero or more multibyte characters enclosed in double-quotes, as in "abc". String literals are not modifiable (and are placed in read-only memory). Any attempt to alter their values results in undefined 
behavior.

```c
char *str = "Zelhajou"
```
### 2. **String Functions**:
C provides several string manipulation functions declared in the `string.h` library. Here are some commonly used ones:

#### a. `strlen` - String Length:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    int length = strlen(str);
    printf("Length of the string: %d\n", length);
    return 0;
}
```

#### b. `strcpy` - String Copy:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello";
    char destination[10];
    strcpy(destination, source);
    printf("Destination: %s\n", destination);
    return 0;
}
```
#### c. `strcat` - String Concatenation:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello, ";
    char str2[] = "World!";
    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);
    return 0;
}
```

#### d. `strcmp` - String Comparison:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";
    int result = strcmp(str1, str2);
    
    if (result < 0) {
        printf("str1 comes before str2\n");
    } else if (result > 0) {
        printf("str1 comes after str2\n");
    } else {
        printf("str1 and str2 are equal\n");
    }
    
    return 0;
}
```

### 3. **String Input and Output**:

#### a. String Input using `scanf`:
```c
#include <stdio.h>

int main() {
    char name[50];
    printf("Enter your name: ");
    scanf("%s", name); // Reads a single word
    printf("Hello, %s!\n", name);
    return 0;
}
```

#### b. String Input using `fgets`:
```c
#include <stdio.h>

int main() {
    char name[50];
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin); // Reads a line, including spaces
    printf("Hello, %s!\n", name);
    return 0;
}
```

#### c. String Output using `printf`:
```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    printf("%s\n", str);
    return 0;
}
```

### 4. **String Manipulation and Access**:
#### a. Accessing Individual Characters:

You can access individual characters in a string using array indexing.

```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    char firstChar = str[0]; // Access the first character
    printf("First character: %c\n", firstChar);
    return 0;
}
```

#### b. Modifying Individual Characters:

You can modify individual characters in a string as well.
```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    str[7] = 'C'; // Change 'W' to 'C'
    printf("%s\n", str);
    return 0;
}
```





### 5. **Dynamic Strings**:

You can also work with dynamically allocated strings using `malloc` and other memory management functions. Here's an example of dynamically allocating a string:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char *dynamicStr = (char *)malloc(20 * sizeof(char));
    if (dynamicStr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    strcpy(dynamicStr, "Dynamic String");
    printf("%s\n", dynamicStr);

    free(dynamicStr); // Don't forget to free allocated memory
    return 0;
}
```

### 6. Strings and Pointers :

As we have seen, strings in C are represented by character arrays which act as pointers. Hence, we can use pointers to manipulate or even perform operations on the string.

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
	char str[] = "Scaler.";
	printf("%c", *str);     // Output: S
	printf("%c", *(str + 1)); // Output: c
	printf("%c\n", *(str + 6)); // Output: .

	char *stringPtr;
	stringPtr = str;
	printf("%c", *stringPtr);     // Output: S
	printf("%c", *(stringPtr + 1)); // Output: c
	printf("%c", *(stringPtr + 6)); // Output: .

	printf("str = %d %d %d ", sizeof(str), sizeof(str[0]), sizeof(str)/sizeof(str[0]));
	return 0;
}
```

## 7. **String and Memory Functions**

**Header file**

- `string.h` contains the function prototypes and any other definitions that are needed

**Memory Functions :**

String handling functions, as we have seen, deal only with string-data. Then what about the processing of **Non-String data,**

for example, an array of floats, an array of structures, an array of pointers, etc.. Further, it’s not uncommon for non-string data to contain’0′ (NULL) characters. ANSI C library provides a related set of functions called memory functions for handling such needs.

```c
void *memcpy(void *dst, const void *src, size_t lenbytes);
void *memmove(void *dst, const void *src, size_t lenbytes);
void *memcmp(void const *dst, const void *src, size_t lenbytes);
void *memchr(void const *a, int ch, size_t lenbytes);
void *memset(void *a, int ch, size_t lenbytes);
```

Notice the type of arguments ‘void *’ in function prototypes which means pointers-to-any_type can be passed to pointers of type ‘void *’.

**In addition. unlike strn— functions, memory functions don’t stop when they encounter the first NULL character**