# Go: The Complete Developer's Guide (Golang)

## Introduction
This is a [course](https://www.udemy.com/course/go-the-complete-developers-guide) from Udemy on Golang. The goal is to code along the lectures to study golang. 

## Golang Overview

### static vs dynamic typed

Golang is a static-type langauge. 

Basic go types: 

| Type    | Example                                          |
| ------- | ------------------------------------------------ |
| bool    | true, false                                      |
| string  | "uwu", fmt.Sprintf("%d-%d-%d", year, month, day) |
| int     | 0, 1, 1 ,2 ,3 ,5, 8, 13, 21, 34                  |
| float64 | 3.1415926                                        |


### Collections

**Array & Slices**

- Array: Fixed length list of objects
- Slice: an array that can grow or shrink, like list() in Python or C#, and ArrayList in Java
    - every element in a slice must be of same type

**Map**



### strong vs weak type

### Paradigm? 

Paradigm in programming means a set of methods to solve problems or complete tasks. 

- Imperative programming: one of the oldest programming paradigm. It features close relation to machine architecture.
    - It works by changing the program state through assignment statement. It performs step by step tasks by changing state. The main focus is on how to achive the goal. This paradigm consist of several statments and after execution of all the reult is sotred. 
    - It's called imperative because as progarmmers we dictate exactly what the computer has to do in a very specic way

- Procedural Programming: a derivation of imperative programming, adding to it the feature of functions (also known as "procedures" or "subroutines")
    - In procedural programming, the user is encouraged to subdivide the program execution into functions, as a way of improving modularity and organization.

Go is a procedural programming language

### how does memory management work? 

### is it compiled or interpreted? 

Is is compiled right? 

## Notes

### A Simple Start

- How do we run the code in a go project? 

Navigate to the command line at the right directory, and type

```shell
go run <file-name>.go
```
Go CLI (Command Line Interface) with some common commands

| command    | action                                                  |
| ---------- | ------------------------------------------------------- |
| go build   | compiles a bunch of go source gold file                 |
| go run     | compiles and execute one or two files                   |
| go fmt     | formats all the code in each file in current directory  |
| go install | compiles and installs a package                         |
| go get     | downloads the raw source code of someone else's package |
| go test    | runs any tests associated with the current project      |

- What does 'package main" mean? 

Package is a collection of common source code files. In this case, a package is similar to a project or a workspace. A package can have a series of .go files. 

    - Types of packages: 

        - Executable: generate a file that can be ran. "main" is the keyword.
        - Reuseable: Code used as helpers. Good place to put reusable logics. Don't name is main. 

    - The name of the package is used to make an executable type of package

- What does "import "fmt" mean? 

The literal meaning is give my package everything in the library "fmt" (format). 

By doing so it would establish a link between packages. 

Go to [golang.org/pkg](kttps://golang.org/pkg) for a list of standard golang standard packages. 

- What's 'func'? 

    - "func" means a function. "func" is the the keyword to declare a function
    - The name after func inticate the name of the function 
    - In the (), it includes a list of arguments to pass the function
    - after the (), clarify the return type. Omit indicates it returns nothing. No need to mention void
    - Within the curly braces, we can define the function body. Calling the function will run the code

```go
func sum (a int, b int) int {
    return a + b
}
```

- How is the main.go file organized? 

    1. ```package main``` package declaration
    2. ```import "fmt"```  import packages that we need
    3. declare functions, tell Golang to do its magic
    ```go 
    func main {
        fmt.Println("Hello World")
    }
    ```

### Deeper Into Go



### Organizing Data With Structs

### Maps

### Interfaces

### Channels and Go Routines 

