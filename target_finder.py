# Goal: Find a target number inside a list

def find_index(nums, target):
    """
    Find the index of a target value in a sorted list using binary search.

    Args:
        nums: A sorted list of comparable elements.
        target: The value to search for.

    Returns:
        The index of target if found, otherwise -1.

    Time Complexity: O(log n)
    """
    left = 0
    right = len(nums) - 1

    # Keep searching while the range is valid
    while left <= right:
        # Pick the middle element
        mid = (left + right) // 2

        # If the middle is the target, return the index
        if nums[mid] == target:
            return mid

        # If target is bigger, search the right half
        elif nums[mid] < target:
            left = mid + 1

        # If target is smaller, search the left half
        else:
            right = mid - 1

    # If we finish without finding it, return -1
    return -1


# Example list
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Target we want to find
target = 11

# Print the result
print("Index:", find_index(numbers, target))
