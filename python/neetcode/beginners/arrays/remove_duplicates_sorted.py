from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        
        for x in nums:
            if x not in result:
                result.append(x)
        return len(result)




if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [1, 1, 2, 3, 4],
        [2, 10, 10, 30, 30, 30],
        [],
        [1],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]


    for nums in test_cases:
        arr = nums[:]
        k = sol.removeDuplicates(arr)
        print(f"Input: {nums} -> k={k}, Result: {arr[:k]}")






