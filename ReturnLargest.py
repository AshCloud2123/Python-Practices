def main():
    i = 0
    nums = []
    for i in range (3):
        num = int(input("Enter number {}: ".format(i+1)))
        nums.append(num)
    
    largest = delLargest(nums)
    print("The largest number is:", largest)


def delLargest (nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

if __name__ == "__main__":
    main()