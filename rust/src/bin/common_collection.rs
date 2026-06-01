use std::collections::HashMap;

fn main() {
    let v = vec![1, 2, 3];

    println!("vector {v:?}");

    // updating vector
    let mut v: Vec<i32> = Vec::new();

    v.push(5);
    v.push(6);

    println!("vector {v:?}");

    // reading vector

    let v = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v[2];

    println!("The third element is {third}");

    let third: Option<&i32> = v.get(2);

    match third {
        Some(third) => println!("The third element is {third}"),
        None => println!("There is no third element"),
    }

    // iterating over vector 
    let v = vec![100, 32, 57];

    for i in &v {
        println!("{i}");
    }

    let mut v = vec![100, 32, 57];

    for i in &mut v {
        *i += 50;
    }

    println!("vector after increase {v:?}");

    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

    // creating string 
    let mut s = String::new(); // empty string
    let data = "initial value";
    let s = data.to_string();

    let a = String::from("Initial value");

    // updaing string 

    let mut s = String::from("foo");
    s.push_str("bar");

    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {s2}");

    let mut s = String::from("lo");
    s.push('l');

    println!("s : {s:?}");

    // concatenation with +

    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2;
    println!("s3 is {s3}");

    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{s1}-{s2}-{s3}");
    println!("s is {s}");

    let hello = String::from("Hola");
    let h = &hello[0..4];
    println!("h: {h}");

    for c in hello.chars() {
        println!("{c}");
    }

    for b in hello.bytes() {
        println!("{b}")
    }

    // creating a hashmap

    let mut socres = HashMap::new();

    socres.insert(String::from("blue"), 10);

    // accessing values in a hash map

    let team_name = String::from("blue");
    let socre = socres.get(&team_name).copied().unwrap_or(0);

    socres.insert(String::from("red"), 50);

    for (key, value) in &socres {
        println!("{key}: {value}");
    }

    // updating the value in hashmap

    socres.insert(String::from("red"), 12);

    println!("{socres:?}");

    // adding the value only if key not present

    socres.entry(String::from("yellow")).or_insert(10);
    socres.entry(String::from("red")).or_insert(10);

    println!("{socres:?}");

    let text = "hello world wonderful world";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }

    println!("{map:?}");
    
}