'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t 
figure this out at this point - we’ll get to it soon)
'''

import random
a = []
b = []

num_list_items_a = random.randint(1, 10)
num_list_items_b = random.randint(1, 10)

for i in range(0, (num_list_items_a + 1)):
    a.append(random.randint(0, 15))
    i += 1

for i in range(0, (num_list_items_b + 1)):
    b.append(random.randint(0, 15))
    i += 1

print('random list a = {}\n random list b = {}'.format(a, b))
print('the numbers that a and b have in common are')
c = list(set(a).intersection(set(b)))
c.sort()
print(c)