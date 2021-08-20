import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "Project_File.xlsx"
xls = pd.ExcelFile(file)

otherCountries = xls.parse(
    usecols=[0,13,14,15,16,17,18,30,31,32,33,34],
    names=["", "India", "Pakistan", "Sri Lanka", "Saudi Arabia", "Kuwait", "UAE", "USA", "Canada", "Australia", "New Zealand", "Africa"]
)
print(otherCountries)

year = otherCountries.iloc[:,0].str.split(' ', n = 2, expand = True)
print(year)

year = otherCountries.assign(Year=year[0])
print(year)

# print 1988 - 1997
othersYearRange = otherCountries[(year['Year'] >= str(1988)) & (year['Year'] <= str(1997))]
print(othersYearRange)

# create another dataframe without the years and months
others = otherCountries[["India", "Pakistan", "Sri Lanka", "Saudi Arabia", "Kuwait", "UAE", "USA", "Canada", "Australia", "New Zealand", "Africa"]]
print(others)

# to calculate the whole 10 years range
others = others.astype(int)
calculateSum = others.sum()
print(calculateSum)

# sort to ascending order (from greater to smaller)
sortAsc = calculateSum.sort_values(ascending=False)
print(sortAsc)


# sort out the top 3 countries
sortTop3Countries = sortAsc.head(3)
print(sortTop3Countries)


# plotting top 3 countries with the most visitors chart
ps = sortTop3Countries.sort_values(ascending=False)
#index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Visitors', fontsize=10)
plt.title('Top 3 Others countries from 1988-1997')
plt.bar(ps.index, ps.values/1000)
plt.show()

# plotting all countries with the most visitors chart
ps = calculateSum
plt.xlabel('Countries', fontsize=10)
plt.ylabel('Vistors', fontsize=10)
plt.title('All Others Countries')
plt.bar(ps.index, ps.values/1000)
plt.show()


# total sum of the top 3 countries
top3CountriesSum = sortTop3Countries.sum()
print("Total sum of the top 3 others countries:", top3CountriesSum)


# mean of the top 3 countries
top3CountriesMean = sortTop3Countries.mean()
print("Total mean of the top 3 others countries:", round(top3CountriesMean, 1))


# median of the top 3 countries
top3CountriesMean = sortTop3Countries.median()
print("Median of the top 3 other countries:", top3CountriesMean)


# Unit Testing
class Testing:
    def add(num1, num2, num3):
        result = num1 + num2 + num3
        return result

    def mean(num2):
        result = sum(num2) / len(num2)
        return result








