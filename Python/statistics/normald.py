import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print("%5.3f" %(cdf(19.5)))
# Between 20 and 22
print("%5.3f" %(cdf(22) - cdf(20)))