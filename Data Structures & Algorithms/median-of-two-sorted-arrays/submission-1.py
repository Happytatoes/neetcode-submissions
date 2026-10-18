class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # A is the smaller array
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        l, r = 0, len(A) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        even = (total % 2 == 0)
        
        # binary search for the partition in A such that
        # we can find the median
        while True:
            m = (l + r) // 2
            c = half - m - 2

            A_left = A[m] if m >= 0 else -float('inf')
            A_right =  A[m+1] if m + 1 < len(A) else float('inf')
            B_left = B[c] if c >= 0 else -float('inf')
            B_right = B[c+1] if c + 1 < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                # we found the right partition!
                if even: 
                    return (max(A_left, B_left) + min(B_right, A_right)) / 2
                else:
                    return min(B_right, A_right)
            elif B_left > A_right:
                # m is too small
                l = m + 1
            else: 
                # m is too large
                r = m - 1

