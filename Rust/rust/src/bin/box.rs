use::std::ops::Deref;
use crate::List::{Cons, Nil};
use std::rc::Rc;

enum List {
    Cons(i32, Rc<List>),
    Nil,
}


struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

struct CustomSmartPointer {
    data: String,
}

fn hello(name: &str) {
    println!("Hello {name}");
}

fn main() {
    let b = Box::new(5);
    println!("b = {b}");

    let x = 5;
    let y = &x;
    let z = Box::new(x);
    let a = MyBox::new(5);

    assert_eq!(5, *y);
    assert_eq!(5, x);
    assert_eq!(x, *z);
    assert_eq!(x, *a);

    let name = MyBox::new(String::from("sandeep"));
    hello(&name);

    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    // c.drop();
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created");

    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!("count after creating a = {}", Rc::strong_count(&a));
    let b = Cons(3, Rc::clone(&a));
    println!("count after creating b = {}", Rc::strong_count(&a));
    {
        let c = Cons(4, Rc::clone(&a));
        println!("count after creating c = {}", Rc::strong_count(&a));
    }
    println!("count after c goes out of scope = {}", Rc::strong_count(&a));
}