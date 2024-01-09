import numpy as np


arr = np.arange(1, 10)
print(f"\nDefault arr: \n{arr}")
print(f"\narr + arr: \n{(arr + arr)}")
print(f"\narr - arr: \n{(arr - arr)}")
print(f"\narr * arr: \n{(arr * arr)}")
print(f"\narr / arr: \n{(arr / arr)}")
print(f"\narr + 5: \n{(arr + 5)}")
print(f"\narr - 5: \n{(arr - 5)}")
print(f"\narr ** 2: \n{(arr ** 2)}")
print(f"\narr sqrt: \n{np.sqrt(arr)}")
print(f"\narr exp: \n{np.exp(arr)}")
print(f"\narr sin: \n{np.sin(arr)}")
print(f"\narr cos: \n{np.cos(arr)}")
print(f"\narr log: \n{np.log(arr)}")