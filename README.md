

<!--
![Frame 1 (2)](https://github.com/user-attachments/assets/1d01f499-41e3-40c8-8bf7-709f48db0c01)
-->
## Hey! 👋

This is where I keep all my coding projects from my time at [42](https://42.fr/en/homepage/). I'm studying at [1337](https://1337.ma/en/) (part of the [42](https://42.fr/en/homepage/) Network) and I'm learning everything from scratch - starting with C programming and working my way up to building entire web apps.

What makes 42 different is there are no teachers and no lectures. Instead, you figure things out on your own, work on real projects, and learn alongside other students. Every project has to go through peer reviews (we call them "corrections") before you can move forward. It's intense, but it's a great way to learn how to code and solve problems.

In this repo, you'll find my progress through the whole curriculum - from basic stuff like coding my own C library to more complex projects like building web servers and creating full-stack applications. Each project taught me something new about computer science and software development.

## Table of Contents
<!--
- 🏫 [About 42](#about-42)
-->
- 📚 [Curriculum](#curriculum)
- 🚀 [Projects](#projects)
    - [Core Programming Fundamentals](#core-programming-fundamentals)
    - [Unix & System Programming](#unix--system-programming)
    - [Algorithms & Data Structures](#algorithms--data-structures)
    - [Computer Graphics](#computer-graphics)
    - [Network Programming](#network-programming)
    - [Object-Oriented Programming](#object-oriented-programming)
    - [DevOps & Cloud](#devops--cloud)
    - [Full-Stack Development](#full-stack-development)
- 🛠️ [Skills](#skills)
- 📊 [Stats](#stats)
- 📝 [Blogs and Articles](#blogs-and-articles)
- 📚 [Bookshelf](#bookshelf)
- 📞 [Contact](#contact)
<!--
- 📓 [Study Notes](#study-notes)
-->

<!--
## About 42

42 is a global education initiative that offers a new way of learning technology:
no teachers, no classrooms, students learning from their fellow students (peer-to-peer learning), with a methodology that develops both computing and life skills. The 42cursus is free for whoever is approved in its selection process* - the so-called "Piscine" - becoming thus "cadets" (42's students).

For further information about 42's **selection process** (the "Piscine"), please visit the [C Piscine repo](https://github.com/zelhajou/42-piscine_c).
-->
## Curriculum

The 42 curriculum is structured like a galaxy of projects, organized in concentric circles from basic to advanced:

**Inner Circle (Common Core)**
- Begins with fundamental C programming
- Projects increase in complexity as you progress
- At certain points, you can choose between different projects:
    - For example, between graphics projects (FdF/fract-ol) or Unix projects (minitalk/pipex)
    - Some levels offer multiple project options, where you only need to complete one to progress
- All mandatory phases must be completed to finish the common core
-Required for activities like internships and student exchange

**Outer Treks**
- A collection of diverse project trails available after the inner circle
- Covers various specialization areas:

    - Operating Systems
    - Web Development
    - Graphics
    - Network & System Administration
    - And more...

These tracks allow students to specialize in their preferred areas of software development and computer science.


<!--
<details>

<summary><ins><b>Click to expand the 42 Holy Graph</b></ins></summary>

</details>
-->
![42 Holy Graph](https://github.com/user-attachments/assets/ccabd3a7-bd07-4e37-ad30-b8fdeb8a363c)


Note: The Holy Graph visualization above maps the complete curriculum structure. The turquoise nodes indicate completed projects, while grey nodes represent projects yet to be tackled. Each connection line shows the prerequisites needed to unlock the next project, with some levels offering multiple paths to choose from.

## Projects

The following table lists the projects I've completed as part of the 42 Cursus. Each project is linked to its repository, where you can find the project's description, requirements, and my implementation.



### Core Programming Fundamentals
<table>
<tr>
<td colspan="2">
<div align="center">

#### Foundation Phase
<img src="https://img.shields.io/badge/Language-C-00599C?style=flat&logo=c"/>
<img src="https://img.shields.io/badge/Environment-UNIX-FCC624?style=flat&logo=linux"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-libft">
<strong>libft</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-122%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Create a custom C library implementing standard functions and additional utilities</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Memory functions (malloc, free, memset, memcpy)</li>
<li>String operations (strlen, strcpy, strcat, split)</li>
<li>List management (linked list creation and manipulation)</li>
<li>Character utilities (isalpha, isdigit, toupper, tolower)</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/Makefile-A42E2B?logo=gnu&logoColor=white"/>
<img src="https://img.shields.io/badge/GDB-green?logo=gnu&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Low-level memory management</li>
<li>Data structure implementation</li>
<li>Pointer manipulation</li>
<li>Code modularization</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-ft_printf">
<strong>ft_printf</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Recreate the printf function with core format specifiers and various flags</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Format specifiers (%c, %s, %p, %d, %i, %u, %x, %X)</li>
<li>Flag handling (width, precision, alignment)</li>
<li>Buffer management for efficient string handling</li>
<li>Error detection and input validation</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/Format_String_Parsing-555555?style=flat"/>
<img src="https://img.shields.io/badge/Type_Handling-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Variadic functions implementation</li>
<li>String formatting algorithms</li>
<li>Type conversion techniques</li>
<li>Memory optimization strategies</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-get_next_line">
<strong>get_next_line</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-125%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Develop a function that reads lines from file descriptors</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>File descriptor handling and management</li>
<li>Static variable utilization</li>
<li>Buffer management and optimization</li>
<li>Memory leak prevention</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/File_I%2FO-555555?style=flat"/>
<img src="https://img.shields.io/badge/Memory_Management-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>File operations and I/O handling</li>
<li>Memory management techniques</li>
<li>Static variable usage</li>
<li>Buffer optimization strategies</li>
</ul>
</td>
</tr>

</table>



### Unix & System Programming
<table>
<tr>
<td colspan="2">
<div align="center">

#### System Administration & Process Management
<img src="https://img.shields.io/badge/System-Administration-FCC624?style=flat&logo=linux"/>
<img src="https://img.shields.io/badge/Process-Management-00ADD8?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-Born2beRoot">
<strong>Born2beroot</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-108%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Set up and configure a secure Linux server with strict rules</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>System administration and security setup</li>
<li>User and group management</li>
<li>Service configuration (SSH, UFW, sudo)</li>
<li>System monitoring script development</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=white"/>
<img src="https://img.shields.io/badge/VirtualBox-183A61?logo=virtualbox&logoColor=white"/>
<img src="https://img.shields.io/badge/Bash-4EAA25?logo=gnu-bash&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Linux system administration</li>
<li>Security policy implementation</li>
<li>Service management</li>
<li>System monitoring and maintenance</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-minitalk">
<strong>Minitalk</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Create a client-server communication system using UNIX signals</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Signal handling (SIGUSR1, SIGUSR2)</li>
<li>Bit manipulation for data transfer</li>
<li>Client-server architecture</li>
<li>Error handling and recovery</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/UNIX-FCC624?logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/Signal_Processing-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Inter-process communication</li>
<li>Signal handling mechanisms</li>
<li>Binary data transmission</li>
<li>Process synchronization</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-Philosophers">
<strong>Philosophers</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Solve the dining philosophers problem using threads and mutexes</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Thread creation and management</li>
<li>Mutex implementation for resource control</li>
<li>Deadlock prevention strategies</li>
<li>Performance optimization</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/Thread_Management-555555?style=flat"/>
<img src="https://img.shields.io/badge/Mutex_Operations-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Concurrent programming concepts</li>
<li>Thread synchronization techniques</li>
<li>Resource sharing management</li>
<li>Race condition prevention</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-minishell">
<strong>Minishell</strong>
</a><br>
<img src="https://img.shields.io/badge/Team-2_Members-orange"/>
<img src="https://img.shields.io/badge/Score-101%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Create a basic shell interpreter similar to bash</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Command parsing and lexical analysis</li>
<li>Process creation and management</li>
<li>Built-in command implementation</li>
<li>Signal handling and environment management</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/Parser_Development-555555?style=flat"/>
<img src="https://img.shields.io/badge/Process_Management-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Shell program architecture</li>
<li>Process control and execution</li>
<li>Environment variable handling</li>
<li>Collaborative development</li>
</ul>
</td>
</tr>

</table>



### Algorithms & Data Structures
<table>
<tr>
<td colspan="2">
<div align="center">

#### Algorithm Implementation & Optimization
<img src="https://img.shields.io/badge/Focus-Algorithms-FF6B6B?style=flat"/>
<img src="https://img.shields.io/badge/Focus-Data_Structures-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-push_swap">
<strong>Push_swap</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-125%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Develop an efficient sorting algorithm using two stacks with limited operations</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Custom sorting algorithm development</li>
<li>Stack data structure management</li>
<li>Operation sequence optimization</li>
<li>Algorithm complexity analysis</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/Algorithm_Design-555555?style=flat"/>
<img src="https://img.shields.io/badge/Data_Structures-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Algorithm optimization techniques</li>
<li>Stack operations and manipulation</li>
<li>Time complexity analysis</li>
<li>Problem-solving methodologies</li>
</ul>
</td>
</tr>

</table>



### Computer Graphics
<table>
<tr>
<td colspan="2">
<div align="center">

#### Graphics Programming & Visualization
<img src="https://img.shields.io/badge/Focus-Graphics-FF6B6B?style=flat"/>
<img src="https://img.shields.io/badge/Focus-Visualization-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-fractol">
<strong>Fract-ol</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Create a graphical program to explore and render various fractals</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Fractal rendering algorithms (Mandelbrot, Julia)</li>
<li>User input and event handling</li>
<li>Color mapping and gradients</li>
<li>Zoom and navigation features</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/MinilibX-Graphics-FF6B6B"/>
<img src="https://img.shields.io/badge/Math-Complex_Numbers-green"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Graphics programming fundamentals</li>
<li>Complex number mathematics</li>
<li>Event-driven programming</li>
<li>Optimization techniques</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-cub3D">
<strong>Cub3D</strong>
</a><br>
<img src="https://img.shields.io/badge/Team-2_Members-orange"/>
<img src="https://img.shields.io/badge/Score-115%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Develop a 3D game engine using raycasting techniques</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Raycasting algorithm implementation</li>
<li>Map parsing and validation</li>
<li>Texture mapping and rendering</li>
<li>Player movement and collision detection</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C-00599C?logo=c&logoColor=white"/>
<img src="https://img.shields.io/badge/MinilibX-Graphics-FF6B6B"/>
<img src="https://img.shields.io/badge/Mathematics-Linear_Algebra-green"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>3D graphics fundamentals</li>
<li>Linear algebra application</li>
<li>Game physics basics</li>
<li>Team collaboration</li>
</ul>
</td>
</tr>

</table>


### Network Programming
<table>
<tr>
<td colspan="2">
<div align="center">

#### Network & Protocol Implementation
<img src="https://img.shields.io/badge/Focus-Networking-0089D6?style=flat"/>
<img src="https://img.shields.io/badge/Focus-Protocols-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42-net_practice">
<strong>NetPractice</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Master network configuration and TCP/IP fundamentals</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>IP addressing and subnetting</li>
<li>Network topology design</li>
<li>Routing configuration</li>
<li>Network troubleshooting</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/Networking-0089D6?logo=cisco"/>
<img src="https://img.shields.io/badge/TCP%2FIP-555555?style=flat"/>
<img src="https://img.shields.io/badge/Network_Design-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Network architecture principles</li>
<li>IP addressing schemes</li>
<li>Subnet calculation</li>
<li>Network diagnostics</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-webserv">
<strong>Webserv</strong>
</a><br>
<img src="https://img.shields.io/badge/Team-3_Members-orange"/>
<img src="https://img.shields.io/badge/Score-125%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Build an HTTP/1.1 compliant web server from scratch</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>HTTP protocol implementation</li>
<li>Socket programming and I/O multiplexing</li>
<li>Request/Response handling</li>
<li>CGI execution and configuration</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/HTTP-Protocol-orange"/>
<img src="https://img.shields.io/badge/Socket-Programming-blue"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Web server architecture</li>
<li>HTTP protocol internals</li>
<li>Non-blocking I/O</li>
<li>Team collaboration</li>
</ul>
</td>
</tr>

</table>



### Object-Oriented Programming
<table>
<tr>
<td colspan="2">
<div align="center">

#### Modern C++ Development
<img src="https://img.shields.io/badge/Focus-Modern_C++-00599C?style=flat&logo=cplusplus"/>
<img src="https://img.shields.io/badge/Focus-OOP-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-cpp-modules">
<strong>CPP Modules<br>(00-04)</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Master fundamental C++ concepts and OOP principles</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Classes and objects implementation</li>
<li>Inheritance and polymorphism</li>
<li>Memory management in C++</li>
<li>Operator overloading</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/OOP-Design-orange"/>
<img src="https://img.shields.io/badge/Memory_Management-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Object-oriented design principles</li>
<li>Class implementation techniques</li>
<li>C++ memory management</li>
<li>SOLID principles</li>
</ul>
</td>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-cpp-modules">
<strong>CPP Modules<br>(05-09)</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Status-In_Progress-blue"/>
</div>
</td>
<td><strong>Objective</strong>: Advanced C++ concepts and Standard Template Library utilization</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Template programming</li>
<li>STL containers and algorithms</li>
<li>Exception handling</li>
<li>Design patterns</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/STL-Library-orange"/>
<img src="https://img.shields.io/badge/Template_Programming-555555?style=flat"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Advanced template techniques</li>
<li>STL container usage</li>
<li>Error handling strategies</li>
<li>Generic programming concepts</li>
</ul>
</td>
</tr>

</table>


### DevOps & Cloud
<table>
<tr>
<td colspan="2">
<div align="center">

#### Container Orchestration & Deployment
<img src="https://img.shields.io/badge/Focus-Containerization-2496ED?style=flat&logo=docker"/>
<img src="https://img.shields.io/badge/Focus-Service_Management-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-inception">
<strong>Inception</strong>
</a><br>
<img src="https://img.shields.io/badge/Solo-Project-blue"/>
<img src="https://img.shields.io/badge/Score-100%2F100-success"/>
</div>
</td>
<td><strong>Objective</strong>: Set up a complete containerized web infrastructure using Docker</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Multi-container application setup</li>
<li>Docker network and volume configuration</li>
<li>Service orchestration (NGINX, WordPress, MariaDB)</li>
<li>Custom Docker image creation</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white"/>
<img src="https://img.shields.io/badge/MariaDB-003545?logo=mariadb&logoColor=white"/>
<img src="https://img.shields.io/badge/WordPress-21759B?logo=wordpress&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Container orchestration</li>
<li>Service configuration management</li>
<li>Network security implementation</li>
<li>Infrastructure as Code principles</li>
</ul>
</td>
</tr>

</table>



### Full-Stack Development
<table>
<tr>
<td colspan="2">
<div align="center">

#### Web Development & Real-Time Applications
<img src="https://img.shields.io/badge/Focus-Web_Development-3178C6?style=flat&logo=typescript"/>
<img src="https://img.shields.io/badge/Focus-Real_Time-4CAF50?style=flat"/>
</div>
</td>
</tr>

<tr>
<th width="200px">Project</th>
<th width="1200px">Details</th>
</tr>

<tr>
<td rowspan="4">
<div align="center">
<a href="https://github.com/zelhajou/42cursus-ft_transcendence">
<strong>ft_transcendence</strong>
</a><br>
<img src="https://img.shields.io/badge/Team-Project-orange"/>
<img src="https://img.shields.io/badge/Status-In_Progress-blue"/>
</div>
</td>
<td><strong>Objective</strong>: Create a full-stack web application featuring real-time multiplayer game and social features</td>
</tr>
<tr>
<td><strong>Implementation</strong>:
<ul>
<li>Single-page application development</li>
<li>Real-time game and chat system</li>
<li>OAuth 2.0 authentication</li>
<li>RESTful API design</li>
<li>Tournament and matchmaking system</li>
</ul>
</td>
</tr>
<tr>
<td><strong>Technical Stack</strong>:<br>
<img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/Django-0C4B33?logo=django&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>Key Learnings</strong>:
<ul>
<li>Full-stack application architecture</li>
<li>Real-time communication protocols</li>
<li>User authentication and security</li>
<li>Database design and management</li>
</ul>
</td>
</tr>

</table>

### Achievement Summary
<div align="center">

#### Project Statistics
<img src="https://img.shields.io/badge/13-Completed_Projects-success"/>
<img src="https://img.shields.io/badge/2-In_Progress-blue"/>
<img src="https://img.shields.io/badge/4-Team_Projects-orange"/>
<img src="https://img.shields.io/badge/106%2F100-Average_Score-success"/>

#### Exam Achievements
<img src="https://img.shields.io/badge/Exam%2002-100%2F100-success"/>
<img src="https://img.shields.io/badge/Exam%2003-100%2F100-success"/>
<img src="https://img.shields.io/badge/Exam%2004-100%2F100-success"/>
<img src="https://img.shields.io/badge/Exam%2005-100%2F100-success"/>
</div>




## Skills


### 🔧 Programming & Development
- **Languages:** C, C++, Bash, HTML/CSS, JavaScript
- **Core Skills:** Memory management, data structures, algorithms, OOP
- **Tools:** Git, Make, Docker, GDB, Valgrind
- **Environments:** VSCode, Vim, Emacs, Linux, macOS

### 💻 System & Network
- **System Programming:** Process management, IPC, threading, memory optimization
- **Network:** Socket programming, HTTP/TCP/IP, web server development
- **Security:** System hardening, SSH, firewall configuration, authentication

### 🎮 Graphics & Mathematics
- **Graphics:** Raycasting, 3D rendering, game physics, collision detection
- **Mathematical:** Fractal computation, complex number operations, optimization

### 🐳 DevOps & Web
- **Containerization:** Docker, service configuration, container orchestration
- **Web Development:** Full-stack applications, REST APIs, WebSockets
- **Databases:** PostgreSQL, MariaDB, data modeling

### 🛠️ Professional Practice
- **Development:** Code review, documentation, debugging, testing
- **Collaboration:** Team projects, pair programming, project management
- **Problem Solving:** Algorithm design, optimization, architectural planning

[![My Skills](https://skillicons.dev/icons?i=c,cpp,linux,ubuntu,apple,bash,git,vscode,vim,emacs,md,latex,docker,github,figma,html,css,javascript,nginx)](https://skillicons.dev)







<!--
### 🔧 Fundamental C Programming ([Libft](https://github.com/zelhajou/42cursus-libft))

<pre>
├── Memory Management
│   ├── malloc/free implementation
│   ├── memory copy and set operations
│   └── memory block manipulation
├── String Operations
│   ├── string manipulation (strdup, strjoin, strtrim)
│   ├── string comparison functions
│   ├── character classification
│   └── string conversion (atoi, itoa)
└── Data Structures
    ├── linked list implementation
    ├── node manipulation
    └── list traversal algorithms
</pre>

### 📝 Input/Output Management
<pre>
├── Printf Implementation (<a href="https://github.com/zelhajou/42cursus-ft_printf">ft_printf</a>)
│   ├── variadic functions usage
│   ├── format specifier parsing
│   ├── type conversion handling
│   └── buffer management
├── File Operations (<a href="https://github.com/zelhajou/42cursus-get_next_line">get_next_line</a>)
│   ├── file descriptor handling
│   ├── static variable usage
│   ├── buffer reading strategies
│   └── memory leak prevention
└── Standard I/O
    ├── input parsing
    ├── output formatting
    └── error handling
</pre>

### 💻 System Administration ([Born2beroot](https://github.com/zelhajou/42cursus-Born2beRoot))
<pre>
├── Virtualization
│   ├── Virtual Machine setup
│   ├── Debian system installation
│   └── system resource management
├── System Security
│   ├── password policy implementation
│   ├── user/group management
│   └── sudo configuration
└── Service Management
    ├── SSH server configuration
    ├── UFW firewall setup
    └── system monitoring (cron)
</pre>

### 🧮 Algorithm Implementation
<pre>
├── Stack Operations (<a href="https://github.com/zelhajou/42cursus-push_swap">Push_swap</a>)
│   ├── stack data structure
│   ├── sorting algorithms
│   ├── operation optimization
│   └── complexity analysis
└── Mathematical Visualization (<a href="https://github.com/zelhajou/42cursus-fract-ol">Fract-ol</a>)
    ├── fractal mathematics
    ├── complex number operations
    ├── zoom handling
    └── color mapping
</pre>


### ⚡ Process & Thread Management
<pre>
├── Signal Handling (<a href="https://github.com/zelhajou/42-minitalk">Minitalk</a>)
│   ├── UNIX signals
│   ├── bit manipulation
│   └── process communication
├── Thread Synchronization (Philosophers)
│   ├── mutex implementation
│   ├── deadlock prevention
│   ├── resource sharing
│   └── dining philosophers algorithm
└── Process Control (<a href="https://github.com/zelhajou/42cursus-minishell">Minishell</a>)
    ├── process creation (fork)
    ├── process execution (execve)
    ├── pipe implementation
    └── signal handling
</pre>

### 🌐 Networking
<pre>
├── Network Configuration (<a href="https://github.com/zelhajou/42cursus-net_practice">NetPractice</a>)
│   ├── IP addressing
│   ├── subnet masks
│   ├── routing tables
│   └── network troubleshooting
└── Web Server Implementation (<a href="https://github.com/zelhajou/42cursus-webserv">Webserv</a>)
    ├── socket programming
    ├── HTTP protocol
    ├── request handling
    └── response generation
</pre>

### 🎮 Graphics Programming ([Cub3D](https://github.com/zelhajou/42cursus-cub3D))
<pre>
├── Raycasting Engine
│   ├── ray calculation
│   ├── wall rendering
│   └── texture mapping
├── Game Development
│   ├── player movement
│   ├── collision detection
│   └── map parsing
└── Graphics Optimization
    ├── frame rate management
    ├── rendering efficiency
    └── memory usage optimization
</pre>


### 🔵 Object-Oriented Programming (CPP Modules)
<pre>
├── Basic Concepts (<a href="https://github.com/zelhajou/42cursus-cpp-modules">00-04</a>)   
│   ├── class implementation
│   ├── encapsulation
│   ├── inheritance
│   └── polymorphism
├── Advanced Features (<a href="https://github.com/zelhajou/42cursus-cpp-modules">05-09</a>)
│   ├── templates
│   ├── exception handling
│   └── operator overloading
└── Standard Template Library
    ├── containers
    ├── algorithms
    └── iterators
</pre>
  
### 🐳 Containerization ([Inception](https://github.com/zelhajou/42cursus-inception))
<pre>
├── Docker
│   ├── container creation
│   ├── image building
│   └── volume management
├── Service Configuration
│   ├── nginx setup
│   ├── WordPress configuration
│   └── MariaDB management
└── Network Architecture
    ├── container networking
    ├── port mapping
    └── service discovery
</pre>

### 🌐 Full-Stack Development ([ft_transcendence](https://github.com/zelhajou/42cursus-ft_transcendence))
<pre>
├── Frontend Development
│   ├── single-page application
│   ├── real-time game interface
│   └── responsive design
├── Backend Architecture
│   ├── microservices design
│   ├── REST API development
│   └── WebSocket implementation
├── Database Management
│   ├── PostgreSQL
│   ├── data modeling
│   └── query optimization
└── DevOps & Security
    ├── Docker containerization
    ├── SSL/HTTPS configuration
    ├── authentication & authorization
    └── monitoring & logging
</pre>

### 🛠️ Development Tools & Practices
<pre>
├── Build System
│   ├── Makefile creation
│   └── compilation flags
├── Debugging
│   ├── GDB usage
│   ├── Valgrind for memory checking
│   └── error tracking
└── Version Control
    ├── Git fundamentals
    ├── repository management
    └── collaborative workflow
</pre>

### 📊 Project Planning & Management
<pre>
├── Time Management
│   ├── project scheduling
│   └── deadline adherence
│   └── resource allocation
├── Documentation
│   ├── code documentation
│   └── README creation
└── Team Collaboration
    ├── pair programming (<a href="https://github.com/zelhajou/42cursus-minishell">Minishell</a>, <a href="https://github.com/zelhajou/42cursus-cub3D">Cub3D</a>, <a href="https://github.com/zelhajou/42cursus-webserv">Webserv</a>)
    ├── code review
    └── project coordination
</pre>

-->



<!--
![13v6seyveh661](https://github.com/user-attachments/assets/943fff17-50fb-4a74-b6cd-8c369319dc0c)
-->




## Stats

**42 Stats**

<div align="center">

[![zelhajou's 42 stats](https://badge.mediaplus.ma/binary/zelhajou)](https://github.com/oakoudad/badge42)

</div>

**GitHub Stats**

<div align="center">

| <img src="https://github-readme-stats.vercel.app/api?username=zelhajou&show_icons=true&count_private=true&hide_border=true&&theme=transparent" align="center" style="width: 100%" /> | <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=zelhajou&layout=compact&hide_border=true&theme=transparent" align="center" style="width: 100%" /> |
|:-:|:-:|

</div>

## Blogs and Articles

These are some of the blogs and articles I've written about my experiences at 42 and other topics related to computer science and programming.

- [Building the 42-School Minitalk Project: A Guide to UNIX Signal-Based Communication in C](https://medium.com/@aaaikrz/building-the-42-school-minitalk-project-a-guide-to-unix-signal-based-communication-in-c-d11605643747)


## [Bookshelf](https://github.com/zelhajou/1337-Bookshelf)

These are some of the books I've read or plan to read to deepen my knowledge in computer science, programming, and other subjects.

| **Name**| **Description**| **Category** | **Image** |
| --------- | --------- | --------- | --------- |
|  The Linux Programming Interface-Michael Kerrisk       | A comprehensive guide to system programming on the Linux platform by Michael Kerrisk. Covers system calls, libraries, and more. |  Computer System-level Programming | <img src="https://github.com/zelhajou/42-cursus/assets/39954629/e8ceb45e-9c83-47f0-a5f1-41cd01c0d642" width="200"> |
| Advanced Programming in the Linux Environment | Explores advanced topics in Linux programming, offering insights into system calls, libraries, and techniques for efficient software development. |  Computer System-level Programming |  <img src="https://github.com/zelhajou/42-cursus/assets/39954629/08f28684-3f19-46fa-a284-ce64141b1bd5" width="200"> |
| Operating System Concepts | A classic textbook on operating system principles and concepts, providing a foundational understanding of OS design and functionality. |  Computer System-level Programming |  <img src="https://github.com/zelhajou/42-cursus/assets/39954629/98c74ba3-665e-481d-828e-a492ec516fa3" width="200">  |
| Networking Essentials - A CompTIA Network+ N10-008 Textbook | Provides comprehensive coverage of essential networking concepts and technologies required for CompTIA Network+ certification exam N10-008. Authored by Jeffrey S. Beasley and Piyasat Nilkaew, this textbook offers detailed explanations and practical examples to help readers understand networking fundamentals.| Computer Networking | <img src="https://github.com/zelhajou/42-cursus/assets/39954629/54e56797-b95e-490e-ac31-9a7f2d818f9e" width="200">  |
| Computer Networks - A Tanenbaum - 5th edition | A comprehensive textbook on computer networking, authored by Andrew S. Tanenbaum, covering a wide range of networking topics including protocols, architectures, and applications. | Computer Networking | <img src="https://github.com/zelhajou/42-cursus/assets/39954629/6141d72a-e655-429d-84f8-c0bd06f42709" width="200">  |
| UNIX Network Programming Volume 1, Third Edition: The Sockets Networking API | A classic reference on UNIX network programming, authored by W. Richard Stevens, offering in-depth coverage of the Sockets API and various networking concepts on UNIX-based systems | Computer System-level Programming | <img src="https://github.com/zelhajou/42-cursus/assets/39954629/9e14fd69-a5c7-46cb-9042-e1cb6a401f44" width="200"> |


<!--
## Study Notes

These are some of the study notes and cheat sheets I've created to help me learn and remember key concepts in computer science, programming, and other subjects.

- Text editors and version control ([Emacs](https://github.com/zelhajou/42-cursus/blob/main/Computer%20Science/Computer%20Systems/Distributed%20Systems/Operating%20Systems/Linux/Text%20Editors/Emacs.md), [Vim](https://github.com/zelhajou/42-cursus/blob/main/Computer%20Science/Computer%20Systems/Distributed%20Systems/Operating%20Systems/Linux/Text%20Editors/VIM.md),  [Git](https://github.com/zelhajou/42-cursus/blob/main/Computer%20Science/Computer%20Systems/Distributed%20Systems/Operating%20Systems/Linux/Git.md))
-  Programming languages ([C](https://github.com/zelhajou/42cursus-piscine-c/tree/main/C%20Cheat%20Sheet), [C++](https://github.com/zelhajou/42cursus-cpp-modules/tree/main/C%2B%2B%20Cheat%20Sheet))
- Frontend web development ([HTML](https://github.com/zelhajou/42-cursus/tree/main/Software%20Engineering/Web%20Development/Frontend/Fundamentals/HTML), [CSS](https://github.com/zelhajou/42-cursus/tree/main/Software%20Engineering/Web%20Development/Frontend/Fundamentals/CSS))

-->

## Contact

Feel free to reach out to me if you have any questions, suggestions, or just want to chat!

<a href="mailto:zelhajou@gmail.com">
    <img align="left" alt="Gmail" width="18px" src="https://cdn.simpleicons.org/gmail/000/fff" />
</a>
<a href="https://www.linkedin.com/in/zelhajou/">
    <img align="left" alt="Linkedin" width="18px" src="https://cdn.simpleicons.org/linkedin/000/fff" />
</a>
<a href="https://twitter.com/zelhajou">
    <img align="left" alt="Twitter" width="18px" src="https://cdn.simpleicons.org/x/000/fff" />
</a>
<a href="https://discord.com/users/aaaikrz">
    <img align="left" alt="Discord" width="18px" src="https://cdn.simpleicons.org/discord/000/fff" />
</a>
<a href="https://t.me/aaaikrz">
    <img align="left" alt="Telegram" width="18px" src="https://cdn.simpleicons.org/telegram/000/fff" />
</a>
<a href="https://www.instagram.com/aaaikrz/">
    <img align="left" alt="Instagram" width="18px" src="https://cdn.simpleicons.org/instagram/000/fff" />
</a>

<br>
<br>
<br>

<div align="center">


![8rtdcmuc8jk51](https://github.com/user-attachments/assets/6d614260-90e0-43b1-afb7-97f8e8f9f247)

<!--
> Forrest Gump ghir tanjri 9ariban arrivederci 🏃
-->

</div>
