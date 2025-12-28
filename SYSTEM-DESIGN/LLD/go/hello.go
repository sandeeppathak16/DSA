// Every Go program starts with a package declaration. The main package is special
// it tells Go that this is an executable program, not a library.
package main

// This imports the format package (fmt) from the standard library, which provides formatting and printing functions.
import "fmt"

// The main function is the entry point of the program. When you run a Go program, execution starts in the main function.
func main () {
	// Declare with explicit type
	var name string = "John"
    
    // Type inference (Go determines the type)
    var age = 25
    
    // Short declaration (only inside functions)
    salary := 50000.50
    
    fmt.Println("Name:", name)
    fmt.Println("Age:", age)
    fmt.Println("Salary:", salary)
}