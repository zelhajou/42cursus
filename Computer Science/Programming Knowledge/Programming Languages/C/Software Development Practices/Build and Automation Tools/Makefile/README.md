  
A Makefile is a build automation tool used to manage the compilation and linking of source code files in a project. It's especially useful for C projects, where you have multiple source files that need to be compiled and linked together to create an executable program.**Key Concepts in a Makefile:**

1. **Targets:** Targets are the files or actions that you want to create or perform. Common targets include executable programs, object files, and cleanup tasks like "clean."
    
2. **Dependencies:** Dependencies are files or other targets that the current target depends on. If any dependency is modified, the target is rebuilt.
    
3. **Rules:** Rules define how to build a target. They specify the dependencies for a target and the command(s) to create or update it.
```Makefile
target: dependencies
    commands
```
    
4. **Commands:** Commands are shell commands that are executed to build a target. They are indented with a tab character.
    
5. **Variables:** Variables are used to store values like compiler settings, flags, and file names. They can be referenced throughout the Makefile.
	   
6. **Phony Targets:** Some targets don't represent files but are used to trigger specific actions. For example, "clean" is a common phony target used to delete generated files like object files or executables:
```Makefile
clean:
    rm -f myprogram *.o

.PHONY: clean
- means the word "clean" doesn't represent a file name in this Makefile;
- means the Makefile has nothing to do with a file called "clean" in the same directory.

```
	
7. **Automatic Variables:** Make provides a set of automatic variables that you can use in rules and commands to reference common values like the target name, dependencies, or source files. Examples include `$@` (the target), `$<` (the first dependency), and `$^` (all dependencies).
	
8. **Pattern Rules:** Instead of writing a rule for each source file individually, you can use pattern rules to specify a generic rule for building multiple files with a similar pattern. For example:
```
%.o: %.c
    $(CC) $(CFLAGS) -c $<
```
This rule builds object files from corresponding C source files.
	
9. **Include Statements:** You can use the `include` directive to include other Makefiles or configuration files. This is helpful for modularizing complex projects.
    
10. **Conditional Statements:** Makefiles can include conditional statements to handle platform-specific settings or build configurations. For instance, you can use `ifeq` and `endif` to conditionally set variables or rules based on certain conditions.
    
11. **Implicit Rules:** Make provides implicit rules for common tasks like compiling C source files into object files. You can use these rules without explicitly defining them in your Makefile.
    
12. **Special Targets:** Makefiles can define special targets such as ".PHONY" (to mark phony targets), ".DEFAULT" (the default target if none is specified), and others to customize the build process further.

---

# **Creating and Using a Makefile:**

## **Step 1: Create a Makefile**

**Create a Makefile**: Start by creating a file named `Makefile` (or `makefile`, both are valid) in the root directory of your C project.

## **Step 2: Define Variables**

Define variables in your Makefile to specify the compiler, compiler flags, directories, and libraries you'll use. For example:

```bash
# Compiler and compiler flags
CC := gcc
CFLAGS := -Wall -Wextra -Werror
LDFLAGS := -Iinclude

# Libraries
LIBS := -lft_printf -lm

# Directories
SRC_DIR := src
OBJ_DIR := build
BIN_DIR := bin
INC_DIR := include
LIB_DIR := lib
UTILS_DIR := utils
TEST_DIR := test

# Source files
SRC_FILES := $(wildcard $(SRC_DIR)/*.c)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SRC))

# Executable name
EXECUTABLE := $(BIN_DIR)/push_swap


# Test files
TEST_SRC_FILES := $(wildcard $(TEST_DIR)/*.c)
TEST_EXECUTABLES := $(patsubst $(TEST_DIR)/%.c, $(BIN_DIR)/%, $(TEST_SRC_FILES))
```

>[!note]
> 1. `CC := gcc`: Defines the compiler to be used (GCC).
> 2. `CFLAGS := -Wall -Wextra -Werror`: Compiler flags to enable warnings and treat warnings as errors. 
> 3. `SRCDIR`, `INCDIR`, `BUILDDIR`, `LIBDIR`, `TESTDIR`, `UTILSDIR`: Directory variables for source code, include files, build artifacts, libraries, tests, and utilities.
> 4. `SRC := $(wildcard $(SRCDIR)/*.c)`: Automatically detects source files in the `src/` directory.
> 5. `OBJ := $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SRC))`: Converts source file paths to object file paths in the build directory. 
> 6. `LIBS := -lft_printf -lm`: Define any libraries your project depends on. 
> 7. `EXEC := push_swap`: The name of the executable.

