# SE-3, 20, Suraj Jagtap

#Python Experiment No 01

# Implement functions of n that calculate the given series. 
# Calulate the arithmetic mean, geometric mean and harmonic mean of a list of numbers.

import math

def summation(n):
    sum = 0
    for i in range(n):
        sum += math.sin(i/math.pi)
    return round(sum, 2) #rounding off to 2 decimal places

def product(n):
    mult = 1
    for i in range(1, n):
        mult *= 1 - (1 / (4 * i * i))
    return round(mult, 2)

def arithmeticMean(lst):
    am = 0
    for i in lst:
        am += i
    return round(am/len(lst), 2)  #using len() to calculate the length of the list

def geometricMean(lst):
    gm = 1
    for i in lst:
        gm *= i
    return round(math.pow(gm, 1/len(lst)), 2) #using math.pow() to calculate the power 

def harmonicMean(lst):
    hm = 0
    for i in lst:
        hm += 1/i
    return round(len(lst)/hm, 2)

def main():
    x = 1;
    while x != 0:
        print("\n1.Addition Series\n2.Product Series\n3.Arithmetic Mean")
        print("4.Geometric Mean\n5.Harmonic Mean\n0.Exit")
        x = int(input("Enter the choice: "))
        if x == 1:
            n = int(input("Enter the value of n to calulate the SUmmation series: "))
            print("Answer =  " + str(summation(n)))
        elif x == 2:
            n = int(input("Enter the value of n to calulate the product series: "))
            print("Answer =  " + str(product(n)))
        elif x == 3:
            lst = []
            n = int(input("Enter the no. of elements: "))
            print("Enter the List Elements:")
            for i in range(0, n):
                    ele = int(input())

                    lst.append(ele)
            print("Arithmetic Mean of the list = " + str(arithmeticMean(lst)))
        elif x == 4:
            lst = [] #list to store the elements
            n = int(input("Enter the no. of elements: "))
            print("Enter the List Elements:")
            for i in range(0, n):
                    ele = int(input())

                    lst.append(ele) #adding the elements to the list
            print("Geometric Mean of the list = " + str(geometricMean(lst)))
        elif x == 5:
            lst = []
            n = int(input("Enter the no. of elements: "))
            print("Enter the List Elements:")
            for i in range(0, n):
                    ele = int(input())

                    lst.append(ele)
            print("Harmonic Mean of the list = " + str(harmonicMean(lst)))
        

main()
                    
                    
            

