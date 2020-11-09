a = list(range(5))
print(a)

import numpy as np

B = np.random.randint(9, size=(5, 5))
print(B)

B = np.array([[7, 2, 1, 5, 0], [3, 8, 4 ,0, 3], [8, 6 ,8 ,3 ,5], [3, 7 ,0 ,4, 8], [0, 1 ,6 ,0, 7]])

C = B[2:4, 2:4]

print(C)

B[:, 3] = 99

print(C)



