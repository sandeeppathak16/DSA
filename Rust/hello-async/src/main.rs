use trpl::{Either, Html, StreamExt};
use std::{thread, time::Duration};

fn main() {
    // let args: Vec<String> = std::env::args().collect();

    // trpl::block_on(async {
    //     let title_fut_1 = page_title(&args[1]);
    //     let title_fut_2 = page_title(&args[2]);

    //     // trpl::block_on(async {
    //     //     let url = &args[1];
    //     //     match page_title(url).await {
    //     //         Some(title) => println!("The title for {url} was {title}"),
    //     //         None => println!("{url} had no title"),
    //     //     }
    //     // });

    //     let (url, maybe_title) =
    //         match trpl::select(title_fut_1, title_fut_2).await {
    //             Either::Left(left) => left,
    //             Either::Right(right) => right,
    //         };

    //     println!("{url} returned first");
    //     match maybe_title {
    //         Some(title) => println!("Its page title was: '{title}'"),
    //         None => println!("It had no title."),
    //     }
    // });

    // trpl::block_on(async {
    //     let handle = trpl::spawn_task(async {
    //         for i in 1..10 {
    //             println!("hi number {i} from the first task!");
    //             trpl::sleep(Duration::from_millis(500)).await;
    //         }
    //     });

    //     for i in 1..5 {
    //         println!("hi number {i} from the second task!");
    //         trpl::sleep(Duration::from_millis(500)).await;
    //     };

    //     handle.await.unwrap();
    // });

    // trpl::block_on(async {
    //     run_two_task().await;
    // });

    // trpl::block_on(async {
    //     sharing_val().await;
    // });
    
    trpl::block_on(async {
        let one_ms = Duration::from_millis(1);

        let a = async {
            println!("'a' started.");
            slow("a", 30);
            trpl::yield_now().await;
            slow("a", 10);
            trpl::yield_now().await;
            slow("a", 20);
            trpl::yield_now().await;
            println!("'a' finished.");
        };

        let b = async {
            println!("'b' started.");
            slow("b", 75);
            trpl::yield_now().await;
            slow("b", 10);
            trpl::yield_now().await;
            slow("b", 15);
            trpl::yield_now().await;
            slow("b", 350);
            trpl::yield_now().await;
            println!("'b' finished.");
        };

        trpl::select(a, b).await;
    });

    trpl::block_on(async {
        let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        let iter = values.iter().map(|n| n * 2);
        let mut stream = trpl::stream_from_iter(iter);

        while let Some(value) = stream.next().await {
            println!("The value was: {value}");
        }
    });

    trpl::block_on(async {
        let slow = async {
            trpl::sleep(Duration::from_secs(5)).await;
            "Finally finished"
        };

        match timeout(slow, Duration::from_secs(2)).await {
            Ok(message) => println!("Succeeded with '{message}'"),
            Err(duration) => {
                println!("Failed after {} seconds", duration.as_secs())
            }
        }
    });
    
}

fn slow(name: &str, ms: u64) {
    thread::sleep(Duration::from_millis(ms));
    println!("'{name}' ran for {ms}ms");
}


async fn sharing_val() {
    // let (tx, mut rx) = trpl::channel();

    // let vals = vec![
    //     String::from("hi"),
    //     String::from("from"),
    //     String::from("the"),
    //     String::from("future"),
    // ];

    // for val in vals {
    //     tx.send(val).unwrap();
    //     trpl::sleep(Duration::from_millis(500)).await;
    // }

    // while let Some(value) = rx.recv().await {
    //     println!("received '{value}'");
    // }

    let (tx, mut rx) = trpl::channel();

    let tx1 = tx.clone();
    let tx1_fut = async move {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("future"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };

    let rx_fut = async {
        while let Some(value) = rx.recv().await {
            println!("received '{value}'");
        }
    };

    let tx_fut = async move {
        let vals = vec![
            String::from("more"),
            String::from("messages"),
            String::from("for"),
            String::from("you"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            trpl::sleep(Duration::from_millis(1500)).await;
        }
    };

    trpl::join!(tx1_fut, tx_fut, rx_fut);
}

async fn run_two_task() {
    let fut1 = async {
        for i in 1..10 {
            println!("hi number {i} from the run_two_task first task!");
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };

    let fut2 = async {
        for i in 1..5 {
            println!("hi number {i} from the run_two_task second task!");
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };

    trpl::join(fut1, fut2).await;
}

async fn page_title(url: &str) -> (&str, Option<String>) {
    let response_text = trpl::get(url).await.text().await;
    let title = Html::parse(&response_text)
        .select_first("title")
        .map(|title| title.inner_html());
    (url, title)
}


async fn timeout<F: Future>(
    future_to_try: F,
    max_time: Duration,
) -> Result<F::Output, Duration> {
    match trpl::select(future_to_try, trpl::sleep(max_time)).await {
        Either::Left(output) => Ok(output),
        Either::Right(_) => Err(max_time),
    }
}