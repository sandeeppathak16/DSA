// Variable Declaration

// Method 1: Declaration with explicit type
var name string = "John"

// Method 2: Type inference (Go figures out the type)
var age = 25

// Method 3: Short declaration (only inside functions)
salary := 50000.50

// Multiple declarations
var (
    city    string = "New York"
    country string = "USA"
)

// Basic Data Types


// Numeric types
var integer int = 42
var float float64 = 3.14159
var complex complex128 = 3 + 4i

// Boolean type
var isActive bool = true

// String type
var message string = "Hello, Go!"

// Byte (alias for uint8)
var b byte = 'A'

// Rune (alias for int32, represents a Unicode code point)
var r rune = '😀'


// Constant

const Pi = 3.14159
const (
    StatusOK       = 200
    StatusNotFound = 404
)
