from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 4, 1, 2],
        [22, 21, 20, 1],
        [],
        [1],
        [5, 10, 15]
    ]
    for nums in test_cases:
        result = sol.getConcatenation(nums)
        print(f"Input: {nums} -> Result: {result}")