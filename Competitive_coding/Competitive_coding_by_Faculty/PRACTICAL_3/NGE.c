#include<stdio.h>
#include<stdlib.h>
#define max 100

void NEXT_GREATER_ELEMENT(int arr[] , int n){
    int stack[max];
    int top = -1;
    int result[max];
    
    for (int i = 0; i < n; i++)
    {
        result[i] = -1;
    }

    for (int i = 0; i < n; i++)
    {
        while(top != -1 && arr[i] > arr[stack[top]]){
            int idx = stack[top--];
            result[idx] = arr[i];
        }
        stack[++top] = i;
    }
    printf("Element in Stack are: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\nElement in NGE are: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ",result[i]);
    }    
}

int main(){

    int array[5] = {4,5,9,2,1};
    NEXT_GREATER_ELEMENT(array,5);
    return 0;
}