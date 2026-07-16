fn main() {
    // scaler type
    let a: i32 = -123;
    let b: u32 = 123;
    let x: f32 = 2.0;
    let bt: bool = true;
    let c: char = 'a';

    // compound type

    // tuple
    let tup: (i32, char, bool, f32, u32) = (-123, 'a', true, 2.0, 123);
    let (a, b, c, d, e) = tup;
    println!("The values are {a}, {b}, {c}, {d}, {e}");
    println!(
        "Access using period(.) {}, {}, {}, {}, {}",
        tup.0, tup.1, tup.2, tup.3, tup.4
    );

    // array
    let a = [1, 2, 3, 4, 5];
    let b: [i32; 3] = [6, 7, 8];
    let c = [3; 5];

    println!("Arrayes are: {:?}, {:?}, {:?}", a, b, c);

    let variable: i32 = 1_224;
    println!("variable is {variable}");

    let a: i32 = 12;
    let b: i16 = a as i16;

    let pi: f64 = 3.14159;
    println!("pi value with 2 decimal {pi:.2}");

    let with_milk: bool = true;
    let with_sugar: bool = true;

    let is_my_type_of_coffee = with_milk && with_sugar;
    println!("is my type of coffee {is_my_type_of_coffee}");
}
