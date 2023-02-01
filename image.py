unused_variable = "unused_variable"
unused_variable2 = "unused_variable"
unused_variable3 = "unused_variable"
unused_variable4 = "unused_variable"
unused_variable5 = "unused_variable"
unused_variable6 = "unused_variable"
unused_variable7 = "unused_variable"
unused_variable8 = "unused_variable"
unused_variable9 = "unused_variable"
unused_variable10 = "unused_variable"


class Numbers:
    def __init__(self, n):
        self.n = n

    def print_number(self):
        list1 = list()
        for i in range(len(self.n)):
            list1.append(self.n[i])

        return list1


object1 = Numbers([10, 20])
object1.print_number()


def print_number(n):
    list1 = list()
    for i in range(len(n)):
        list1.append(n[0])

    return list1
