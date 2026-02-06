class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        counts = {}

        for x in set1:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        for x in set2:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        for x in set3:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        out = []
        for key, val in counts.items():
            if val > 1:
                out.append(key)

        return out
