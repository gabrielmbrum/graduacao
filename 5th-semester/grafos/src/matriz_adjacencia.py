import numpy as np

# REDES SOCIAL
X = np.array([
    [0, 1, 0], # v0 liga com v1
    [1, 0, 1], #v1 liga com v0 e v2
    [0, 1, 0] #v2 liga com v1
])

# X = np.array([
#     [0, 1, 1], # v0 liga com v1 e v2
#     [1, 0, 1], #v1 liga com v0 e v2
#     [1, 1, 0] #v2 liga com v0 e v1
# ])

print("Matriz Original X (r = 1):")
print(X)
print("\n" + "-"*40 + "\n")

X2 = np.linalg.matrix_power(X, 2)
print("Matriz X^2 (r = 2):")
print(X2)
print("\n" + "-"*40 + "\n")

# X3 = np.linalg.matrix_power(X, 3)
# print("Matriz X^3 (r = 3):")
# print(X3)
# print("\n" + "-"*40 + "\n")

# X4 = np.linalg.matrix_power(X, 4)
# print("Matriz X^4 (r = 4):")
# print(X4)