# Loops

a loop is a sequence of instructions that is continually repeated until a certain condition is reached. Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.

- Entry Controlled:
	``for``
	``while``
- Exit Controlled:
	``do-while``

Loops  can also be combined with other control statements such as the **Break statement**, **Continue statement** and  [goto] statement in C, and [[Conditional Statements]]

# 1. For Loop:

```c
for (int i = 0; i < 5; i++) {
    printf("C: Iteration %d\n", i);
}

```

## For Loop with **Break statement**, Continue statement:
```c
for (int i = 0; i < 5; i++) {
    if (i == 2) {
        printf("C: Skipping iteration %d\n", i);
        continue;
    }
    if (i == 4) {
        printf("C: Exiting loop at iteration %d\n", i);
        break;
    }
    printf("C: Iteration %d\n", i);
}

```

# 2. While Loop:

```c
int i = 0;
while (i < 5) {
    printf("C: Iteration %d\n", i);
    i++;
}
```


# 3. Do-While Loop 
(Note: C and Java support do-while loops, Python and JavaScript do not have a direct equivalent):

C:
```c
int i = 0;
do {
    printf("C: Iteration %d\n", i);
    i++;
} while (i < 5);
```

---

The [goto] statement is rarely used in modern programming languages because it can lead to code that is difficult to understand and maintain. Many programming best practices discourage its use.

### C (Using `goto`):

```c
#include <stdio.h>

int main() {
    int i = 0;
    
    loop_start:
    if (i < 5) {
        printf("C: Iteration %d\n", i);
        i++;
        goto loop_start; // Jump back to the 'loop_start' label.
    }
    
    printf("C: Loop finished.\n");
    
    return 0;
}
```
