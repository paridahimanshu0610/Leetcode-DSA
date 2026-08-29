class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGrt = {}
        stack = []

        for e in nums2[::-1]:
            while len(stack) > 0 and stack[-1] <= e:
                stack.pop()

            if len(stack) > 0:
                nextGrt[e] = stack[-1]
            else:
                nextGrt[e] = -1

            stack.append(e)

        res = [None]*len(nums1)

        for i in range(len(nums1)):
            res[i] = nextGrt[nums1[i]]

        return res 