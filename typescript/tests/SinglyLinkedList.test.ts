import SinglyLinkedList from "../SinglyLinkedList";
import { expect, test, describe, mock, spyOn } from "bun:test";

describe("SinglyLinkedList", () => {
  test("should be able to create a new list", () => {
    const list = new SinglyLinkedList();
    expect(list).toBeDefined();
  });

  const list = new SinglyLinkedList();
  test("should be able to append, prepend", () => {
    list.append(1);
    // [1]
    expect(list.head?.value).toBe(1);
    list.prepend(2);
    // [2, 1]
    expect(list.head?.value).toBe(2);
    expect(list.head?.next?.value).toBe(1);
    expect(list.head?.next?.next).toBeUndefined();
    expect(list.length).toBe(2);
    list.append(5);
    list.append(6);
    // [2, 1, 5, 6]
  });

  test("should be abble to insert at", () => {
    console.log(list.print());
    list.insertAt(3, 2);
    // [2, 1, 5, 6]
    console.log(list.print());
    expect(list.head?.next?.next?.value).toBe(3);
  });

//   test("should be able to add a new node to the end of the list", () => {
//     const list = new SinglyLinkedList();
//     list.append(1);
//     list.append(2);
//     list.append(3);
//     expect(list.head?.value).toBe(1);
//     expect(list.head?.next?.value).toBe(2);
//     expect(list.head?.next?.next?.value).toBe(3);
//   });
});
