#coding=utf-8
__metaclass__ = type
import shelve
from urllib import urlopen

class MemberCounter:
    members = 0

    def __init__(self):
        MemberCounter.members += 1


class Person:

    def __init__(self, namestr="test"):
        self.name = namestr


class StudentMember(MemberCounter, Person):
    student = 1

    def __init__(self):
        super(StudentMember, self).__init__

    def functest(self):
        print 'hello world'
    pass

def testShelve():
    s = shelve.open('test.dat')
    #类似于字典一样的东东。可以存储对象。
    s['x'] = ['a', 'b', 'c']
    temp = s['x'] #取出x对应的值
    print s
    temp.append('d') #给数组添加元素
    s['x'] = temp #更新数据库中的信息。
    print s

def main():
    memberOne = MemberCounter()
    print memberOne.members
    student = StudentMember()
    studentDB = shelve.open('test.dat')
    studentDB['A'] = student
    print studentDB
    studenttest = studentDB['A']
    studenttest.functest()
    print hasattr(student, 'functest')
    print callable(getattr(student, 'functest', None))
    from constants import test
    test.test()
    print dir(test)
    listS = [0,1,2,3,1,2,3,4,5,6,7,8,9,7,4,5,6]
    print set(listS)
    testShelve()
    webPage = urlopen('https://www.baidu.com/')
    print webPage.read()
    pass
if __name__ == '__main__':
    main()
