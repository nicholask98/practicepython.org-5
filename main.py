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

print('random list a = {}\nrandom list b = {}'.format(a, b))
print('the numbers that a and b have in common are')
c = list(set(a).intersection(set(b)))
c.sort()
print(c)