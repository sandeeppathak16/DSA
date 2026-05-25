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

    // we can not have two mutable referece a time 

    {
        let r1 = &mut s1;
    } // r1 goes out of scope here, so we can make a new reference with no problems.

    let r2 = &mut s1;

    // we can not have mutable reference while we have immutable reference
    let r1 = &s1; // no problem
    let r2 = &s1; // no problem
    println!("{r1} and {r2}");
    // Variables r1 and r2 will not be used after this point.

    let r3 = &mut s1; // no problem
    println!("{r3}");

    let reference_to_nothing = dangle();
    println!("{}", first_word(&reference_to_nothing));
    let hello = &reference_to_nothing[0..5];
    println!("{hello}");

}

fn dangle() -> String {
    let s = String::from("Hello world");

    s
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

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}