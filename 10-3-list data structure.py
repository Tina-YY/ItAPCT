class ListNode:
    next = None
    data = None

    def __init__(self, data=None):
        self.data = data


# key start from 0
def search(head, key):
    pointer = head.next
    for i in range(key):
        if pointer is None:
            print("not enough nodes")
            return None
        pointer = pointer.next

    return pointer


def search_with_element(head, element):
    pointer = head
    while pointer is not None:
        if pointer.data == element:
            return pointer
        pointer = pointer.next

    print("No suited node")
    return None


def delete_first_appear(head, element):
    pointer = head
    while pointer.next is not None:
        if pointer.next.data == element:
            pointer.next = pointer.next.next
            return
        pointer = pointer.next


def delete_all(head, element):
    pointer = head
    while pointer.next is not None:
        if pointer.next.data == element:
            pointer.next = pointer.next.next
            continue
        pointer = pointer.next


def insert(pointer, element):
    new_pointer = ListNode(element)
    new_pointer.next = pointer.next
    pointer.next = new_pointer
    return new_pointer


def show(head):
    pointer = head.next
    data = []
    while pointer is not None:
        data.append(pointer.data)
        pointer = pointer.next
    print(data)


h = ListNode()
p = h
for i in range(10):
    p = insert(p, i)

show(h)
searched = search(h, 3)
print(searched.data)

searched = search(h, 11)
searched = search_with_element(h, 11)

searched = search_with_element(h, 8)
print(searched.data)
insert(searched, 8)
show(h)
delete_all(h, 8)
show(h)
searched = search_with_element(h, 7)
insert(searched, 2)
show(h)
delete_first_appear(h, 2)
show(h)
