# Solution 1 Binary Search
# import bisect
#
# def twoSum(nums, target):
#     index = bisect.bisect_left(nums, target)
#     if nums[index] == target:
#         return index
#     else:
#         return None
#
#
# if __name__ == "__main__":
#     nums = [2, 7, 11, 15]
#
#     t = 9
#
#     for i in range(0, len(nums)):
#         targetVal = t - nums[i]
#         index = twoSum(nums, targetVal)
#         if index is not None:
#             print([i, index])
#             break

# solution 2 hash map
def twoSum(nums, t):
    hashMap = {}
    for i in range(0, len(nums)):
        hashMap[nums[i]] = i

    for i in range(0, len(nums)):
        targetVal = t - nums[i]
        if targetVal in hashMap:
            return [i, hashMap[targetVal]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    t = 9

    print(twoSum(nums, t))
