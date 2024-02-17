from random import choice


class Rand_operation:
    def __int__(self, num_1, num_2):
        self.__num1 = num_1
        self.__num2 = num_2

        def __rand_oper(self):
            symb = ["_", "+","-"]
            oper = choice(symb)
            if oper == "_":
                return self.__num1_self.__num2
            elif oper == "-":
                return self.__mum1 - self.__num2
            elif oper == "+":
                return self.__num1 + self.__num2

    def result(self):
        return self.__rand_oper()


"num_1" == 25
"num_2" == 24
my_random = Rand_operation("num_1, num_2)
    print(my_random.result())