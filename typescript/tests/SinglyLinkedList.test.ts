import SinglyLinkedList from "../SinglyLinkedList";
import { expect, test, describe, mock, spyOn } from "bun:test";

describe("SinglyLinkedList", () => {

  test("test instantiation", () => {
    const list = new SinglyLinkedList();
    expect(list).toBeDefined();
  });

  const list = new SinglyLinkedList();

  test("test append, prepend", () => {
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

  test("test get, get_node, insert_at", () => {
    // [2, 1, 5, 6]
    expect(list.get_node(2)?.value).toBe(5);
    expect(list.get(2)).toBe(5);
    list.insertAt(2, 3);
    // [2, 1, 3, 5, 6]
    expect(list.length).toBe(5);
    expect(list.get_node(2)?.value).toBe(3);
  });

  test("test remove, remove_at", () => {
    // [2, 1, 3, 5, 6]
    expect(list.remove(3)).toBe(3);
    // [2, 1, 5, 6]
    expect(list.length).toBe(4);
    expect(list.remove_at(2)).toBe(5);
    // [2, 1, 6]
    expect(list.length).toBe(3);
  });
  test("test print", () => {
    // [2, 1, 6]
    expect(list.print()).toBe("[2, 1, 6]");
  }
  );

});
