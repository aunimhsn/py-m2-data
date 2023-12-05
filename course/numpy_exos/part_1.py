import numpy as np

# 1 - 2
numbers = np.array([0.5, 6, 13, 11.4], dtype=np.float16)

# 3 - 4 Créer un ndarray respectant le modèle suivant : [1., 4., 7., 10., 13., 16., 19.]
sequence = np.arange(1, 22, 3, dtype=np.float16)
print(sequence.size)

# 5
print(np.zeros((3, 5, 2)))

# 5. q. uint16 -> (-2**16 / 2) à (2**16 / 2)



