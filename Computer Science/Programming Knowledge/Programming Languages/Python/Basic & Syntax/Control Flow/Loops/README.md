# Loops

a loop is a sequence of instructions that is continually repeated until a certain condition is reached. Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.

Entry Controlled:
	``for``
	``while``
Exit Controlled:
	``do-while``

Loops  can also be combined with other control statements such as the **Break statement**, **Continue statement** and  and **Conditional Statements**

# 1. For Loop:

```python
for i in range(5):
    print("Python: Iteration", i)
```

## For Loop with **Break statement**, **Continue statement**:
```py
print("Example 1: Using break statement")
for num in range(1, 11):
    if num == 5:
        print("Breaking the loop at num =", num)
        break
    print("Current num value:", num)

# Example 2: Using continue statement
print("\nExample 2: Using continue statement")
for num in range(1, 11):
    if num == 5:
        print("Skipping the iteration at num =", num)
        continue
    print("Current num value:", num)

```

# 2. While Loop:

```py
int i = 0;
while (i < 5) {
    printf("C: Iteration %d\n", i);
    i++;
}
```


# 3. Do-While Loop 
(Note: C and Java support do-while loops, Python and JavaScript do not have a direct equivalent):

# 4. For Each Loop (Java, Python, JavaScript):

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Python: Number", num)
```
