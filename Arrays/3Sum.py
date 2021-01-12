def twoSum(i, nums, result):
    lo = i + 1
    hi = len(nums) - 1
    while lo < hi:
        total = nums[i] + nums[lo] + nums[hi]
        if total == 0:
            result.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1
        elif total < 0:
            lo += 1
        else:
            hi -= 1
    return result


def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if nums[i] == 0 or nums[i] != nums[i - 1]:
            twoSum(i, nums, result)
    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
