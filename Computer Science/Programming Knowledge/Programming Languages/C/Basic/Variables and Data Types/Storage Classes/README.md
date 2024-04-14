# Stroage Classes

<table>
<tr>
<th>Storage Class</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>auto</td>
<td>Automatic storage duration. Default for local variables.</td>
<td>

```c
#include<stdio.h>;

void exampleFunction() {
	auto int variable = 10;
	printf("Auto variable: %d\n", variable);
}

int main() {
	exampleFunction();
	return 0;
}
```
</tr>
<tr>
<td>register</td>
<td>Similar to auto, but suggests to the compiler to store the variable in a register for faster access.</td>
<td>

```c
#include<stdio.h>;

void exampleFunction() {
register int variable = 10;
printf("Register variable: %d\n", variable);
}

int main() {
exampleFunction();
return 0;
}
```
</td>
</tr>
<tr>
<td>static</td>
<td>Preserves the value of the variable between function calls and has a file scope if declared outside functions.</td>
<td>

```c
#include<stdio.h>

void exampleFunction() {
static int variable = 10;
printf("Static variable: %d\n", variable);
variable++;
}

int main() {
exampleFunction();
exampleFunction();
return 0;
}
```
</td>
</tr>
<tr>
<td>extern</td>
<td>Declares a variable or function that is defined in another file.</td>
<td>

```c
// File1.c
int globalVariable = 10;

// File2.c
#include &lt;stdio.h&gt;

extern int globalVariable;

int main() {
printf("Extern variable: %d\n", globalVariable);
return 0;
}
```
</td>
</tr>
</table>
