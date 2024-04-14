
# Operators

In mathematics and computer programming, an operator is a character that represents a specific mathematical or logical action or process. For instance, "x" is an arithmetic operator that indicates multiplication, while "&&" is a logical operator representing the logical AND function in programming.


## Unary Operators

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>+</td>
<td>Unary plus (used to indicate positive values).</td>
<td>

```c
int x = 5; int y = +x; // y is now 5
```
</td>
</tr>
<tr>
<td>-</td>
<td>Unary minus (negates the value of an expression).</td>
<td><code>int x = 5; int y = -x; // y is now -5</code></td>
</tr>
<tr>
<td>++</td>
<td>Increment (increases the value of a variable by 1).</td>
<td><code>int x = 5; x++; // x is now 6</code></td>
</tr>
<tr>
<td>--</td>
<td>Decrement (decreases the value of a variable by 1).</td>
<td><code>int x = 5; x--; // x is now 4</code></td>
</tr>
<tr>
<td>!</td>
<td>Logical NOT (inverts the truth value of an expression).</td>
<td><code>int x = 0; if (!x) {/* Code inside executes because x is not true */}</code></td>
</tr>
<tr>
<td>&</td>
<td>Address of (returns the memory address of a variable).</td>
<td><code>int x = 5; int* ptr = &x; // ptr holds the address of x</code></td>
</tr>
<tr>
<td>*</td>
<td>Indirection or dereference (accesses the value pointed to by a pointer).</td>
<td><code>int x = 5; int* ptr = &x; int y = *ptr; // y is now 5</code></td>
</tr>
<tr>
<td>~</td>
<td>Bitwise NOT (inverts the bits of an integer).</td>
<td><code>int x = 5; int y = ~x; // y is now -6 (assuming 32-bit integer)</code></td>
</tr>
<tr>
<td>sizeof</td>
<td>Returns the size (in bytes) of a data type or object.</td>
<td><code>int size = sizeof(int); // size is the number of bytes required to store an int</code></td>
</tr>
</table>

## Binary

<h3>Arithmetic Operators</h3>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>+</td>
<td>Addition</td>
<td><pre>int result = 10 + 5;</pre></td>
</tr>
<tr>
<td>-</td>
<td>Subtraction</td>
<td><pre>int result = 10 - 5;</pre></td>
</tr>
<tr>
<td>*</td>
<td>Multiplication</td>
<td><pre>int result = 10 * 5;</pre></td>
</tr>
<tr>
<td>/</td>
<td>Division</td>
<td><pre>int result = 10 / 5;</pre></td>
</tr>
<tr>
<td>%</td>
<td>Modulus (Remainder after division)</td>
<td><pre>int result = 10 % 3;</pre></td>
</tr>
</table>

<h3>Comparison Operators</h3>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>==</td>
<td>Equal to</td>
<td><pre>int result = (x == y);</pre></td>
</tr>
<tr>
<td>!=</td>
<td>Not equal to</td>
<td><pre>int result = (x != y);</pre></td>
</tr>
<tr>
<td>&lt;</td>
<td>Less than</td>
<td><pre>int result = (x &lt; y);</pre></td>
</tr>
<tr>
<td>&gt;</td>
<td>Greater than</td>
<td><pre>int result = (x &gt; y);</pre></td>
</tr>
<tr>
<td>&lt;=</td>
<td>Less than or equal to</td>
<td><pre>int result = (x &lt;= y);</pre></td>
</tr>
<tr>
<td>&gt;=</td>
<td>Greater than or equal to</td>
<td><pre>int result = (x &gt;= y);</pre></td>
</tr>
</table>

<h3>Logical Operators</h3>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>&amp;&amp;</td>
<td>Logical AND</td>
<td><pre>int result = (x &amp;&amp; y);</pre></td>
</tr>
<tr>
<td>||</td>
<td>Logical OR</td>
<td><pre>int result = (x || y);</pre></td>
</tr>
<tr>
<td>!</td>
<td>Logical NOT</td>
<td><pre>int result = !x;</pre></td>
</tr>
</table>

<h3>Assignment Operators</h3>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>=</td>
<td>Assignment</td>
<td><pre>x = 10;</pre></td>
</tr>
<tr>
<td>+=</td>
<td>Addition assignment</td>
<td><pre>x += 5;</pre></td>
</tr>
<tr>
<td>-=</td>
<td>Subtraction assignment</td>
<td><pre>x -= 3;</pre></td>
</tr>
<tr>
<td>*=</td>
<td>Multiplication assignment</td>
<td><pre>x *= 2;</pre></td>
</tr>
<tr>
<td>/=</td>
<td>Division assignment</td>
<td><pre>x /= 4;</pre></td>
</tr>
<tr>
<td>%=</td>
<td>Modulus assignment</td>
<td><pre>x %= 3;</pre></td>
</tr>
</table>

<h3>Bitwise Operators</h3>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>&amp;</td>
<td>Bitwise AND</td>
<td><pre>int result = x &amp; y;</pre></td>
</tr>
<tr>
<td>|</td>
<td>Bitwise OR</td>
<td><pre>int result = x | y;</pre></td>
</tr>
<tr>
<td>^</td>
<td>Bitwise XOR (Exclusive OR)</td>
<td><pre>int result = x ^ y;</pre></td>
</tr>
<tr>
<td>~</td>
<td>Bitwise complement</td>
<td><pre>int result = ~x;</pre></td>
</tr>
<tr>
<td>&lt;&lt;</td>
<td>Left shift</td>
<td><pre>int result = x &lt;&lt; 2;</pre></td>
</tr>
<tr>
<td>&gt;&gt;</td>
<td>Right shift</td>
<td><pre>int result = x &gt;&gt; 1;</pre></td>
</tr>
</table>

<h2>Ternary Conditional Operator</h2>

<table>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>? :</td>
<td>Ternary conditional operator</td>
<td>

```c
int result = (condition) ? value_if_true : value_if_false;
```

</td>
</tr>
</table>
