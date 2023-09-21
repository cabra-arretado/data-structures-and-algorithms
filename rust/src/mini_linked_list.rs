#[derive(Debug)]
pub struct Node<T> {
    pub value: Option<T>,
    pub next: Option<Box<T>>,
}

impl Node<i32> {
    pub fn new(value: u32) -> Node<u32> {
        Node {
            value: Some(value),
            next: None,
        }
    }
}

pub struct MiniLinkedList<T> {
    pub head: Option<Node<T>>,
    pub length: usize,
}

impl MiniLinkedList<u32>{
    pub fn new() -> MiniLinkedList<u32> {
        MiniLinkedList {
            head: None,
            length: 0,
        }
    }
    pub fn append(self, value: u32) -> MiniLinkedList<u32> {
        let node = Node::new(value);
        match self.head {
            Some(Node) => {
                let mut current: &Node<u32>= self.head;
                while current.next != None {
                    current = current.next;
                }
            }
            None => {
                self.head = Some(node);
            
            }
        }
        self.length += 1;
        self
    }
}

#[cfg(test)]  
mod tests {  
    use super::*;
    #[test]
    fn test_new_node() {
        let node = Node::new(1);
        assert_eq!(node.value, Some(1));
        assert_eq!(node.next, None);
    }
}

// impl LinkedList {
//     pub fn new() -> LinkedList {
//         LinkedList {
//             head: None,
//             tail: None,
//             length: 0,
//         }
//     }

//     pub fn append(mut self, value: i32) {
//         let node = Node::new(value);
//         match self.tail {
//             Some(ref mut tail) => {
//                 tail.next = Some(&node);
//             }
//             None => {
//                 self.head = Some(node);
//             }
//         }
//         self.tail = Some(node);
//         self.length += 1;
//     }

// }
