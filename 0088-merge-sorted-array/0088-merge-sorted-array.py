class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0 and n == 1:
            nums1[:] = nums2
            return
        elif m == 1 and n == 0:
            return
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n])