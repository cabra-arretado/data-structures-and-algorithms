#[derive(Debug)]
struct Node {
    value: i32,
    next: Option<&Node>,
}

impl Node {
    pub fn new(value: i32) -> Node {
        Node { value, next: None }
    }
}

#[derive(Debug)]
pub struct LinkedList {
    pub head: Option<Node>,
    pub tail: Option<Node>,
    pub length: usize,
}

impl LinkedList {
    pub fn new() -> LinkedList {
        LinkedList {
            head: None,
            tail: None,
            length: 0,
        }
    }

    pub fn append(mut self, value: i32) {
        let node = Node::new(value);
        match self.tail {
            Some(ref mut tail) => {
                tail.next = Some(&node);
            }
            None => {
                self.head = Some(node);
            }
        }
        self.tail = Some(node);
        self.length += 1;
    }

}