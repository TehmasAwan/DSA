class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1

capacity = 5
my_circular_queue = CircularQueue(capacity)

my_circular_queue.enqueue(1)
my_circular_queue.enqueue(2)
my_circular_queue.enqueue(3)

print("Queue size:", my_circular_queue.size())

print("Dequeue:", my_circular_queue.dequeue())
print("Dequeue:", my_circular_queue.dequeue())

print("Is the queue empty?", my_circular_queue.is_empty())
print("Is the queue full?", my_circular_queue.is_full())
