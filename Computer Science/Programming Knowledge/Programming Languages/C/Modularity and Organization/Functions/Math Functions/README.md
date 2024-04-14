# Math Functions


<table>
  <tr>
    <th>Math Function</th>
    <th>Description</th>
    <th>Code Example</th>
  </tr>
  <tr>
    <td>abs(x)</td>
    <td>Returns the absolute value of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;stdlib.h&gt;<br><br>int main() {<br>    int num = -5;<br>    int result = abs(num);<br>    printf("Absolute value of %d is %d\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>sqrt(x)</td>
    <td>Returns the square root of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = 25.0;<br>    double result = sqrt(num);<br>    printf("Square root of %.2f is %.2f\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>pow(x, y)</td>
    <td>Returns x raised to the power of y.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double base = 2.0;<br>    double exponent = 3.0;<br>    double result = pow(base, exponent);<br>    printf("%.2f raised to the power %.2f is %.2f\\n", base, exponent, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>sin(x), cos(x), tan(x)</td>
    <td>Trigonometric functions: sine, cosine, tangent.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double angle = 45.0;<br>    double sinValue = sin(angle);<br>    double cosValue = cos(angle);<br>    double tanValue = tan(angle);<br><br>    printf("sin(%.2f) = %.2f\\n", angle, sinValue);<br>    printf("cos(%.2f) = %.2f\\n", angle, cosValue);<br>    printf("tan(%.2f) = %.2f\\n", angle, tanValue);<br><br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>log(x)</td>
    <td>Returns the natural logarithm (base e) of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = 10.0;<br>    double result = log(num);<br>    printf("Natural logarithm of %.2f is %.2f\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>ceil(x)</td>
    <td>Returns the smallest integer greater than or equal to x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = 4.2;<br>    double result = ceil(num);<br>    printf("Ceil of %.2f is %.2f\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>floor(x)</td>
    <td>Returns the largest integer less than or equal to x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = 4.8;<br>    double result = floor(num);<br>    printf("Floor of %.2f is %.2f\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>round(x)</td>
    <td>Rounds x to the nearest integer, rounding to the even number in the case of a tie.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = 4.5;<br>    double result = round(num);<br>    printf("Round of %.2f is %.2f\\n", num, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>fmod(x, y)</td>
    <td>Returns the remainder of the division of x by y.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double dividend = 10.5;<br>    double divisor = 3.0;<br>    double result = fmod(dividend, divisor);<br>    printf("Remainder of %.2f divided by %.2f is %.2f\\n", dividend, divisor, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>fabs(x)</td>
    <td>Returns the absolute value of x for floating-point numbers.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double num = -7.2;<br>    double result = fabs(num);<br>    printf("Absolute value of %.2f is %.2f\\n", num

, result);<br>    return 0;<br>}</pre></td>


  <tr>
    <td>acos(x)</td>
    <td>Returns the arccosine of x in radians.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 0.5;<br>    double result = acos(x);<br>    printf("Arccosine of %.2f is %.2f radians\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>asin(x)</td>
    <td>Returns the arcsine of x in radians.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 0.5;<br>    double result = asin(x);<br>    printf("Arcsine of %.2f is %.2f radians\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>atan(x)</td>
    <td>Returns the arctangent of x in radians.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 0.5;<br>    double result = atan(x);<br>    printf("Arctangent of %.2f is %.2f radians\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>cosh(x)</td>
    <td>Returns the hyperbolic cosine of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 1.0;<br>    double result = cosh(x);<br>    printf("Hyperbolic cosine of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>sinh(x)</td>
    <td>Returns the hyperbolic sine of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 1.0;<br>    double result = sinh(x);<br>    printf("Hyperbolic sine of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>tanh(x)</td>
    <td>Returns the hyperbolic tangent of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 0.5;<br>    double result = tanh(x);<br>    printf("Hyperbolic tangent of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>exp(x)</td>
    <td>Returns the exponential function of x (e^x).</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 2.0;<br>    double result = exp(x);<br>    printf("Exponential function of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>log10(x)</td>
    <td>Returns the common logarithm (base 10) of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 100.0;<br>    double result = log10(x);<br>    printf("Common logarithm of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>cbrt(x)</td>
    <td>Returns the cube root of x.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 27.0;<br>    double result = cbrt(x);<br>    printf("Cube root of %.2f is %.2f\\n", x, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>hypot(x, y)</td>
    <td>Returns the square root of the sum of squares of x and y.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 3.0;<br>    double y = 4.0;<br>    double result = hypot(x, y);<br>    printf("Hypotenuse of sides %.2f and %.2f is %.2f\\n", x, y, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>fmin(x, y)</td>
    <td>Returns the smaller of x and y.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 5.0;<br>    double y = 3.0;<br>    double result = fmin(x, y);<br>    printf("The smaller of %.2f and %.2f is %.2f\\n", x, y, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>fmax(x, y)</td>
    <td>Returns the larger of x and y.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 5.0;<br>    double y = 8.0;<br>    double result = fmax(x, y);<br>    printf("The larger of %.2f and %.2f is %.2f\\n", x, y, result);<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>isnan(x)</td>
    <td>Returns true if x is NaN (Not a Number).</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = sqrt(-1.0);<br>    if (isnan(x)) {<br>        printf("%.2f is NaN (Not a Number)\\n", x);<br>    }<br>    return 0;<br>}</pre></td>
  </tr>
  <tr>
    <td>isinf(x)</td>
    <td>Returns true if x is infinity.</td>
    <td><pre>#include &lt;stdio.h&gt;<br>#include &lt;math.h&gt;<br><br>int main() {<br>    double x = 1.0 / 0.0;<br>    if (isinf(x)) {<br>        printf("%.2f is infinity\\n", x);<br>    }<br>    return 0;<br>}</pre></td>
  </tr>
</table>

