import numpy as np

#will import the base and weight files
baseData = np.genfromtxt('packet_base.txt', delimiter = ',')
weightData = np.genfromtxt('packet_weight.txt', delimiter = ',')

#separate your data into chunks of 8. 
baseArray = baseData.reshape(4096, 8)
weightArray = weightData.reshape(4096, 8)

#multiply your base array by your weight array for every element
multipliedArray = np.multiply(baseArray, weightArray) 

#finding the min, max, and mean of each array chunk with a result
minArray = np.min(multipliedArray, 1)
maxArray = np.max(multipliedArray, 1)
meanArray = np.mean(multipliedArray, 1)

result = (maxArray - meanArray) * minArray

#finding the sum and rounding down
sumArray = np.sum(result)
remainder = np.remainder(sumArray, 4096)
answer = np.floor(remainder)

#print answer
print(answer)