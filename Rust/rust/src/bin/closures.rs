use std::thread;
use std::time::Duration;


#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}


fn main() {
    let expensive_closer = |num: u32| -> u32 {
        println!("calculating slowly....");
        thread::sleep(Duration::from_secs(2));
        num
    };

    let a = expensive_closer(5);

    let example_closure = |x| x;

    let s = example_closure(String::from("hello"));
    // it will raise error becuase now closure type is set to string 
    // let n = example_closure(5);


    let list = vec![1, 2, 3];
    println!("Before defining closure: {list:?}");

    let only_borrows = || println!("From closure: {list:?}");

    println!("Before calling closure: {list:?}");
    only_borrows();
    println!("After calling closure: {list:?}");

    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {list:?}");

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {list:?}");

        let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!("{list:#?}, sorted in {num_sort_operations} operations");
}
