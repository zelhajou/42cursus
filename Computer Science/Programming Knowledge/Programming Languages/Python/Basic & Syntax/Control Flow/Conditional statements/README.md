# Conditional statements

**Conditional statements** are the way computers can make decisions. Conditional statements always have an **if part, which tells the app what to do when the condition is true**. Conditional statements also usually have an **else part, which tells the app what to do when the condition is false.**

There are the following types of conditional statements in C.

- `If` statement.
- `If-Else` statement.
- `Nested If-else` statement.
- `If-Else If` ladder.
- `Switch` statement.
- Ternary Operator (Conditional Expression):


# If-Else Statement:


```py
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are not yet an adult.")

```

# Switch Statement:

[[Python]]: Python and JavaScript do not have a direct switch statement. You can achieve similar functionality using **if-elif-else** constructs.

# Ternary Operator (Conditional Expression):

[[Python]]:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
```