def knapSack(weight, values, n):
    fraction = []
    for i in range(n):
        fraction.append(values[i] / weight[i])
    totalValue = 0
    totalWeight = 0
    for i in range(n):
        if totalWeight + weight[i] <= weight[0]:
            totalValue += values[i]
            totalWeight += weight[i]
        else:
            totalValue += (values[i] * (weight[0] - totalWeight)) / weight[i]
            break
    return totalValue


values = [110, 120, 2]
weight = [6, 7, 3]
n = len(values)
weight0 = weight[0]
totalValue = knapSack(weight, values, n)
print(f"Total value of knapsack is {totalValue}")