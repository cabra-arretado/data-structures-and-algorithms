package main

import (
  "fmt"
)

type Node struct {
  value int
  next *Node
}

type LinkedList struct {
  head *Node
  length int
}

func main() {
  l := New()
  l.prepend(1)
  l.append(2)
  l.append(3)
  l.prepend(10)
  l.print()
}

func New() *LinkedList {
  return &LinkedList{}
}

func (l *LinkedList) prepend(value int) {
  newNode := Node{value, nil}
  l.length++
  if l.head == nil {
    l.head = &newNode
    return
  }
  newNode.next = l.head
  l.head = &newNode
}

func (l *LinkedList) append(value int) {
  newNode := Node{value, nil}
  l.length++
  if l.head == nil {
    l.head = &newNode
    return
  }
  curr := l.head
  for curr.next != nil {
    curr = curr.next
  }
  curr.next = &newNode
}

func (l *LinkedList) print() {
  // For debbuging purposes
  curr := l.head
  for curr != nil {
    fmt.Println(curr.value)
    curr = curr.next
  }
  fmt.Println("Length:", l.length)
}
