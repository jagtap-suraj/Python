#Python Assignment No. 01 (Q2)

"""A lower triangular matrix is a square matrix 
(where the number of rows and columns are equal) 
where all the elements above the diagonal are zero.
For example, the following is a lower triangular matrix
with the number of rows and columns equal to 3.
1 0 0
4 5 0
7 8 9
Write a program to convert a square matrix into a lower
triangular matrix."""

def inputM(size):
    matrix = []
    print("Enter elements of matrix row-wise: ")
    for i in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def display(matrix):
    for row in matrix:
        print(row)

def convert(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i+1, size):
            matrix[i][j] = 0
    return matrix

def main():
    size = int(input("Enter size of square matrix: "))
    matrix = inputM(size)
    print("Original Matrix:")
    display(matrix)
    lower_triangular = convert(matrix)
    print("Lower Triangular Matrix:")
    display(lower_triangular)

if __name__ == "__main__":
    main()
