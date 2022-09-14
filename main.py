class Twos:

    def __init__(self, number):
        self.number = int(number)

    def power(self):
        powers = 2
        i = 1
        if self.number == 1:
            return i
        else:
            while powers != self.number:
                i = i + 1
                while powers < self.number:
                    powers = powers * 2
                if powers > self.number:
                    powers = powers / 2
                    self.number = self.number - powers
                    powers = 2
                if self.number == 2:
                    i = i + 1
                if self.number == 1:
                    i = i + 1
                    break
            i = i - 1
            return i


test = Twos(input("Podaj liczbę \n"))
print(test.power())


