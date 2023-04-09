#Python Assignment No. 02 (Q4)

"""Write a Pandas program to compute the mean, standard
deviation, minimum, 25th percentile, median, 75th, and
maximum of the data of a given Series."""

import pandas as pd

def main():
    # Take user input for Series data
    data = pd.Series([int(x) for x in input("Enter comma separated values for Series data: ").split(",")])

    print("Data:")
    print(data)
    print("Mean:", data.mean())
    print("Standard Deviation:", data.std())
    print("Minimum:", data.min())
    print("25th Percentile:", data.quantile(0.25))
    print("Median:", data.median())
    print("75th Percentile:", data.quantile(0.75))
    print("Maximum:", data.max())

if __name__ == "__main__":
    main()
