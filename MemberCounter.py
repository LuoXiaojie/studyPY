__metaclass__ = type


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


def main():
    memberOne = MemberCounter()
    print memberOne.members
    student = StudentMember()
    print hasattr(student, 'functest')
    print callable(getattr(student, 'functest', None))
    pass
if __name__ == '__main__':
    main()
