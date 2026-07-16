struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

//tuple structs
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

// unit like structs
struct AlwaysEqual;

struct Rectangle {
    height: usize,
    width: usize
}

impl Rectangle{
    fn area(&self) -> usize {
        self. width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    fn squar(size: usize) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let user1 = build_user("test@gmail.com".to_string(), "test".to_string());
    println!("username: {}, email: {}", user1.username, user1.email);
    let user2 = User {
        email: String::from("test1@gmail.com"),
        ..user1
    };

    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    let subject = AlwaysEqual;

    let rectangle1 = Rectangle {
        width: 10,
        height: 12
    };

    let squar = Rectangle::squar(9);

    println!("Area of rectangle {}", rectangle1.area());
    println!("Area of squar {}", squar.area());

    if rectangle1.can_hold(&squar) {
        println!("Rectangle can hold squar");
    }
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}