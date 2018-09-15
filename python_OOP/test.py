import unittest

def fib(num):
    numbers = [0,1]
    for i in range(2,num):
        numbers.append(numbers[i-1] + numbers[i-2])
    return numbers

class testFib(unittest.TestCase):
    def testOne(self):
        self.assertTrue(fib(8), [0,1,1,2,3,5,8,13])
    def testTwo(self):
        self.assertTrue(fib(12), [0,1,1,2,3,5,8,13,21,34,55,89])
    def setUp(self):
        print('running setup')
    def tearDown(self):
        print('running teardown')

if __name__ == "__main__":
    unittest.main()