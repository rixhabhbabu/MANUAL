#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

#define max 100

typedef struct{
    int top;
    int data[max];
}Stack;

Stack* createStack(){
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->top = -1;
    return stack;
}
void initilize(Stack *stack){
    stack->top = -1;
}

int isEmpty(Stack *stack){
    return stack->top == -1;
}

int isFull(Stack *stack){
    return stack->top == max-1;
}

void push(Stack *stack,int value){
    if (isFull(stack)){
        printf("Stack is OverFlow!");
        return;
    }
    stack->data[++stack->top] = value;
}

int pop(Stack *stack){
    if (isEmpty(stack)){
        printf("Stack is UnderFlow!");
        return -1;
    }
    return stack->data[stack->top--];
}

int EvaluteExpression(char * expression){
    Stack *stack = createStack();

    for (int i = 0; expression[i] != '\0'; i++)
    {
        char ch = expression[i];
        if (isdigit(ch)){
            push(stack,ch - '0');
        }
        else{
            int operand2 = pop(stack);
            int operand1 = pop(stack);
            switch(ch){
                case '+' : push(stack , operand1 + operand2);break;
                case '-' : push(stack , operand1 - operand2);break;
                case '*' : push(stack , operand1 * operand2);break;
                if (operand2 != 0){
                    push(stack,operand1/operand2);
                }
                else{
                    printf("Division by zero Error\n");
                    exit(EXIT_FAILURE);
                }
                break;

            }
        }
    }

    int result = pop(stack);
    free(stack);
    return result; 
}

int main(){
    char * expression = "36+9*";
    printf("RESULT is : %d\n",EvaluteExpression(expression));

    return 0;
}