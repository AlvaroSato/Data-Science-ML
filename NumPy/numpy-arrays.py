#Import Libs
import numpy as np

my_list = [1, 2, 3]
print(f"Array: \n{np.array(my_list)}") 
# [1, 2, 3]

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: \n{np.array(my_mat)}")
#[[1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]]


#np.arrange(start, stop, step)
print(f"\nArray (Default Step):\n{np.arange(0, 11)}")
print(f"\nArray (Step = 2): \n{np.arange(0, 11, 2)}")


print(f"\nnp.zeros:\n{np.zeros(5)}")
print(f"\nnp.zeros(3, 3):\n{np.zeros((3, 3))}")

print(f"\nnp.ones:\n{np.ones(5)}")
print(f"\nnp.ones(3, 3): \n{np.ones((3, 3))}")

#np.linspace(start, stop, n)
print(f"\nnp.linspace(0, 5, 10): \n{np.linspace(0, 5, 10)}")

print(f"\nnp.eye(3): \n{np.eye(3)}")
print(f"\nnp.eye(5): \n{np.eye(5)}")

print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=- RANDOM =-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

#Random number between 0 - 1
print(f"\nnp.random.rand: \n{np.random.rand(5)}")
print(f"\nnp.random.rand(3, 3): \n{np.random.rand(3, 3)}")

print(f"\nnp.random.randn: \n{np.random.randn(5)}")
print(f"\nnp.random.randn(3, 3): \n{np.random.randn(3, 3)}")

#np.random.randint(start, stop, n)
#Random int between the start and stop(not included), and optionally can pass the n numbers
print(f"\nnp.random.randint: \n{np.random.randint(0, 100, 5)}")

print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=- METHODs =-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

arr = np.arange(25)
randarr = np.random.randint(0, 50, 10)

print(f"\nReshape: \n{arr.reshape(5, 5)}")
print(f"\nMax and index: \n{randarr}\n{randarr.max()}, {randarr.argmax()}")
print(f"\nMin and index: \n{randarr}\n{randarr.min()}, {randarr.argmin()}")

print(f"\narr default shape: \n{arr.shape}")
print(f"\nrandarr shape: \n{randarr.shape}")
print(f"\narr.reshape(5, 5) shape: \n{arr.reshape(5, 5).shape}")
