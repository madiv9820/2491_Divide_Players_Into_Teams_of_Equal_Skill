from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'skill': [3,2,5,1,3,4], 'output': 22},
            2: {'skill': [3,4], 'output': 12},
            3: {'skill': [1,1,2,3], 'output': -1}
        }
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        case = self.__testCases[1]
        res = self.__obj.dividePlayers(case['skill'])
        self.assertIsInstance(res, int)
        self.assertEqual(res, case['output'])

    @timeout(0.5)
    def test_Case_2(self):
        case = self.__testCases[2]
        res = self.__obj.dividePlayers(case['skill'])
        self.assertIsInstance(res, int)
        self.assertEqual(res, case['output'])

    @timeout(0.5)
    def test_Case_3(self):
        case = self.__testCases[3]
        res = self.__obj.dividePlayers(case['skill'])
        self.assertIsInstance(res, int)
        self.assertEqual(res, case['output'])


if __name__ == '__main__':
    unittest.main()