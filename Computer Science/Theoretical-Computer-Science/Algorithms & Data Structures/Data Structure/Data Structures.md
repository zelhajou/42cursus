**What is a Data Structure?** A data structure is a way to organize and store data in a computer's memory or storage system. It defines the relationships between data elements and the operations that can be performed on them.

### Types of Data Structures

1. **Primitive Data Types:** These are the most basic data types provided by programming languages. Examples include integers, floating-point numbers, characters, and booleans. They represent individual values, not collections or structures.

2. **Non-Primitive Data structure**: The non-primitive data structure is divided into two types:
	
	1. **Linear Data Structures:** Data structure in which data elements are arranged sequentially or linearly, where each element is attached to its previous and next adjacent elements, is called a linear data structure.
			
		- **Static data structure:** Static data structure has a fixed memory size. It is easier to access the elements in a static data structure.
			- **[[Arrays]]:** A fixed-size collection of elements with direct access via an index.
		- **Dynamic data structure:** In dynamic data structure, the size is not fixed. It can be randomly updated during the runtime which may be considered efficient concerning the memory (space) complexity of the code.
			- **[[Linked Lists]]:** Elements are connected by pointers or references, allowing for efficient insertions and deletions.
			- **[[Stacks]]:** Follows the Last-In-First-Out (LIFO) principle; elements are added and removed from one end.
			- **Queues:** Follows the First-In-First-Out (FIFO) principle; elements are added at one end and removed from the other.

	2. **Non-linear Data Structures:** These data structures do not organize data elements sequentially, enabling more complex relationships between elements. Common non-linear data structures include:
	    
	    - **Trees:** A hierarchical structure with a root node and child nodes; includes binary trees, binary search trees, and balanced trees.
	    - **Graphs:** A collection of nodes connected by edges; can be directed or undirected and may have cycles.
	    - **Heaps:** Specialized trees used for efficient priority queue operations, with properties like min-heaps and max-heaps.
      
4. **Hash-Based Data Structures:** These data structures use hash functions to map keys to specific locations, allowing for fast retrieval and insertion. Common hash-based data structures include:
    
    - **Hash Tables:** Key-value pairs are stored in an array, and a hash function determines the index for each key.
      
5. **String-Based Data Structures:** These data structures are designed for efficient manipulation and storage of strings and text data. Examples include tries (prefix trees) and suffix trees.
    
6. **Advanced Data Structures:** These are specialized data structures designed for specific use cases, such as:
    
    - **Bloom Filters:** Used to test whether an element is a member of a set with probabilistic answers.
    - **Disjoint-Set Data Structures (Union-Find):** Used for tracking disjoint sets and implementing operations like union and find efficiently.
    - **Spatial Data Structures:** Designed for storing and querying spatial or geographic data, such as quad trees and R-trees.
    - **Self-balancing Trees:** Data structures like AVL trees and Red-Black trees that automatically balance themselves to maintain efficient search times.
      
7. **Composite Data Structures:** These data structures combine multiple basic or advanced data structures to create more complex structures. For example, a graph can be implemented using adjacency lists (lists of lists) or adjacency matrices (2D arrays).
    
8. **Abstract Data Types (ADTs):** ADTs are high-level descriptions of data structures that specify the operations that can be performed on them without specifying the implementation details. Examples include lists, stacks, queues, and sets.

###### **Data structures can also be classified as:**

- **Static data structure:** It is a type of data structure where the size is allocated at the compile time. Therefore, the maximum size is fixed.
- **Dynamic data structure:** It is a type of data structure where the size is allocated at the run time. Therefore, the maximum size is flexible.

### Major Operations

The major or the common operations that can be performed on the data structures are:

- **Searching:** We can search for any element in a data structure.
- **Sorting:** We can sort the elements of a data structure either in an ascending or descending order.
- **Insertion:** We can also insert the new element in a data structure.
- **Updating:** We can also update the element, i.e., we can replace the element with another element.
- **Deletion:** We can also perform the delete operation to remove the element from the data structure.

### Which Data Structure?

A data structure is a way of organizing the data so that it can be used efficiently. Here, we have used the word efficiently, which in terms of both the space and time. For example, a stack is an ADT (Abstract data type) which uses either arrays or linked list data structure for the implementation. Therefore, we conclude that we require some data structure to implement a particular ADT.

An ADT tells **what** is to be done and data structure tells **how** it is to be done. In other words, we can say that ADT gives us the blueprint while data structure provides the implementation part. Now the question arises: how can one get to know which data structure to be used for a particular ADT?.

As the different data structures can be implemented in a particular ADT, but the different implementations are compared for time and space. For example, the Stack ADT can be implemented by both Arrays and linked list. Suppose the array is providing time efficiency while the linked list is providing space efficiency, so the one which is the best suited for the current user's requirements will be selected.

### Advantages of Data structures

**The following are the advantages of a data structure:**

- **Efficiency:** If the choice of a data structure for implementing a particular ADT is proper, it makes the program very efficient in terms of time and space.
- **Reusability:** The data structure provides reusability means that multiple client programs can use the data structure.
- **Abstraction:** The data structure specified by an ADT also provides the level of abstraction. The client cannot see the internal working of the data structure, so it does not have to worry about the implementation part. The client can only see the interface.

### Why should we learn Data Structures?

1. Data Structures and Algorithms are two of the key aspects of Computer Science.
2. Data Structures allow us to organize and store data, whereas Algorithms allow us to process that data meaningfully.
3. Learning Data Structures and Algorithms will help us become better Programmers.
4. We will be able to write code that is more effective and reliable.
5. We will also be able to solve problems more quickly and efficiently.