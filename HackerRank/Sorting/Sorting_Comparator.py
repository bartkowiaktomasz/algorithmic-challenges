"""
Comparators are used to compare two objects.
In this challenge, you'll create a comparator and use it to sort an array.
"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            else:
                return 1
