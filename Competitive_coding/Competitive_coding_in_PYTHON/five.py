from queue import Queue

def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator == '^':
        return 3
    return 0

def infix_to_postfix(infix):
    stack = []
    output_queue = Queue()
    
    for token in infix:
        if token.isalnum():  # If the token is an operand, add it to the output queue
            output_queue.put(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output_queue.put(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # If the token is an operator
            while stack and precedence(stack[-1]) >= precedence(token):
                output_queue.put(stack.pop())
            stack.append(token)
    
    while stack:  # Pop all remaining operators from the stack
        output_queue.put(stack.pop())
    
    postfix = []
    while not output_queue.empty():
        postfix.append(output_queue.get())
    
    return ' '.join(postfix)

if __name__ == "__main__":
    infix_expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Postfix expression:", postfix_expression)
