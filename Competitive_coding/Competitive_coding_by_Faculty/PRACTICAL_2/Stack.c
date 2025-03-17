#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define max 7

typedef struct {
    int top;
    int data[max];
    int mindata[max];
}Stack;

void initilize(Stack *s){
    s->top = -1;
}

int isEmpty(Stack *s){
    return s->top == -1;
}

int isFull(Stack *s){
    return s->top == max-1;
}

void push(Stack *s,int element){
    if (isFull(s)){
        printf("Stack is Overflow!");
        return;
    }
    s->data[++s->top] = element;
    if(s->top == 0 || element <= s->mindata[s->top-1]){
        s->mindata[s->top] = element;
    }
    else{
        s->mindata[s->top] = s->mindata[s->top-1];
    }
}

int pop(Stack *s){
    if (isEmpty(s))
    {
        printf("Stack is UnderFlow! ");
        return -1;
    }
    return s->data[s->top--]; 
}

int top(Stack *s){
    if (isEmpty(s))
    {
        printf("Stack is UnderFlow! ");
        return -1;
    }
    return s->data[s->top]; 
}

int Mintop(Stack *s){
    if (isEmpty(s))
    {
        printf("Stack is UnderFlow! ");
        return -1;
    }
    return s->mindata[s->top]; 
}

void display(Stack *s){
    if(isEmpty(s)){
        printf("Stack is UnderFlow!");
        return;
    }
    printf("Element in Stack are: ");
    for (int i = s->top; i > -1 ; i--)
    {
        printf("%d ",s->data[i]);
    }
    printf("\n");
}

void Mindisplay(Stack *s){
    if(isEmpty(s)){
        printf("Stack is UnderFlow!");
        return;
    }
    printf("Element in MinStack are: ");
    for (int i = s->top; i > -1 ; i--)
    {
        printf("%d ",s->mindata[i]);
    }
    printf("\n");
}

int Evalute_Postfix(char *expression){
    Stack ss;
    initilize(&ss);
    for (int i = 0; expression[i] != '\0'; i++)
    {
        if (isdigit(expression[i]))
        {
            push(&ss,expression[i] - '0');
        }
        else{
            int oprand2 = pop(&ss);
            int oprand1 = pop(&ss);

            switch (expression[i])
            {
                case '+': push(&ss, oprand1 + oprand2);
                 break;
                case '-': push(&ss, oprand1 - oprand2); 
                 break;
                case '*': push(&ss, oprand1 * oprand2);
                 break;
                case '/': push(&ss, oprand1 / oprand2);
                 break;
            
                default: printf("Invalid Opration!");
                break;
            }
        }
        
    }
    return pop(&ss);
    
}

int main(){
    char expression[] = "231*+9-";  // Equivalent to (2 + (3 * 1)) - 9 = -4
    printf("Result: %d\n", Evalute_Postfix(expression));
    
    return 0;
}