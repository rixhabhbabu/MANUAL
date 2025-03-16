#include<stdio.h>
#include<stdlib.h>
#define max 5

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
    if(isFull(s)){
        printf("Stack is OverFlow!");
        return;
    }
    s->top++;
    s->data[s->top] = element;
    if (s->top == 0 || element <= s->mindata[s->top-1]){
       s->mindata[s->top] = element;
    }
    else {
        s->mindata[s->top] = s->mindata[s->top-1];
    } 
}

int pop(Stack *s){
    if (isEmpty(s)){
        printf("Stack is UnderFlow!");
        return -1;
    }
    return s->data[s->top--]; 
}

int top(Stack *s){
    if (isEmpty(s)){
        printf("Stack is UnderFlow!");
        return -1;
    }
    return s->data[s->top]; 
}

int mintop(Stack *s){
    if (isEmpty(s)){
        printf("Stack is UnderFlow!");
        return -1;
    }
    return s->mindata[s->top]; 
}

void display(Stack *s){
    if (isEmpty(s))
    {
        printf("Stack is UnderFLow!");
    }
    else{
        printf("Element in Stack are: ");
        for(int i = max-1 ; i > -1 ; i--){
            printf("%d ",s->data[i]);
        }
        printf("\n");
    } 
}

void MinDisplay(Stack *s){
    if (isEmpty(s))
    {
        printf("Stack is UnderFLow!");
    }
    else{
        printf("Element in MinStack are: ");
        for(int i = max-1 ; i > -1 ; i--){
            printf("%d ",s->mindata[i]);
        }
        printf("\n");
    }
}

int main(){

    Stack s;
    initilize(&s);
    for (int i = 0; i < 5; i++)
    {
        int mini = 1, maxi = 50;
        int random_number = (rand() % (maxi - mini + 1)) + mini;
        push(&s,random_number);
    }
    pop(&s);
    // pop(&s);
    display(&s);
    MinDisplay(&s);
    printf("Top Element in Stack are: %d \n",top(&s));
    printf("Top Element in MinStack are: %d \n",mintop(&s));
    
    
    return 0;
}