mod linked_list;

fn main() {
    // create a new ArrayList
    let list = linked_list::LinkedList::new();

    // add some elements
    println!("{:#?}", list);
}
