pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}

impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();

        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        if self.list.is_empty() {
            self.average = 0.0;
            return;
        }

        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();

    let n: i32 = args
        .get(1)
        .expect("Please provide a number")
        .parse()
        .expect("Please provide a valid integer");

    let mut average = AveragedCollection {
        list: vec![1, 2, 3],
        average: 0.0,
    };

    average.add(n);

    println!("average is {}", average.average());
}