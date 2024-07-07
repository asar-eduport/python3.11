"""
Difference Between a Shallow Copy and Deep Copy

Deepcopy creates a different object and populates it with the child objects of the original object. Therefore, changes in the original object are not reflected in the copy.

copy.deepcopy() creates a Deep Copy.

Shallow copy creates a different object and populates it with the references of the child objects within the original object. Therefore, changes in the original object are reflected in the copy.

copy.copy creates a Shallow Copy.

"""


import copy

# Original object
original = [1, 2, [3, 4], 5]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Modifying the nested list in the original
original[2][0] = 'X'

print("Original:", original)    # Output: Original: [1, 2, ['X', 4], 5]
print("Shallow Copy:", shallow) # Output: Shallow Copy: [1, 2, ['X', 4], 5]
print("Deep Copy:", deep)       # Output: Deep Copy: [1, 2, [3, 4], 5]
