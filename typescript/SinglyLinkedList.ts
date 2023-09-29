class Node<T> {
  public value: T;
  public next?: Node<T> | undefined;

  constructor(value: T, next?: Node<T>) {
    this.value = value;
    this.next = next ? next : undefined;
  }
}

export default class SinglyLinkedList<T> {
  public length: number;
  public head?: Node<T> | undefined;

  constructor() {
    this.length = 0
  }

  prepend(item: T): void {
    let node = new Node(item)
    this.length++;
    if (this.head) {
      node.next = this.head
      this.head = node
      return
    }
    this.head = node
  }

  insertAt(item: T, idx: number): void {
    let new_node = new Node(item);
    let prev_node = this.get_node(idx);
    if (!prev_node) {
      return
    }
    this.length++;
    new_node.next = prev_node.next;
    prev_node.next = new_node;
  }

  append(item: T): void {
    let node = new Node(item)
    this.length++;
    let curr = this.head
    if (curr) {
      while (curr.next) {
        curr = curr.next
      }
      curr.next = node
      return
    }
    this.head = node
  }

  remove(item: T): T | undefined {
    let curr: Node<T> | undefined = this.head
    if (this.length == 0 || !curr) {
      return
    }

    if (curr.value == item){
      let val = curr.value
      this.head = curr.next
      this.length--;
      return val 
    }
    while (curr.next) {
      if (curr.next.value == item) {
        let val = curr.next.value
        curr.next = curr.next.next
        this.length--;
        return val
      }
      curr = curr.next
    }

    return undefined
  }

  get(idx: number): T | undefined {
    return this.get_node(idx)?.value
  }

  get_node(idx: number): Node<T> | undefined {
    let curr = this.head
    if (idx > this.length - 1 || curr == undefined || idx < 0) {
      return undefined
    }
    for (let i = 0; i <= idx; i++) {
      if (i == idx) {
        return curr
      }
      if (!curr.next) {
        return undefined
      }
      curr = curr.next
    }
    return undefined
  }

  removeAt(idx: number): T | undefined {
    if (idx > this.length - 1 ||  idx < 0 || this.length == 0) {
      return 
    }
    if (idx == 0) {
      let val = this.head?.value
      this.head = this.head?.next
      this.length--;
      return val;
    }
    let prev_node = this.get_node(idx - 1)

    if (!prev_node) {
      return
    }
    let target_node = prev_node.next
    if (!target_node) {
      return
    }
    prev_node.next = target_node.next
    this.length--;
    return target_node.value
  }
}
