"""Calculation of measures of dispersion"""
# The smaller the variance and standard deviation are, the closer the data values are to the mean,
# and the less overall dispersion (that is, spread) there is between the values and the mean.

import statistics as stat

## Example 1
data = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

# Calculate the mean
mean_value = stat.mean(data)
print(f'The mean for data is: {mean_value}')

# Calculate the population variance of the data
population_variance = stat.pvariance(data)
print(f'Population variance of our data is: {population_variance}') # 2.25

# Calculate the population standard deviation of the data
# Which is the square root of the variance
# In data analytics, this will tone down the effect of outliers in your data.
sd = stat.pstdev(data)
print(f'Population Standard Deviation is : {sd}') #1.5


## Example 2
data2 = [2, 2.5, 2.6, 2.7, 1.8, 1.9, 2, 2, 1.9, 2]

# Calculate the mean
mean_value2 = stat.mean(data2)
print(f'The mean for data 2 is: {mean_value2}')

population_variance2 = stat.pvariance(data2)
print(f'Population variance 2 is: {population_variance2}') #

sd2 = stat.pstdev(data2)
print(f'Population Standard Deviation 2 is : {sd2}') #1.5
