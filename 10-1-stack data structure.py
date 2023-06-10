class Stack:
    data = None
    stack_size = None

    def __init__(self):
        self.data = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def pop(self):
        if self.is_empty():
            print("None to pop")
            return

        self.stack_size = self.stack_size - 1
        print(self.data[self.stack_size])
        return self.data[self.stack_size]

    def push(self, element):
        self.stack_size = self.stack_size + 1
        if self.stack_size <= len(self.data):
            self.data[self.stack_size - 1] = element
            return
        self.data.append(element)

    def show(self):
        if self.is_empty():
            print("Nothing")
            return
        print(self.data[:self.stack_size])


s = Stack()
s.show()
print(s.is_empty())
s.pop()
s.push(10)
s.push(20)
s.show()
s.pop()
s.show()
s.push(10)
s.push(10)
s.push(10)
s.show()
s.pop()
s.pop()
s.show()
