fn main() {
    let mut s = String::from("Hello");
    
    {
        let mut s = s.clone();
        s.push_str(", world");
        println!("{s}");
    }

    println!("{s}");

    takes_ownership(s);

    let x = 5;

    makes_copy(5);

    let mut s1 = String::from("Hello 1");
    let len = calculate_len(&s1);

    println!("length of {s1} is {len}");

    change(&mut s1);

    println!("{s1}");

}

fn change(s: &mut String) {
    s.push_str(", world 2");
}

fn calculate_len(s: &String) -> usize {
    s.len()
}

fn takes_ownership(some_string: String) {
    println!("{some_string}");
}

fn makes_copy(some_integer: i32) {
    println!("{some_integer}");
}