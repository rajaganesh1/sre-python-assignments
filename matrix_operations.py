#Matrix operations for nxn matrix only
import numpy

R1 = int(input("Enter the number of rows for Matrix1:")) 
C1 = int(input("Enter the number of columns for Matrix1:")) 

# Initialize matrix 1
matrix1 = [] 
print("Enter the row wise entries for Matrix1 line by line :") 

for i in range(R1):		 
	a =[] 
	for j in range(C1):	 
		a.append(int(input())) 
	matrix1.append(a) 

# Print matrix 1 
for i in range(R1): 
	for j in range(C1): 
		print(matrix1[i][j], end = " ") 
	print() 

#########################################################

R2 = int(input("Enter the number of rows for Matrix2:")) 
C2 = int(input("Enter the number of columns for Matrix2:")) 

# Initialize matrix 2
matrix2 = [] 
print("Enter the row wise entries for Matrix2 line by line:") 

for i in range(R2):		 
	a =[] 
	for j in range(C2):	 
		a.append(int(input())) 
	matrix2.append(a) 

# For printing the matrix 
for i in range(R2): 
	for j in range(C2): 
		print(matrix2[i][j], end = " ") 
	print()
a = numpy.array(matrix1)
b= numpy.array(matrix2)
#addition of Matrices
print("Addition of Matrices :")

print(numpy.add(a,b))

#Multiplication of Matrices
if (C1 == R2):
	print("Multiplication of Matrices :")
	print(numpy.multiply(a,b))
else:
	print("Multiplication is not possible")

#Transpose of Matrices
print("Transpose of matrix 1 is : ")
print(a.T)

print("Transpose of matrix 2 is :")
print(b.T)