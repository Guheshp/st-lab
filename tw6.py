# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
#         mid_element = arr[mid]
        
#         if mid_element == target:
#             return mid  # Target found, return the index
#         elif mid_element < target:
#             low = mid + 1  # Search in the right half
#         else:
#             high = mid - 1  # Search in the left half
    
#     return -1  # Target not found

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 9
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Element {target} found at index {result}")
# else:
#     print(f"Element {target} not found")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + high // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    else:
        return -1
    

arr = [1,2,3,4,5,6,7,8,9,10]
target = 1

result = binary_search(arr, target)

if result != -1:
    print(f"element {target} found at index {result}")
else:
    print(f"elemeny {target} not found")