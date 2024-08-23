def main():
    num = []
    i = 0
    for i in range(10):
        numbers = int(input("Please enter the numbers {}: ".format(i+1)))
        num.append(numbers)
    total = Total(num)
    largest = Largest(num)
    smallest = Smallest(num)
    totalPos = TotalPositiveNumbers(num)
    totalNeg = TotalNegativeNumbers(num)
    numNeg = NumberNegativeNumbersEntered(num)
    countBetween = NumbersEnteredBetween(num)

    print("Total: ", total)
    print("Largest: ", largest)
    print("Smallest: ", smallest)
    print("Total Positive: ", totalPos)
    print("Total Negative: ", totalNeg)
    print("How Many Negative: ", numNeg)
    print("Count In Between 50 & 100: ", countBetween)

def Total(numbers):
    totalNum = 0
    for num in numbers:
        totalNum += num
    
    return totalNum

def Largest(numbers):
    largestNum = numbers[0]
    for num in numbers:
        if num > largestNum:
            largestNum = num
    return largestNum

def Smallest(numbers):
    smallestNum = numbers[0]
    for num in numbers:
        if num < smallestNum:
            smallestNum = num
    return smallestNum


def TotalPositiveNumbers(numbers):
    totalPositiveNum = 0

    for num in numbers:
        if num > 0:
            totalPositiveNum += num
        else:
            continue
    return totalPositiveNum

def TotalNegativeNumbers(numbers):
    totalNegativeNum = 0

    for num in numbers:
        if num < 0:
            totalNegativeNum += num
        else:
            continue
    return totalNegativeNum

def NumberNegativeNumbersEntered(numbers):
    numberNegativeNum = 0

    for num in numbers:
        if num < 0:
            numberNegativeNum += 1
        else:
            continue
    return numberNegativeNum

def NumbersEnteredBetween(numbers):
    numberInBetween = 0

    for num in numbers:
        if num > 50 and num < 100:
            numberInBetween += 1
        else:
            continue
    return numberInBetween

if __name__ == "__main__":
    main()

