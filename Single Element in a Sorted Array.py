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

class Solution():
    def singleNonDuplicate(self, nums):
        ans = 0
        for item in nums:
            ans = ans^item
        return ans

if __name__ == '__main__':
    unittest.main()
