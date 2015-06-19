# HackerRank / Python / Standardize mobile number using Decorators
# Author: Tzu-Wen Lee

def wrapper(func):
    def standardize(numbers):
        return func(['+91 ' + num[-10:-5] + ' ' + num[-5:] for num in numbers])
    return standardize

@wrapper
def sorting(numbers):
    return sorted(numbers)

print '\n'.join(sorting([raw_input() for _ in xrange(input())]))