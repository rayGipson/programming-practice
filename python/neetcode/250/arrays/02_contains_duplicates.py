def hasDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 3], True),   # Example 1
        ([1, 2, 3, 4], False),  # Example 2
        ([], False),            # empty list
        ([5], False),           # single element
        ([7, 7, 7, 7], True),   # all same
        ([1, 2, 1], True),      # duplicate at beginning + end
        ([1, 2, 3, 4, 5, 6], False),
    ]

    for nums, expected in test_cases:
        result = hasDuplicate(nums)
        print(f"Input: {nums} -> Output: {result} (expected: {expected})")