__metaclass__ = type


def main():
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        result = x / y
    except(ZeroDivisionError, TypeError) as e:
        print 'your number is wrong and the except is %s' % e
    else:
        print 'the input is ok and the result is %s' % result
if __name__ == "__main__":
    main()
