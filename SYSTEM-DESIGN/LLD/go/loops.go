package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}

// while loop type for
func main() {
    sum := 1
    for sum < 10 {
        sum += sum
        fmt.Println(sum)
    }
}

// infinite loop 
for {
    // This will run forever unless broken out of
    if condition {
        break
    }
}


// for range loop
func main() {
    fruits := []string{"apple", "banana", "cherry"}
    
    for index, fruit := range fruits {
        fmt.Printf("Index: %d, Fruit: %s", index, fruit)
    }
}