fn main() {
    let x = increase_five(5);

    println!("value of x: {x}");
}

fn increase_five(x: i32) -> i32 {
    x + 5
}