import heapq

def find_product_of_three_largest(nums):
    # Use a set to get distinct elements
    unique_nums = list(set(nums))
    
    # If less than 3 distinct elements, return None or raise an error
    if len(unique_nums) < 3:
        return None
    
    # Use heapq.nlargest to get the three largest distinct elements efficiently
    largest1, largest2, largest3 = heapq.nlargest(3, unique_nums)
    
    # Return the product of the three largest elements
    return largest1 * largest2 * largest3

if __name__ == "__main__":
    # Input array
    nums = [5, 10, 2, 8, 15, 3]
    
    # Calculate and display the product of the three largest distinct elements
    result = find_product_of_three_largest(nums)
    if result is not None:
        print("Product of the three largest distinct elements:", result)
    else:
        print("Not enough distinct elements to compute the product.")
