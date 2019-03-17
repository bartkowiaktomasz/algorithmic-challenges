# -*- coding: utf-8 -*-
"""
You’re given the pointer to the head node of a linked list, an integer to add
to the list and the position at which the integer must be inserted. Create a
new node with the given integer, insert this node at the desired position and
return the head node.
"""

import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


# Complete the insertNodeAtPosition function below.
def insertNodeAtPosition(head, data, position):
    i = 0
    current_node = head
    previous_node = head
    while(i < position):
        previous_node = current_node
        current_node = current_node.next
        i += 1
    previous_node.next = SinglyLinkedListNode(data)
    previous_node.next.next = current_node
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')
    fptr.close()
