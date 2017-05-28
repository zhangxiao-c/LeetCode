class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rlist = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] == nums2[j]):
                    if(rlist.count(nums1[i]) == False):
                        rlist.append(nums1[i])
        return rlist;

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    result = Solution().intersection(nums1,nums2)
    print result