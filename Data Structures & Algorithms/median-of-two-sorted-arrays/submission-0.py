class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)

        l, r = 0, n1
        half = (n1 + n2 + 1) // 2

        while l <= r:
            p1 = (l + r) // 2
            p2 = half - p1

            left1 = nums1[p1 - 1] if p1 > 0 else float("-inf")
            right1 = nums1[p1] if p1 < n1 else float("inf")

            left2 = nums2[p2 - 1] if p2 > 0 else float("-inf")
            right2 = nums2[p2] if p2 < n2 else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = p1 - 1

            else:
                l = p1 + 1