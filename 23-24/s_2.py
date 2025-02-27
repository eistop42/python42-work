numbers = [4, 12, 3, 43, 4, 100, 2]

def find_max(nums: list):
    max = nums[0]
    for number in nums:
        if number > max:
            max = number
    return max

print(find_max(numbers))

