def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes.
    visited = set()
    visited.add(0)  # Start with the first box, which is unlocked.

    # Initialize a stack to perform depth-first search.
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check if the current box contains keys.
        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    # If all boxes are visited, return True; otherwise, return False.
    return len(visited) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Should print True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Should print True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Should print False