```
# Source files
SRC := $(wildcard $(SRCDIR)/*.c)
OBJ := $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SRC))
```
>[!note]
> 1. `SRC := $(wildcard $(SRCDIR)/*.c)`: This line uses the `wildcard` function to find all the `.c` source files within the `$(SRCDIR)` directory. `$(SRCDIR)` is a variable representing the source code directory in your project structure. For example, if you have `main.c`, `operations.c`, and `solver.c` in your `src/` directory, `SRC` will be set to a list of these source files: `src/main.c src/operations.c src/solver.c`.
> 2. `OBJ := $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SRC))`: This line takes the list of source files stored in `SRC` and generates a list of corresponding object files stored in `OBJ`. Here's a breakdown of how this works:
> - `$(patsubst ...)` is a function that performs pattern substitution.
> - `$(SRCDIR)/%.c` is the pattern to match each source file path. It says that any file ending with `.c` in the `$(SRCDIR)` directory is a match.
> - `$(BUILDDIR)/%.o` is the replacement pattern. It specifies that for each source file found, we want to create an object file in the `$(BUILDDIR)` directory with the same base name but with a `.o` extension.

So, if `SRC` contains `src/main.c src/operations.c src/solver.c`, `OBJ` will be set to `build/main.o build/operations.o build/solver.o`. These object files will be used as dependencies for building the executable in the subsequent rules. This automates the process of compiling each source file into an object file with the appropriate naming and directory structure.

## **Step 3: Define Targets and Rules**

Define your build targets and the rules for building them. Targets typically include the final executable, object files, and any additional targets like tests.

```Makefile

all: $(EXECUTABLE)
test: $(TEST_EXECUTABLES)

# Target: The final executable
$(EXECUTABLE): $(OBJ_FILES)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LIBS)

# Rule: How to compile a .c file into a .o file
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ -c $<

$(BIN_DIR)/%: $(TEST_DIR)/%.c $(OBJ_FILES)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $< $(OBJ_FILES) $(LIBS)

```
>[!note] 
>- `all`: The default target. When you run `make`, it will build the executable defined in `$(EXECUTABLE)`.
>- `$(EXECUTABLE)`: Specifies how to build the executable. It depends on the object files in `$(OBJ_FILES)`.
>- `$(OBJ_DIR)/%.o`: This rule tells Make how to compile individual source files into object files.

### Special characters and symbols

There are several special characters and symbols used to define rules and dependencies. Here's a table of some common symbols and their meanings in Makefiles:

|Symbol|Meaning|
|---|---|
|`$@`|The target of the rule (the left-hand side).|
|`$^`|All the dependencies (the right-hand side).|
|`$<`|The first dependency (the first item on the right).|
|`$?`|All the dependencies that are newer than the target.|
|`$*`|The stem of the target (used in pattern rules).|
|`$(`var`)`|The value of a variable (e.g., `$(CC)` for the C compiler).|
|`$(...)`|Substitution reference (e.g., `$(SRC:.c=.o)` replaces `.c` with `.o` in a list).|
|`:=`|Assignment operator for immediate evaluation.|
|`%`|A wildcard in pattern rules (matches any string).|
|`*`|A wildcard character (e.g., `*.c` matches all `.c` files in a directory).|

## **Step 4: Specify Dependencies**

Ensure that your Makefile specifies dependencies correctly. If `my_program` depends on `main.o` and `util.o`, make sure they are listed as dependencies.

## **Step 5: Build Your Project**

To build your project, open a terminal and navigate to the project's directory containing the Makefile. Use the `make` command followed by the target you want to build. For example, to build `my_program`, run:
```
make my_program
```

## **Step 6: Clean Up**

You can use a clean target to remove generated files like object files and executables:
```
clean:
    rm -f my_program *.o
```

 - `clean`: This target is used to remove generated files like object files and executables.

Run `make clean` to remove these files:
```
make clean
```

## **Step 7: Run Tests (Optional)**

If you have test targets defined, you can use `make` to build and run tests:
```
make my_test
```

## **Step 8: Customizing and Expanding**

You can customize and expand your Makefile to suit your project's specific needs. This includes adding more targets, specifying additional flags, or integrating other build tools.




# Resources :
- [Easy Makfile](https://pulgamecanica.herokuapp.com/posts/makefiles)
- [Make-A-Make: Clear the fog around Makefiles](https://github.com/Nuno-Jesus/Make-A-Make)
