import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])
####1###
vec2=(np.pi/4)*vec1
print(vec2)
####2####
vec2 = np.cos( vec2 )
print(vec2)
###3###
vec3 = vec1 + 2 * vec2
print(vec3)
###4###
vec4=la.norm(vec3)
print(vec4)
####5###
matrix1=np.asmatrix(mat1)
matrix2=np.asmatrix(vec3)
print('matrix1:',matrix1)
print('matrix2:',matrix2)
print('multipy',np.cross(matrix1,matrix2))
###6###
T =  mat1.transpose()
print('Transpose:',T)
###7###
d=la.det(mat1)
print(d)
###8###
t=mat1.trace()
print(t)
###9###
minElement = np.amin(vec1)
print('Minimum element from Vector : ', minElement)
###10###
n=vec1.argmin()
print('smalest arguman:',n)
###11###
minElement = np.amin(mat1)
print('Minimum element from matrix : ', minElement)
##12###
A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])
sutuni=A.sum(axis=1)
print('SUM.sutuni:',sutuni)
satri=A.sum(axis=-1)
print('SUM.satri:',satri)

ghotreasli=np.diag(A)
print('ghotre asli:',ghotreasli)
b=ghotreasli.sum()
print('SUM.ghotre asli:',b)

makuseA=np.fliplr(A)
print('makuse A:',makuseA)
ghotrefaree=np.diag(makuseA)
print('ghotre faree:',ghotrefaree)
c=ghotrefaree.sum()
print('SUM.ghotre faree:',c)
###dar hame maghadir 65 shodand pas matrix magic asat###
###13###
M=np.random.rand(10,10)
print('M 10*10 random matrix:',M)
###14###
##upper##
MUL=M[0:5,0:5]
print('MUL:',MUL)
MUR=M[0:5,5:10]
print('MUR:',MUR)
##lower##
MLL=M[5:10,0:5]
print('MLL:',MLL)
MLR=M[5:10,5:10]
print('MLR:',MLR)







