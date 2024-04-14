# Conditional statements

**Conditional statements** are the way computers can make decisions. Conditional statements always have an **if part, which tells the app what to do when the condition is true**. Conditional statements also usually have an **else part, which tells the app what to do when the condition is false.**

There are the following types of conditional statements in C.

- `If` statement.
- `If-Else` statement.
- `Nested If-else` statement.
- `If-Else If` ladder.
- `Switch` statement.

# If-Else Statement:


```c
#include <stdio.h>

int main() {
    int age = 18;

    if (age >= 18) {
        printf("You are an adult.\n");
    } else {
        printf("You are not yet an adult.\n");
    }

    return 0;
}
```

# Switch Statement:

[[C]]:

```c
int day = 3;
switch (day) {
    case 1:
        printf("Monday\n");
        break;
    case 2:
        printf("Tuesday\n");
        break;
    case 3:
        printf("Wednesday\n");
        break;
    default:
        printf("Unknown day\n");
}

```