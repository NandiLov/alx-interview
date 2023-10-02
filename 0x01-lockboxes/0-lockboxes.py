#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    if not boxes:
        return False
    visited = set()
    visited.add(0)
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                stack.append(key)
    return len(visited) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Should print True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Should print True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Should print False
