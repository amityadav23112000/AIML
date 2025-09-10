import numpy as np

# l=[1,2,3,4,5];
# np.array(l);
# print(type(l))
# print(type(np.array(l)))


# import numpy as np

# a = np.array([1, 2, 3])             # 1D array
# b = np.array([[1, 2], [3, 4]])      # 2D array (matrix)
# c = np.zeros((2, 3))                # 2x3 array of zeros
# d = np.ones((3, 3))                 # 3x3 array of ones
# e = np.arange(0, 10, 2)             # array from 0 to 10 with step 2
# f = np.linspace(0, 1, 5)            # 5 values from 0 to 1


# print(a,b,c,d,e,f,sep="\n")


# print(b.shape)    # dimensions → (2, 2)
# print(b.ndim)     # number of dimensions → 2
# print(b.size)     # total elements → 4
# print(b.dtype)    # data type → int64 (depends on system)


# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# print(x + y)     # elementwise addition
# print(x * y)     # elementwise multiplication
# print(x @ y)     # dot product → 32
# print(x ** 2)    # power


# arr = np.array([[10, 20, 30], [40, 50, 60]])

# print(arr[0, 1])     # 20 (row0, col1)
# print(arr[:, 1])     # [20 50] (all rows, col1)
# print(arr[1, :])     # [40 50 60] (row1, all cols)
# print(arr[0:2, 1:3]) # [[20 30], [50 60]] (subarray)


# print(np.mean(x))    # average
# print(np.std(x))     # standard deviation
# print(np.max(x))     # maximum
# print(np.sum(x))     # sum



# Random dataset: 100 rows, 4 features
data = np.random.randint(10, 100, (100, 4))
print(data[:5])  # show first 5 rows


reshaped = np.reshape([20,20,1,4],(2,2))  # reshape if needed
print(reshaped)

arr = np.arange(4)            # 1*4 = 4 elements
reshaped = arr.reshape(2, 2)
print(reshaped)
