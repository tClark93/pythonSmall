import unittest

def reverseList(alist):
    for i in range(0, int(len(alist)/2)):
        alist[i], alist[len(alist)-i-1] = alist[len(alist)-i-1], alist[i]
    return alist

class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([5,4,3,2,1]), [1,2,3,4,5])
    def testTwo(self):
        self.assertEqual(reverseList([8,5,7,5,3,0,9]), [9,0,3,5,7,5,8])
    def setUp(self):
        print('runnng setup')
    def tearDown(self):
        print('running teardown')

if __name__ == "__main__":
    unittest.main()


def isPalendrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return string

class isPalendromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue('racecar', 'racecar')
    def testTwo(self):
        self.assertTrue('tacocat', 'tacocat')
    def setUp(self):
        print('runnng setup')
    def tearDown(self):
        print('running teardown')

if __name__ == "__main__":
    unittest.main()

    import unittest

import unittest

def coins(num):
    change = {'quarters':0, 'dimes': 0, 'nickels':0, 'pennies':0}
    if num > 25:
        change['quarters'] = int(num/25)
        num = num - change['quarters']*25
    if num < 25 and num > 10:
        change['dimes'] = int(num/10)
        num = num - change['dimes']*10
    if num < 10 and num > 5:
        change['nickels'] = int(num/5)
        num = num - change['nickels']*5 
    change['pennies'] = num
    return change

class testCoins(unittest.TestCase):
    def testOne(self):
        self.assertTrue(coins(81), {'quarters':3, 'dimes':0, 'nickels':1, 'pennies':1})
    def testTwo(self):
        self.assertTrue(coins(23), {'quarters':0, 'dimes':10, 'nickels':0, 'pennies':3})
    def setUp(self):
        print('running setup')
    def tearDown(self):
        print('running teardown')

if __name__ == "__main__":
    unittest.main()

import unittest

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        print(fact)
    return fact


class testfactorial(unittest.TestCase):
    def testOne(self):
        self.assertTrue(factorial(5), 120)
    def testTwo(self):
        self.assertTrue(factorial(8), 40320)
    def setUp(self):
        print('running setup')
    def tearDown(self):
        print('running teardown')

if __name__ == "__main__":
    unittest.main()

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