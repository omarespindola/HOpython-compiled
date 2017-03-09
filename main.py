import ctypes as C
import numpy as np
math = C.CDLL('./src/libmymath.so')
intp = C.POINTER(C.c_int)
flp = C.POINTER(C.c_float)

#Suma de enteros
math.add_float.restype = C.c_int
math.add_float.argtypes = [C.c_int, C.c_int]

print "La suma por enteros es ", math.add_int(3, 4)

#Suma de flotantes
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]

print "La suma por flotantes es ", math.add_float(5.0, 4.)

#Suma de enteros por referencia

ent1 = C.c_int(2)
ent2 = C.c_int(22)
out1 = C.c_int()

math.add_int_ref(C.byref(ent1), C.byref(ent2), C.byref(out1))

print "La suma de enteros por referencia es ", out1.value

#Suma de flotantes por referencia

ent1 = C.c_float(7)
ent2 = C.c_float(6)
out1 = C.c_float()

math.add_float_ref(C.byref(ent1), C.byref(ent2), C.byref(out1))

print "La suma de flotantes por referencia es ", out1.value

#Suma de arrays

array1 = np.array([1, 2, 3, 4], dtype=C.c_int)
array2 = np.array([6, 7, 8, 9], dtype=C.c_int)
out2 = np.zeros(4, dtype=np.int32)

math.add_int_array(array1.ctypes.data_as(intp), array2.ctypes.data_as(intp), out2.ctypes.data_as(intp), C.c_int(4))

print "La suma de los vectores es: ", out2

#Multiplicacion de arrays

array1 = np.array([1, 2, 3, 4], dtype=C.c_float)
array2 = np.array([6, 7, 8, 9], dtype=C.c_float)
out2 = np.zeros(4, dtype=np.float16)
math.dot_product.restype = C.c_float

a = math.dot_product(array1.ctypes.data_as(flp), array2.ctypes.data_as(flp), C.c_int(4))
print "El producto de los vectores es: ", a




