// import the array_list module
mod array_list;

fn main() {
    // create a new ArrayList
    let list = array_list::ArrayList::<usize>::new();
    // add some elements
    println!("{:#?}", list);
}
