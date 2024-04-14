
<h2>C String Manipulation Functions</h2>

<table>
<tr>
<th>Function</th>
<th>Description</th>
<th>Prototype</th>
</tr>
<tr>
<td>strlen()</td>
<td>Calculate the length of a string</td>
<td><code>size_t strlen(const char *str);</code></td>
</tr>
<tr>
<td>strcpy()</td>
<td>Copy a string</td>
<td><code>char *strcpy(char *dest, const char *src);</code></td>
</tr>
<tr>
<td>strncpy()</td>
<td>Copy a specified number of characters from one string to another</td>
<td><code>char *strncpy(char *dest, const char *src, size_t n);</code></td>
</tr>
<tr>
<td>strcat()</td>
<td>Concatenate two strings</td>
<td><code>char *strcat(char *dest, const char *src);</code></td>
</tr>
<tr>
<td>strncat()</td>
<td>Concatenate a specified number of characters from one string to another</td>
<td><code>char *strncat(char *dest, const char *src, size_t n);</code></td>
</tr>
<tr>
<td>strcmp()</td>
<td>Compare two strings</td>
<td><code>int strcmp(const char *str1, const char *str2);</code></td>
</tr>
<tr>
<td>strncmp()</td>
<td>Compare a specified number of characters of two strings</td>
<td><code>int strncmp(const char *str1, const char *str2, size_t n);</code></td>
</tr>
<tr>
<td>strchr()</td>
<td>Locate the first occurrence of a character in a string</td>
<td><code>char *strchr(const char *str, int c);</code></td>
</tr>
<tr>
<td>strrchr()</td>
<td>Locate the last occurrence of a character in a string</td>
<td><code>char *strrchr(const char *str, int c);</code></td>
</tr>
<tr>
<td>strstr()</td>
<td>Locate a substring in a string</td>
<td><code>char *strstr(const char *haystack, const char *needle);</code></td>
</tr>
<tr>
<td>strtok()</td>
<td>Split a string into tokens</td>
<td><code>char *strtok(char *str, const char *delimiters);</code></td>
</tr>
<tr>
<td>strspn()</td>
<td>Get the length of the initial segment of a string consisting of specified characters</td>
<td><code>size_t strspn(const char *str, const char *accept);</code></td>
</tr>
<tr>
<td>strcspn()</td>
<td>Get the length of the initial segment of a string consisting of characters not in a specified set</td>
<td><code>size_t strcspn(const char *str, const char *reject);</code></td>
</tr>
<tr>
<td>memcpy()</td>
<td>Copy memory block</td>
<td><code>void *memcpy(void *dest, const void *src, size_t n);</code></td>
</tr>
<tr>
<td>memmove()</td>
<td>Move memory block</td>
<td><code>void *memmove(void *dest, const void *src, size_t n);</code></td>
</tr>
<tr>
<td>memset()</td>
<td>Fill memory with a constant byte</td>
<td><code>void *memset(void *dest, int c, size_t n);</code></td>
</tr>
</table>