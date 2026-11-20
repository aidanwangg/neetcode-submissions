class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        lengths = []

        for num in nums:
            if (num - 1) in nums_set:
                continue
            length = 1
            curr = num
            while curr + 1 in nums_set:
                length += 1
                curr += 1
            lengths.append(length)
        if lengths == []:
            return 0
        return max(lengths)