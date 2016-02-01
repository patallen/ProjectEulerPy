# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(num):
    string = str(num)
    return string == string[::-1]


def largest_palindrome(digits=3):
    start = int(digits * '9')
    palindromes = []
    for x in reversed(xrange(start)):
        for y in reversed(xrange(x)):
            if is_palindrome(y*x):
                palindromes.append(y*x)
    return max(palindromes)

print largest_palindrome(3)
