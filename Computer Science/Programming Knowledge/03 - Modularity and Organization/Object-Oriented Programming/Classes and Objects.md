
# 1. [[C]] (Structures for Object-Like Behavior):

- In C, there are no built-in classes and objects as in object-oriented languages, but you can achieve similar functionality using structures.
- Structures allow you to group different data types together into a single unit.
- You can use structures to create custom data types that resemble objects.
```c
#include <stdio.h>
#include <string.h>

// Define a structure
struct Person {
    char name[50];
    int age;
};

int main() {
    // Create an instance of the structure
    struct Person person1;
    strcpy(person1.name, "John");
    person1.age = 30;

    // Access and manipulate data within the structure
    printf("C: %s is %d years old.\n", person1.name, person1.age);

    return 0;
}
```


# 2. [[Java]] (Object-Oriented Programming):
- Java is an [[Object-Oriented Programming]] language, and it revolves around classes and objects.
- Classes are blueprint templates for creating objects.
- Objects are instances of classes, and they contain both data (attributes) and methods (functions).
```java
// Define a class
class Person {
    String name;
    int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void introduce() {
        System.out.println("Java: My name is " + name + " and I am " + age + " years old.");
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an object of the class
        Person person1 = new Person("John", 30);

        // Call a method on the object
        person1.introduce();
    }
}
```

# 3. [[Python]] (Object-Oriented Programming):
- Python is also an [[Object-Oriented Programming]] language, and it supports classes and objects.
- Classes are used to define objects and their behavior.
- Objects are instances of classes and can have attributes and methods.
```python
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def introduce(self):
        print("Python: My name is", self.name, "and I am", self.age, "years old.")

# Create an object of the class
person1 = Person("John", 30)

# Call a method on the object
person1.introduce()
```

# 4. JavaScript (Object-Based):

- [[JavaScript]] is often described as an object-based language, as it does not have traditional classes like Java and Python but still uses objects extensively.
- Objects can be created directly, and they can have properties and methods.
```javascript
// Define an object
const person1 = {
    name: "John",
    age: 30,
    introduce: function() {
        console.log("JavaScript: My name is " + this.name + " and I am " + this.age + " years old.");
    }
};

// Call a method on the object
person1.introduce();
```

In summary, C uses structures to simulate object-like behavior, while Java, Python, and JavaScript are object-oriented and provide built-in support for defining classes and creating objects. Classes act as blueprints for objects, and objects contain data (attributes) and behavior (methods). These concepts are fundamental in object-oriented programming for creating organized, reusable, and modular code.