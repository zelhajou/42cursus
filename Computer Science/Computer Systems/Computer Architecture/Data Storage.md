Recall that the most basic unit of memory, the bit, has two possible states, **“on” or “off”**. If we used one bit to store a number, we could use each different state to represent a different number. For example, a bit could be used to represent the numbers 0, when the bit is off, and 1, when the bit is on.

We will need to store numbers much larger than 1; to do that we need more bits.

## **Numbers :**

If we use two bits together to store a number, each bit has two possible states, so there are four possible combined states:

- both bits off,
- first bit off and second bit on,
- first bit on and second bit off,
- or both bits on.

The settings for a series of bits are typically written using a 0 for off and a 1 for on. For example, the four possible states for two bits are 00, 01, 10, 11. This representation is called **binary** notation.

### **Integers**

Integers are commonly stored using a word of memory, which is 4 bytes or 32 bits, so integers from 0 up to 4,294,967,295

in the decimal system we are used to using 10 symbols or values : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

we use the symbols to write numbers

|100s|10s|1s|
|---|---|---|
|5|2|7|

in binary we just have two symbols or values, `o` and `1`. this means that in binary number system each column heading is twice as big as the previous one as we move from right to left.

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|1|0|0|1|1|1|

how convert : 32 + 4 + 2 +1 = 39

100111 = 39.

- Convert the decimal number 142 into binary

is 128 smaller than 142 ?

yes it we re record 1 in the first column from left-hand side.

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|1||||||||

142 - 128 = 14

we subtract 128 from 142, to leave a remainder of 14.

we now check 14 against the next column value

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|1|0|0|0|1||||

14 - 8 = 6

……

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|1|0|0|0|1|1|1|0|

## **Characters :**

Text is stored on a computer by first converting each character to an integer and then storing the integer.

Example : to store the letter ‘A’, we will actually store the number 65; ‘B’ is 66 …

A letter is usually stored using a single byte (8 bits ) Each letter is assigned an integer number and that number is stored

The conversion of letters to numbers is called an encoding. the encoding used in the examples above is called **[ASCII](https://www.ascii-code.com/)**

![[Untitled 2.png]]
## **Overflow errors**

If we are working with 8-bit numbers and all we can store is 8 bits, the following problem might occur.For example, if we add these two 8-bit numbers:

For example, if we add these two 8-bit numbers:

![[Untitled (1).png]]
The carried 1 in the left-hand column would be the ninth digit in our answer, but we are limited to 8 bits. This carry is lost, which means we have an overflow error.

In this example, we tried to add 11000110 (198 in decimal) and 11100011 (227 in decimal).198 + 227 = 425 in decimal. The answer produces an overflow error because we needed a 9th bit. Without a 9th bit that information is lost, giving an incorrect answer of 10101001 in binary, which is 169 in decimal.

The largest value we can store in 8 bits is 11111111, or 255 in decimal. So the reason for the overflow error is that 425 is too large a number to store in 8 bits.

[7.4 Computer Memory](https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node55.html)

## The problem with overflow :

If you have an unsigned int number at 255, and you increment it, you’ll get 256 in return. As expected. If you have an unsigned char number at 255, and you increment it, you’ll get 0 in return. It resets starting from the initial possible value.

If you have an unsigned char number at 255 and you add 10 to it, you’ll get the number 9:

**Library Functions :**

C has many in-built functions which can make our work easier and code readable. Inbuilt functions are already defined in C and could be directly used in the program. These functions are grouped in a library, which can be accessed by including those header files in our program.