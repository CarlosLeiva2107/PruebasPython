
def getMaxAggregateTemperatureChange(tempChanges):
    maxList = []
    for i,j in enumerate(tempChanges):
        prevDays = tempChanges[0:i+1]
        nextDays = tempChanges[i:]
        maxList.append(max(sum(prevDays),sum(nextDays)))
    return max(maxList)

print(getMaxAggregateTemperatureChange([6,-2,5]))