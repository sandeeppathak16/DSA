fn main() {
    // if else
    let n = 5;

    if n > 0 {
        println!("Greater than 0");
    } else {
        println!("Less than 0");
    }

    // elif
    if n % 2 == 0 {
        println!("{n} is even number");
    } else if n % 3 == 0 {
        println!("{n} is divisible by 3");
    } else {
        println!("{n} is not even number and also not divisible by 3");
    }

    // loop

    let mut count = 0;
    'count_loop: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");

            if remaining == 9 {
                break;
            }

            if count == 2 {
                break 'count_loop;
            }

            remaining -= 1;
        }
        
        count += 1;
    }

    // while loop
    let mut number = 10;

    while number > 0 {
        println!("number = {number}");

        number -= 1;
    }

    // for loop 

    let elements = [1, 2, 3, 4, 5];
    for ele in elements {
        println!("the value is : {ele}");
    }

    for i in 1..=10 {
        println!("iter value: {i}");
    }
}