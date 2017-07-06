import unittest

class unitest(unittest.TestCase):
    def testNumberZero(self):
        nums = [0];
        ans = 0;
        self.assertEqual(Solution().singleNonDuplicate(nums),ans);
    def testNumberOne(self):
        nums = [1];
        ans = 1;
        self.assertEqual(Solution().singleNonDuplicate(nums),ans);
    def testList(self):
        nums = [1,1,3];
        ans = 3;
        self.assertEqual(Solution().singleNonDuplicate(nums),ans);

class Solution():
    def singleNonDuplicate(self, nums):
        botton, top = 0,len(nums)-1
        while botton < top:
            middle = int((botton + top) / 2)
            if nums[middle] == nums[middle ^ 1]:
                botton = middle+1
            else:
                top = middle
        return nums[botton]

if __name__ == '__main__':
    unittest.main()
