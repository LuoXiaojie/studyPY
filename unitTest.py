#coding=utf-8
__metaclass__ = type
import unittest, my_math
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):
    def testWithPylint(self):
        cmd = 'pylint -rn {0}'.format('my_math')
        result = Popen(cmd, stdout = PIPE, stderr = PIPE)
        self.assertEqual(result.stdout.read(), '')

    def testIntegers(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                p = my_math.product(x, y)
                self.failUnless(p == x*y, 'Integer multiplication failed')

    def testFloats(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                x = x/10.0
                y = y/10.0
                p = my_math.product(x, y)
                self.failUnless(p == x*y, 'Float multiplication failed')

if __name__ == '__main__':
    unittest.main() #unittest.main函数负责运行测试.它会实例化所有TestCase的子类,运行所有名字以test开头的方法.
       
