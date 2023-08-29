export default class Stack<T> {
  public length: number;
  public tail?: Node<T>;

  constructor() {
    this.length = 0;
    this.tail = undefined;
  }

  push(item: T): void {
    let node = new Node(item)
    if (!this.tail) {
      this.tail = node
    } else {
      node.previous = this.tail
      this.tail = node
    }
    this.length++;
  }
  pop(): T | undefined {
    if (!this.tail) {
      return undefined
    }
    if (this.length === 0) {
      this.tail = undefined
      return
    }
    let tmp = this.tail
    this.tail = this.tail.previous
    this.length--;
    return tmp.value

  }
  peek(): T | undefined {
    if (this.tail) {
      return this.tail.value;
    }
    return undefined;
  }
}

class Node<T> {
  value: T;
  previous?: Node<T>;
  constructor(value: T) {
    this.value = value
  }
}

