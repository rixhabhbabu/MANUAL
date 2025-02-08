#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

//Define the maximum element in the stack
#define max 5

typedef struct 
{
    int data[max];
    int min_data[max];
    int top;   
}Min_Stack;

void initilize(Min_Stack *stack){
 stack->top = -1;
}

int isFull(Min_Stack *stack){
    return stack->top == max-1;
}

int isEmpty(Min_Stack *stack){
    return stack->top == -1;
}

void push(Min_Stack *stack , int data){
    if (isFull(stack)){
        printf("Stack is Overflow!");return;
    }
    stack->top++;
    stack->data[stack->top] = data;

    if (stack->top == 0 || data <= stack->min_data[stack->top - 1]) { 
        stack->min_data[stack->top] = data; 
    } else { 
        stack->min_data[stack->top] = stack->min_data[stack->top - 1]; 
    } 
} 

void pop(Min_Stack *stack){
    if (isEmpty(stack)){
        printf("Stack in UnderFlow");
        return;
    }
    int popped_element = stack->data[stack->top];
    stack->top--;
    if(popped_element == stack->min_data[stack->top + 1]){
        stack->min_data[stack->top+1] = INT_MAX;
    }
}

int peek(Min_Stack *stack){
    if (isEmpty(stack)){
        printf("Stack in underflow!");
        return -1;
    }
    return stack->data[stack->top];
}

int getMin(Min_Stack *stack){
    if (isEmpty(stack)){
        printf("Stack is UnderFlow!");
        return -1;
    }
    return stack->min_data[stack->top];
}

void display(Min_Stack *stack){
    if (isEmpty(stack)){
        printf("Stack is UnderFlow!");
        return;
    }
    printf("Elements in Array are: ");
    for (int i = 0; i <= stack->top; i++)
    {
        printf("%d ",stack->data[i]);
    }
    printf("\n");
    
}

int main() { 
    Min_Stack minStack; 
    initilize(&minStack); 
 
    push(&minStack, 3); 
    push(&minStack, 5); 
    push(&minStack, 2); 
    push(&minStack, 7); 
    push(&minStack, 1); 
 
    display(&minStack); 
    printf("Min element in stack: %d\n", getMin(&minStack));  
    
 
    printf("Top element in stack: %d\n", peek(&minStack)); 
     
    return 0; 
} 
