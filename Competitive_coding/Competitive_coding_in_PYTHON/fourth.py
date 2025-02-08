class CircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
            self.size += 1
            return True
        return False

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def Front(self):
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self):
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    cq = CircularQueue(5)
    print(cq.enQueue(1))  # True
    print(cq.enQueue(2))  # True
    print(cq.enQueue(3))  # True
    print(cq.Front())  # 1
    print(cq.Rear())  # 3
    print(cq.enQueue(4))  # True
    print(cq.enQueue(5))  # True
    print(cq.enQueue(6))  # False
    print(cq.isFull())  # True
    print(cq.deQueue())  # True
    print(cq.deQueue())  # True
    print(cq.Front())  # 3
    print(cq.Rear())  # 5
