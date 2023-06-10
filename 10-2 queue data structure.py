class Queue:
    data = None
    head = None
    tail = None
    queue_size = None

    def __init__(self, queue_size=5):
        self.queue_size = queue_size
        self.data = [i for i in range(queue_size)]
        self.head = 0
        self.tail = -1

    def is_empty(self):
        return self.tail == -1

    def push(self, element):
        if (self.tail + 1) % self.queue_size == self.head:
            if not self.is_empty():
                print("No more space")
                return

        self.tail = (self.tail + 1) % self.queue_size
        self.data[self.tail] = element

    def pop(self):
        if self.is_empty():
            print("Nothing to pop")
            return
        print(self.data[self.head])
        self.head = (self.head + 1) % self.queue_size

        # deal with empty queue (separate it from other situations)
        if self.head - self.tail == 1:
            self.tail = -1
            self.head = 0

    def show(self):
        if self.is_empty():
            print("The queue is empty")
            return
        if self.tail >= self.head:
            print(self.data[self.head: self.tail + 1])
            return

        data = self.data[self.head:]
        data += self.data[: self.tail + 1]
        print(data)


q = Queue()
q.show()
q.pop()
q.push(1)
q.show()
q.push(2)
q.show()
q.pop()
q.show()
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.show()
q.push(7)
q.show()
q.pop()
q.show()
q.push(8)
q.show()
