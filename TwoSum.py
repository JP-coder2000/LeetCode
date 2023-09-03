def twoNumberSum(array, targetSum):
    values = {}
    for number in array:
        if targetSum - number in values:
            return [values[targetSum-number], number]
        else:
            values[number] = number
    return[]
