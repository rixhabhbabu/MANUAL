class NextGreaterElement:
    @staticmethod
    def next_greater_element(arr):
        # Initialize a stack and a result array
        stack = []
        result = [-1] * len(arr)  # Fill the result array with -1 as default

        # Iterate through the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # While stack is not empty and the top of the stack is less than or equal to arr[i]
            while stack and stack[-1] <= arr[i]:
                stack.pop()  # Pop elements that are not greater

            # If stack is not empty, the top element is the next greater element
            if stack:
                result[i] = stack[-1]

            # Push the current element onto the stack
            stack.append(arr[i])

        return result

if __name__ == "__main__":
    arr = [9, 3, 8, 1, 2]
    result = NextGreaterElement.next_greater_element(arr)

    # Print the results
    print("Input array:")
    print(" ".join(map(str, arr)))

    print("Next Greater Elements:")
    print(" ".join(map(str, result)))