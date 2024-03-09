# Go: The Complete Developer's Guide (Golang)

## Introduction
This is a [course](https://www.udemy.com/course/go-the-complete-developers-guide) from Udemy on Golang. The goal is to code along the lectures to study golang. 

## Golang Overview

### static vs dynamic typed

### strong vs weak type

### Paradigm? 

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

