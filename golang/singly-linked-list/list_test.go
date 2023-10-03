package main;

import (
  "testing"
)

func TestAppend(t *testing.T) {
  t.Log("Testing append")
  l := New()
  l.append(1)
  l.append(2)
  l.append(3)
  l.append(4)
  l.append(5)
  if l.length != 5 {
    t.Errorf("Expected length of 5, got %d", l.length)
  }
}
