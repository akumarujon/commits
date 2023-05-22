use std::process;
use std::fs;

fn main(){

    const NUMBER_OF_COMMITS: i32 = 4000;

    let mut count: i32 = 2000;

    loop {
        count += 1;

        fs::File::create(format!("./files-rs/{}.txt", count.clone()));
        process::Command::new("git").arg("add").arg(format!("./files-rs/{}.txt", count.clone())).spawn().expect("Couldnt add").wait();
        process::Command::new("git").arg("commit").arg("-m").arg(format!("\"{}.txt\"", count.clone())).spawn().expect("Couldnt commit").wait();

        if count==NUMBER_OF_COMMITS{
            process::Command::new("git").arg("push").arg("origin").arg("main").spawn();
            break;
        }
    }

    println!("Done!");
}
