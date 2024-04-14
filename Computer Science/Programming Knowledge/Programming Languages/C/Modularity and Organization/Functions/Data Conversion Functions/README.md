<h1>C Data Conversion Functions</h1>

Data conversion functions in C are used to convert values between different data types. These functions play a crucial role when dealing with input/output operations, user input processing, or when manipulating data in various forms. Here is a description of some common data conversion functions in C:


<table>
  <tr>
    <th>Function</th>
    <th>Purpose</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>atof()</td>
    <td>Converts a string to a floating-point number.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123.45";
    float num = atof(str);
    printf("Converted floating-point number: %f\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>atoi()</td>
    <td>Converts a string to an integer.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123";
    int num = atoi(str);
    printf("Converted integer: %d\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>atol()</td>
    <td>Converts a string to a long integer.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123456789";
    long num = atol(str);
    printf("Converted long integer: %ld\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>ecvt()</td>
    <td>Converts a floating-point number to a string in exponential format.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    double num = 12345.6789;
    char buffer[20];
    ecvt(num, 6, NULL, NULL);
    printf("Converted string: %s\n", buffer);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>fcvt()</td>
    <td>Converts a floating-point number to a string with a specified number of digits after the decimal point.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    double num = 12345.6789;
    char buffer[20];
    fcvt(num, 2, NULL, NULL);
    printf("Converted string: %s\n", buffer);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>gcvt()</td>
    <td>Converts a floating-point number to a string with a specified number of significant digits.</td>
    <td><pre>#include &lt;stdio.h&gt;

int main() {
    float num = 123.45;
    char str[20];
    gcvt(num, 6, str);
    printf("Converted string: %s\n", str);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>itoa()</td>
    <td>Converts an integer to a string.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    int num = 123;
    char str[10];
    itoa(num, str, 10);
    printf("Converted string: %s\n", str);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>ltoa()</td>
    <td>Converts a long integer to a string.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    long num = 123456789;
    char str[20];
    ltoa(num, str, 10);
    printf("Converted string: %s\n", str);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>strtod()</td>
    <td>Converts a string to a double-precision floating-point number.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123.456";
    double num = strtod(str, NULL);
    printf("Converted double: %f\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>strtol()</td>
    <td>Converts a string to a long integer.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123";
    long num = strtol(str, NULL, 10);
    printf("Converted long integer: %ld\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>strtoul()</td>
    <td>Converts a string to an unsigned long integer.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    char str[] = "123";
    unsigned long num = strtoul(str, NULL, 10);
    printf("Converted unsigned long integer: %lu\n", num);
    return 0;
}</pre></td>
  </tr>
  <tr>
    <td>ultoa()</td>
    <td>Converts an unsigned long integer to a string.</td>
    <td><pre>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    unsigned long num = 123456789;
    char str[20];
    ultoa(num, str, 10);
    printf("Converted string: %s\n", str);
    return 0;
}</pre></td>
  </tr>
</table>

</body>