package main

import "fmt"

func main() {
    age := 18
    
    if age >= 18 {
        fmt.Println("You are an adult")
    } else if age >= 13 {
        fmt.Println("You are a teenager")
    } else {
        fmt.Println("You are a child")
    }

	if score := calculateScore(); score > 100 {
		fmt.Println("High score!")
	} else {
		fmt.Println("Keep trying!")
	}
}

// switch

func mainSwitch() {
    day := "Monday"
    
    switch day {
    case "Monday":
        fmt.Println("Start of work week")
    case "Friday":
        fmt.Println("End of work week")
    case "Saturday", "Sunday":
        fmt.Println("Weekend!")
    default:
        fmt.Println("Mid-week")
    }
}