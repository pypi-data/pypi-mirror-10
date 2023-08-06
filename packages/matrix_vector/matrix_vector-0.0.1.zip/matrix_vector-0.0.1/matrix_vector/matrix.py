from .vector import Vector 


class MatrixDimensionError:
	pass


class Matrix:
	# Initialize Matrix object.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    #   => <matrix_vector.matrix.Matrix object>
    #
    # Example:
    #   >> Matrix(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
    #   => <matrix_vector.matrix.Matrix object>
    #
    # Arguments:
    #   N sequences or N vectors of the same size

	def __init__(self, *rows):
		if len(set(len(_) for _ in rows)) <= 1:
		    self.elements = [Vector(*row) for row in rows]
		else:
			raise TypeError("All rows must be the same length")

    # Returns the number of rows of the matrix.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).rows()
    #   => 3
    #
    # Arguments:
    #   No arguments

	def rows(self):
		return len(self.elements)

    # Returns the number of colums of the matrix.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).colums()
    #   => 3
    #
    # Arguments:
    #   No arguments

	def colums(self):
		return self[0].size

    # Returns the n-th colum of the matrix as an object of class Vector.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).get_colum(1)
    #   => Vector(2, 5, 8)
    #
    # Arguments:
    #   number : (int)

	def get_colum(self, number):
		if (number in range(self.colums())):
			return Vector(*[element[number] for element in self.elements])
		else:
			raise IndexError("Matix index out of range")
    
    # Returns the n-th row of the matrix as an object of class Vector.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).get_row(1)
    #   => Vector(4, 5, 6)
    #
    # Arguments:
    #   number : (int)

	def get_row(self, number):
		if (number in range(self.rows())):
			return self[number]
		else:
			raise IndexError("Matix index out of range")

    # Boolean method checkig if two matrices have the same dimensions.
    # 
    # Example:
    #   >> Matrix([1, 2], [4, 5]).is_same_dimension(Matrix([3, 2], [6, 7]))
    #   => True
    #
    # Arguments:
    #   matrix : (Matrix)

	def is_same_dimension(self, matrix):
		return self.rows() == matrix.rows() and self.colums() == matrix.colums()


	def __add_matrix(self, matrix):
		return Matrix(*[list(x + y) for x, y in zip(self.elements, matrix.elements)])


	def __add_number(self, number):
		return Matrix(*[list(x + number) for x in self.coordinates])


	def __sub_matrix(self, matrix):
		return Matrix(*[list(x - y) for x, y in zip(self.elements, matrix.elements)])
		   

	def __sub_number(self, number):
		return Matrix(*[list(x - number) for x in self.coordinates])

    # Depending on the argument either adds a number to the elements of the matrix or adds two matrices. Returns a new object.
    # 
    # Example(number):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + 2
    #   => Matrix([3, 4, 5], [6, 7, 8], [9, 10, 11])
    #
    # Example(matrix):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    #   => Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])
    #
    # Arguments:
    #   number : (Numeric)
    #   or
    #   matrix : (Matrix)

	def __add__(self, other):
		if type(other) is Matrix:
		    if self.is_same_dimension(other):
		    	return self.__add_matrix(other)
		    else:
		    	raise MatrixDimensionError("Can't add matrices with different dimensions")
		else:
			return self.__add_number(other)

    # Depending on the argument either adds a number to the elements of the matrix or adds two matrices. Changes the object.
    # 
    # Example(number):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + 2
    #   => Matrix([3, 4, 5], [6, 7, 8], [9, 10, 11])
    #
    # Example(matrix):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    #   => Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])
    #
    # Arguments:
    #   number : (Numeric)
    #   or
    #   matrix : (Matrix)


	def __iadd__(self, other):
		self = self + other
		return self
    
    # Depending on the argument either substracts a number from the elements of the matrix or substracts two matrices. Returns a new object.
    # 
    # Example(number):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - 2
    #   => Matrix([-1, 0, 1], [2, 3, 4], [5, 6, 7])
    #
    # Example(matrix):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - Matrix([1, 1, 3], [2, 5, 7], [2, 3, 4])
    #   => Matrix([0, 1, 0], [2, 0, -1], [5, 5, 5])
    #
    # Arguments:
    #   number : (Numeric)
    #   or
    #   matrix : (Matrix)


	def __sub__(self, other):
		if type(other) is Matrix:
		    if self.is_same_dimension(other):
		    	return self.__sub_matrix(other)
		    else:
		    	raise MatrixDimensionError("Can't substitute matrices with different dimensions")
		else:
			return self.__sub_number(other)

    # Depending on the argument either substracts a number from the elements of the matrix or substracts two matrices. Changes the object.
    # 
    # Example(number):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - 2
    #   => Matrix([-1, 0, 1], [2, 3, 4], [5, 6, 7])
    #
    # Example(matrix):
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - Matrix([1, 1, 3], [2, 5, 7], [2, 3, 4])
    #   => Matrix([0, 1, 0], [2, 0, -1], [5, 5, 5])
    #
    # Arguments:
    #   number : (Numeric)
    #   or
    #   matrix : (Matrix)

	def __isub__(self, other):
		self = self - other
		return self

    # Access the elements of the matrix with the [] operator.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])[1]
    #   => Vector(4, 5, 6)
    #
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])[1][2]
    #   => 6
    #
    # Arguments:
    #   number : (int)

	def __getitem__(self, index):
		return self.elements[index]

    # Tranposes a matrix. Returns a new object.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).transposed()
    #   => Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9])
    #
    # Arguments:
    #   No arguments

	def transposed(self):
		return Matrix(*[self.get_colum(i) for i in range(self.colums())])
    
    # Tranposes a matrix. Changes the object.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).transpose()
    #   => Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9])
    #
    # Arguments:
    #   No arguments

	def transpose(self):
		self = self.transposed()
		return self

    # Depending on the argument eigher multiplies the matrix elements with a number or mlultiplies two matrices.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) * 2
    #   => Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])
    #
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) * Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    #   => Matrix([30, 36, 42], [66, 81, 96], [102, 126, 150])
    #
    # Arguments:
    #   number : (Numeric)
    #   matrix : (Matrix)

	def __mul__(self, other):
		if (type(other) is Matrix):
			transposed_other = other.transposed()
			if (self.colums() == other.rows()):
				return Matrix(*[[x * y for y in transposed_other] for x in self.elements])
			else:
				raise MatrixDimensionError("Can't multiply matrices with unsutable dimensions")
		else:
			return Matrix(*[list(x * other) for x in self.elements])
    
    # Returns a matrix without the row and the colum given as arguments.
    # 
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).minor(0, 1)
    #   => Matrix([4, 6], [7, 9])
    #
    # Arguments:
    #   number1 : (int)
    #   number2 : (int)

	def minor(self, i, j):
		minor = [list(el) for el in self.elements]
		del minor[i]
		for k in range(self.rows() - 1):
			del minor[k][j]
		return Matrix(*minor)
    
    # Finds the determinant of a square matrix.
    #
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).determinant()
    #   => 0
    # Example:
    #   >> Matrix([1, 3, 5], [-4, 7, 1], [5, -2, 1]).determinant()
    #   => -99
    #
    # Arguments:
    #   no arguments

	def determinant(self):
		if (self.rows() == self.colums()):
			if (self.rows() == 1):
				return self[0][0]
			else:
				det = 0
				for x in range(self.colums()):
					det += self[0][x] * (-1) ** (2 + x) * self.minor(0, x).determinant()
			return det
		else:
			raise MatrixDimensionError("Determinant is defined for square matrices only!")

    # Finds the inverse of a square matrix.
    #
    # Example:
    #   >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).inversed()
    #   => 0
    # Example:
    #   >> Matrix([1, 3, 5], [-4, 7, 1], [5, -2, 1]).determinant()
    #   => -99
    #
    # Arguments:
    #   no arguments

	def inversed(self):
		if (self.determinant() == 0):
			m = Matrix(*[[(-1) ** (i + j) * self.minor(i, j).determinant()
				for j in range(self.rows())] for i in range(self.colums())])
			return (m.transposed() * (1 / self.determinant()))
		else:
			raise ZeroDivisionError("Determinant is zero => inverse matrix does not exist.")

	def __eq__(self, matrix):
		return self.elements == matrix.elements


	def print_matrix(self):
		for element in self.elements:
			element.print_vector()
