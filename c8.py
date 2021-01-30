FORMATING STYLE: PEP8

# 1 (Unique Numbers Count)
# A list of numbers is given which can contain up to 100,000 numbers. Determine how many different numbers it contains.

print(len(set(input().split())))


# 2 (Number of Words in the Text)
# The input file contains text. A word is a sequence of non-blank characters in a row. Words separated by one or more spaces or line breaks.
# Determine how many different words are contained in this text.

print(len(set(open('input.txt').read().split())))


# 3 (The Smallest Odd)
# Print the value of the smallest odd element of the list.

print(min(filter(lambda x: x % 2 == 1, map(int, input().split()))))


# 4 (Zero or not)
# Check if the given N numbers contain zeros.
# Input Format: First line contains N. Then N lines with numbers.
# Output Format: Print True if there is at least one zero among the entered numbers, print False otherwise.

from itertools import repeat
print(0 in list(map(lambda r: int(r()), repeat(input, int(input())))))


# 5 (Permutations of the given length*)
# By given N print all permutations of numbers from 1 to N in lexicographical order.

import itertools
print('\n'.join(map(''.join, itertools.permutations(map(str, range(1, int(input()) + 1))))))


# 6 (Prime Numbers)
# Print all primes on the segment [2; n].
# Input Format: Integer number 2<= n <=100000
# Output Format: All prime numbers in ascending order

from math import sqrt

n = int(input())
primes = [2]
for i in range(3, n+1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for k in primes:
        if k > int((sqrt(i)) + 1):
            primes.append(i)
            break
        if i % k == 0:
            break
    else:
        primes.append(i)
print(*primes)


# 7 (Fifth degree)
# The input is a sequence of natural numbers of length . Count multiplication of the fifth powers of the numbers in the sequence.

from functools import reduce

print(reduce(lambda x, y: x * (y ** 5), map(int, [1] + input().split())))


# 8 (XOR)
# XOR function is given by the following truth table:
# xor(0, 0) = 0; xor(0, 1) = 1; xor(1, 0) = 1; xor(1, 1) = 0.
# We have two sequences (a1, …, an) and (b1, …, bn) consist of 0 and 1.
# Calculate the sequence (c1, …, cn) where every ci = xor(ai, bi).
# Input Format: Input two lines consist of 0 and 1, separated by spaces. First line — sequence (a1, …, an). Second line — sequence (b1, …, bn).
# Output Format: Output sequence (c1, …, cn) separating each element with a space.

print(*list(map(lambda xy: (xy[0] + xy[1]) % 2, zip(map(int, input().split()), map(int, input().split())))))


# 9 (XOR-2)

# 10 (Partial sums)
