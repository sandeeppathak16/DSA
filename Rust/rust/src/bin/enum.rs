enum IpaddrKind {
    V4,
    V6,
}


enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}


fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}


fn main() {

    let four = IpaddrKind::V4;
    let six = IpaddrKind::V6;
    let absent_number: Option<i32> = Some(10);
    let number: i32 = 10;

    match absent_number {
        Some(value) => println!("sum of values = {}", value + number),
        None => println!("No value"),
    };

    let coin = Coin::Penny;
    let value = value_in_cents(coin);
    println!("value of coin is {value}");

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    println!("print six {six:?}");
}
