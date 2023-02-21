import random
import eightball

def get_average(test_scores):
    # determine new average
    sum = 0
    for a_test in test_scores:
        sum += a_test
    average = int(sum / len(test_scores))
    return average

test_scores = []

done = False

# take in scores
while not done:
    grade = int(input("Enter test score: "))
    if grade >= 0:
        test_scores.append(grade)
    else:
        done = True

# print out list contents
print("There are",len(test_scores),"tests in this group.")
for a_test in test_scores:
    print(a_test)

# determine average
sum = 0
for a_test in test_scores:
    sum += a_test
average = int(sum/len(test_scores))
print("The class average is",average)

# curve if lower than 60
for i in range(len(test_scores)):
    if test_scores[i] < 60:
        test_scores[i] += 10 # add letter grade if failing

print("Revised test scores")
for a_test in test_scores:
    print(a_test)


print("The new class average is", get_average(test_scores))


""" Other neat things about lists """
# shuffle a list
random.shuffle(test_scores)
print("Shuffled test scores")
for a_test in test_scores:
    print(a_test)




done = False
while not done:
    trash = input("Ask the 8-ball").lower()
    if trash == 'q':
        done = True
    else:
        print(eightball.eight_ball_answers[random.randint(0,len(eightball.eight_ball_answers) - 1)])
        # or
        # print(random.choice(eight_ball_answers))

def is_one():
    print("one")

def is_two():
    print("two")

def is_three():
    print("three")

calls = [is_one(), is_two(), is_three()]

for call in calls:
    (call)
