class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)

        nextGreater = {e:-1 for e in nums1}
        stack = [nums2[n2-1]]

        for i in range(n2-2, -1, -1):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                stack.pop()
            if nums2[i] in nextGreater:  
                nextGreater[nums2[i]] = stack[-1] if len(stack) > 0 else -1
                
            stack.append(nums2[i])
        
        res = []
        for i in range(n1):
            res.append(nextGreater[nums1[i]])

        return res