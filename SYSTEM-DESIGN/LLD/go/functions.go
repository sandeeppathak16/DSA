package main

import "fmt"

// Basic function
func greet(name string) string {
    return "Hello, " + name + "!"
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("cannot divide by zero")
    }
    return a / b, nil
}

// Named return values
func rectangleProperties(length, width float64) (area, perimeter float64) {
    area = length * width
    perimeter = 2 * (length + width)
    return // "naked" return
}

func main() {
    // Calling a basic function
    message := greet("Alice")
    fmt.Println(message)
    
    // Handling multiple return values
    result, err := divide(10, 2)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }
    
    // Using named return values
    a, p := rectangleProperties(5, 3)
    fmt.Printf("Area: %.2f, Perimeter: %.2f
", a, p)
}