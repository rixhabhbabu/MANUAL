class MinStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []  # List to hold stack elements
        self.minData = []  # List to hold minimum elements
        self.top = -1  # Index of the top element

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, element):
        if self.isFull():
            print("Overflow")
            return

        self.top += 1
        self.data.append(element)

        # Update the min stack
        if self.top == 0 or element <= self.minData[self.top - 1]:
            self.minData.append(element)
        else:
            self.minData.append(self.minData[self.top - 1])

    def pop(self):
        if self.isEmpty():
            print("Underflow")
            return

        popped = self.data.pop()
        self.top -= 1
        self.minData.pop()

    def top_element(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1

        return self.data[self.top]

    def getMin(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1

        return self.minData[self.top]

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        print("Elements in the stack:", end=" ")
        for i in range(self.top + 1):
            print(self.data[i], end=" ")
        print()

# Main function to demonstrate the MinStack
if __name__ == "__main__":
    minStack = MinStack(5)

    minStack.push(3)
    minStack.push(5)
    minStack.push(2)
    minStack.push(7)
    minStack.push(1)

    minStack.display()
    print("Min element in stack:", minStack.getMin())

    minStack.pop()
    minStack.pop()

    print("Top element in stack:", minStack.top_element())