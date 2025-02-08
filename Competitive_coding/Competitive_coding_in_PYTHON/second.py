class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack underflow")
            exit(1)

def evaluate_expression(expression):
    stack = Stack()

    for ch in expression:
        if ch.isdigit():
            stack.push(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if ch == '+':
                stack.push(operand1 + operand2)
            elif ch == '-':
                stack.push(operand1 - operand2)
            elif ch == '*':
                stack.push(operand1 * operand2)
            elif ch == '/':
                if operand2 != 0:
                    stack.push(operand1 // operand2)  # Use // for integer division
                else:
                    print("Division by zero error")
                    exit(1)

    if not stack.is_empty():
        return stack.pop()
    else:
        print("Invalid expression")
        exit(1)

if __name__ == "__main__":
    expression = "36+9*"  # Example postfix expression
    print("Result:", evaluate_expression(expression))