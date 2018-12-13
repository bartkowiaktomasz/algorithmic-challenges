# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    current = head
    pre_current = head

    while(current is not None and current.data < data):
        pre_current = current
        current = current.next

    if current is head:
        head.prev = node
        node.next = head
        return node
    elif current is None:
        pre_current.next = node
        node.prev = pre_current
        return head
    else:
        pre_current.next = node
        node.next = current
        current.prev = node
        return head
