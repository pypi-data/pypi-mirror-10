# matrix_vector
A python package for matrices and vectors operations.


  class Vector:
  #size
     Finds the determinant of square matrix.
    
     Example:
       >> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).determinant()
       => 0
     Example:
       >> Matrix([1, 3, 5], [-4, 7, 1], [5, -2, 1]).determinant()
       => -99
    
     Arguments:
       no arguments

  # +
     Adds two vectors or adds a number to the elements of vector. Returns a new object.
     
     Example:
       >> Vector(1, 2, 3) + Vector(4, 5, 6)
       => Vector(5, 7, 9)
    
     Example:
       >> Vector(1, 2, 3) + 3
       => Vector(4, 5, 6)
    
     Arguments:
       vector : (Vector)
       or
       number : (Numeric)

  # -
     Substracts two vectors or substracts a number from the elements of the vector. Returns a new object.
     
     Example:
       >> Vector(1, 2, 3) - Vector(4, 5, 6)
       => Vector(-3, -3, -3)
    
     Example:
       >> Vector(1, 2, 3) - 3
       => Vector(-2, -1, 0)
    
     Arguments:
       vector : (Vector)
       or
       number : (Numeric)
