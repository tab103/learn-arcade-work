for i in range(5):
    for j in range(5):
        print(j * i, end=' ')
    print()


# 1
for a in range(1,10,2):
    print(a)

# 2
class thing:
    def __init__(self, width, height, scale, color):
        self.width = width
        self.height = height
        self.scale = scale
        self.color = color

# 3
lst = ['the','brown','fox','jumped','over','the','log']
temp = lst[0]
lst[0] = lst [-1]
lst[-1] = temp
lst[len(lst)-2] = 'a'
print(lst)

# 4
for a in range(10):
    print(a, end='')

# 5
class GroceryCart:
    item_count = 0

def main():
    gc = GroceryCart()
    GroceryCart.item_count = 5

main()

#6
# mp3, wav, ogg
# png, bmp, jpg, gif, etc., are all image formats

#7
b = 'First'
c = 'Second'

z = not (b < c)
print(z)

#8
astring = 'A long time ago in a galaxy far away'
start = 2
end = 11
print(astring[start:end])

# 9
# True false self.scale = 1

# 10
# calling base/parent class constructor

# 11
# difference between function and method

# 12
# grocery cart class example

# 13
import random
lower = 1
upper = 101
for a in range(1000):
    rnd = random.randrange(lower, upper)
    print(rnd)

# 14
# lists and tuples

# 15
for a in range(10):
    if a == 6:
        break
    print(a, end=' ')

# 16
for a in range(10):
    if a % 2 != 0:
        continue
    print(a, end=' ')

# 17
x = 10
y = 0
s = -1

for a in range(x, y, s):
    print(a)


# 18
lst = ['the','brown','fox','jumped','over','the','log']
for l in lst:
    print(l, end = ' ')

# or

for i in range(len(lst)):



    print(lst[i], end = ' ')

# 19
# static variables
class Cat:
    population = 0


# 20
# What is the output of the following code (answer all that apply):

a = 3
b = 7
c = 9

if a < b and c > a:
    if a + b > c:
        print("Path A")
    elif b + c < a:
        print("Path B")
elif a < b:
    print("Path C")
else:
    print("Path D")

# 21 Append method to list

# 22
for i in range(5):
    for j in range(5):
        print(j * i, end=' ')
    print()

# 23
a = 3
b = 7
c = 9

z = a == b
print(z)

# 24
# what is a constructor

# 25 on_key_press