use std::num::ParseIntError;

fn add(a: &str, b: &str) -> Result<i32, ParseIntError> {
    let aint = a.parse::<i32>()?;
    let bint = b.parse::<i32>()?;
    Ok(aint + bint)
}

fn main() {
    println!("Hello, world!");
    println!("{:?}", add("2", "3"));
    println!("{:?}", add("2", "x"));
}
