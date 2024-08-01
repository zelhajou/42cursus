A **Linked List** is another example of a linear data structure used to store a collection of data elements dynamically. Data elements in this data structure are represented by the Nodes, connected using links or pointers. Each node contains two fields, the information field consists of the actual data, and the pointer field consists of the address of the subsequent nodes in the list. The pointer of the last node of the linked list consists of a null pointer, as it points to nothing. Unlike the Arrays, the user can dynamically adjust the size of a Linked List as per the requirements.
![An Introduction to Data Structures](https://static.javatpoint.com/ds/images/ds-introduction4.png)
#  **Basic Components of a Linked List:**

 1. **Node:** A node is the fundamental building block of a linked list. Each node contains two main parts:
    
    - Data: The actual value or payload that the node stores.
    - Next (or Link): A reference (pointer) to the next node in the sequence. In a singly linked list, nodes only have a "next" reference, while in a doubly linked list, nodes have both "next" and "previous" references.
2. **Head:** The head is a reference to the first node in the linked list. It serves as the entry point for accessing the list.
    
3. **Tail:** In a singly linked list, the tail is a reference to the last node. In a doubly linked list, there may also be a reference to the first node, called the "head" or "first."

# **Types of Linked Lists:**

1. **[[Singly Linked List]] (SLL):** In a singly linked list, each node points to the next node in the sequence, and the last node points to null. It allows traversal in only one direction (forward).
    
2. **Doubly Linked List (DLL):** In a doubly linked list, each node has both a "next" reference and a "previous" reference. This bidirectional structure enables traversal in both forward and backward directions.
	
3. **Circular Linked List:** In a circular linked list, the last node points back to the first node, creating a closed loop. This structure is useful in applications where you need to cycle through the list indefinitely.
	
4. **Circular doubly linked list -** Circular doubly linked list is a more complex type of data structure in which a node contains pointers to its previous node as well as the next node. Circular doubly linked list doesn't contain NULL in any of the nodes. The last node of the list contains the address of the first node of the list. The first node of the list also contains the address of the last node in its previous pointer.
#  **Operations on Linked Lists:**

1. **Insertion:** Adding a new node to the list, which involves adjusting the "next" and/or "previous" references of neighboring nodes.
    
2. **Deletion:** Removing a node from the list, which also requires adjusting references to neighboring nodes.
    
3. **Traversal:** Iterating through the list to access and process each element. This is typically done using loops or recursion.
    
4. **Search:** Finding a specific element within the list by traversing it sequentially or using more efficient algorithms like binary search in a sorted linked list.

# **Advantages of Linked Lists:**

1. **Dynamic Size:** Linked lists can grow or shrink dynamically, as memory is allocated or deallocated for nodes as needed.
    
2. **Efficient Insertion and deletion -** Unlike arrays, insertion, and deletion in linked list is easier. Array elements are stored in the consecutive location, whereas the elements in the linked list are stored at a random location. To insert or delete an element in an array, we have to shift the elements for creating the space. Whereas, in linked list, instead of shifting, we just have to update the address of the pointer of the node.
    
3. **Memory Efficiency:** Linked lists use memory efficiently because nodes can be scattered throughout memory, reducing the risk of memory fragmentation.
4. **Implementation -** We can implement both stacks and queues using linked list.

# **Disadvantages of Linked Lists:**

1. **Random Access:** Linked lists do not support efficient random access (i.e., accessing elements by index). To reach a specific element, you must traverse the list from the beginning, which takes O(n) time.
    
2. **Additional Memory Overhead:** Each node in a linked list carries additional memory overhead due to the storage of references, making it less memory-efficient for small data types.
    
3. **Complexity:** Managing pointers and ensuring proper memory allocation and deallocation can lead to more complex code and a higher chance of bugs compared to arrays.
	
4.  **Reverse traversing -** Backtracking or reverse traversing is difficult in a linked list. In a doubly-linked list, it is easier but requires more memory to store the back pointer.

# **Some Applications of Linked Lists:**

1. The Linked Lists help us implement stacks, queues, binary trees, and graphs of predefined size.
2. We can also implement Operating System's function for dynamic memory management.
3. Linked Lists also allow polynomial implementation for mathematical operations.
4. We can use Circular Linked List to implement Operating Systems or application functions that Round Robin execution of tasks.
5. Circular Linked List is also helpful in a Slide Show where a user requires to go back to the first slide after the last slide is presented.
6. Doubly Linked List is utilized to implement forward and backward buttons in a browser to move forward and backward in the opened pages of a website.
7. With the help of a linked list, the polynomials can be represented as well as we can perform the operations on the polynomial.
8. A linked list can be used to represent the sparse matrix.
9. The various operations like student's details, employee's details, or product details can be implemented using the linked list as the linked list uses the structure data type that can hold different data types.
10. Using linked list, we can implement stack, queue, tree, and other various data structures.
11. The graph is a collection of edges and vertices, and the graph can be represented as an adjacency matrix and adjacency list. If we want to represent the graph as an adjacency matrix, then it can be implemented as an array. If we want to represent the graph as an adjacency list, then it can be implemented as a linked list.
12. A linked list can be used to implement dynamic memory allocation. The dynamic memory allocation is the memory allocation done at the run-time.

## Why use linked list over array?

Till now, we were using array data structure to organize the group of elements that are to be stored individually in the memory. However, Array has several advantages and disadvantages which must be known in order to decide the data structure which will be used throughout the program.

Array contains following limitations:

1. The size of array must be known in advance before using it in the program.
2. Increasing size of the array is a time taking process. It is almost impossible to expand the size of the array at run time.
3. All the elements in the array need to be contiguously stored in the memory. Inserting any element in the array needs shifting of all its predecessors.

Linked list is the data structure which can overcome all the limitations of an array. Using linked list is useful because,

1. It allocates the memory dynamically. All the nodes of linked list are non-contiguously stored in the memory and linked together with the help of pointers.
2. Sizing is no longer a problem since we do not need to define its size at the time of declaration. List grows as per the program's demand and limited to the available memory space.
![[Screen Shot 2023-10-08 at 10.58.46 AM.png]]


Linked list is the Linked representation of list and its not a sequential representation of list