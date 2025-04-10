

nums = [1,1,2]
nums1 = [0,0,0,1,1,1,2,2,3,3,4]

def remove_duplicates(numbers):
    for i in range(len(numbers)):
        for i in range(len(numbers) -1):
            if numbers[i] == numbers[i+1]:
                numbers.pop(i+1)
                numbers.append('_')
    numbers_copy = numbers.copy()
    for number, item in enumerate(numbers_copy):
        if item == '_':
            numbers.pop(number)
    return numbers

# print(remove_duplicates(nums))
print(remove_duplicates(nums1))