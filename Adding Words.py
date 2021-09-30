""" You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great

"""


def concatenate(*args):
    for i in args:
        return '-'.join(args)# functia join() ia fiecare element din lista si le leaga intr-un string folosind "-"
print(concatenate("I", "love", "Python", "!"))