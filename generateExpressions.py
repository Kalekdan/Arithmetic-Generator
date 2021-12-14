import random

maxInt = 100
minInt = 0
includeAddition = True
includeSubtraction = True
includeMultiplication = True
includeDivision = True
numExpressions = 5
expressions = []

for i in range(0,numExpressions):
    tempExpressions = []
    # Generate addition and subtractions
    a = random.randint(minInt,maxInt)
    b = random.randint(minInt,maxInt)
    c = a + b
    if includeAddition:
        tempExpressions.append(f"{a} + {b} = {c}")
    if includeSubtraction:
        tempExpressions.append(f"{c} - {b} = {a}")

    # Generate multiplication and divisions
    a = random.randint(minInt,maxInt)
    b = random.randint(minInt,maxInt)
    c = a * b
    if includeMultiplication:
        tempExpressions.append(f"{a} x {b} = {c}")
    if includeDivision:
        tempExpressions.append(f"{c} ÷ {b} = {a}")
    expressions.append(tempExpressions[random.randint(0,len(tempExpressions)-1)])

print(expressions)