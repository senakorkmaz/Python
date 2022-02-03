import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]
print(type(py_list))

#numpy array
np_array=np.array([1,2,3,4,5,6,7,8,9])
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
print(len(py_multi))
np_multi = np_array.reshape(3,3)
print('Python Multi List')
print(py_multi)
print('Numpy Multi Array')
print(np_multi)
print('Np array ve Np multi arrayin boyutlari')
print(np_array.ndim)
print(np_multi.ndim)
print(np_array.shape)
print(np_multi.shape)