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
  fmt.Println(l.head.value)
}

func New() *LinkedList {
  return &LinkedList{}
}

func (l *LinkedList) append(n *Node) {
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
