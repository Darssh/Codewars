'''Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
You can assume that you will only get positive integers as inputs.'''


def divisors(integer):
    value = []
    n = integer -1
    while n > 1:
        if integer%(n) == 0:
            value.append(n)
        n -= 1
    if(len(value) == 0):
        return str(integer) + " is prime"
    return sorted(value)     



'''def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l'''


'''def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n'''