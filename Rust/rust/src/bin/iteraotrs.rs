fn main() {
    let v: Vec<i32> = vec![1, 2, 3];

    let v_iter = v.iter();

    for ele in v_iter {
        println!("value : {ele}");
    }

    let total: i32 = v.iter().sum();

    println!("sum is {total}");

    let v2: Vec<_> = v.iter().map(|x| x + 1).collect();
    println!("after adding 1 to v we get {v2:?}");
}