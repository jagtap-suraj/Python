# SE-3, 20, Suraj Jagtap
# Write a program to implement the patterns given in the attachment

print()
n = int(input("Enter the number of rows and columns: "))
print()

#Patter No. 01
for i in range(n): #Rows
    for j in range(n): #Columns
        if i == n//2 or j == n//2: 
            print("*", end = " ")
        else:
            print(" ", end = " ") 
    print()

# n//2 is the middle row and column of the matrix

print()

#Patter No. 02
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

# i = j & i + j = n - 1 are the diagonal elements of the matrix