from wprowadzenie02.cw5 import Calculator


class ScienceCalculator(Calculator):
    def square(self, a):
        try:
            return float(a) ** 2
        except:
            print("error")


if __name__ == "__main__":
    calc = ScienceCalculator()
    print(calc.divide(8, 0))
    print(calc.add(5, 7, 6, 9, 8, 5, 4, 7))
    print(calc.multiply(8, 3, 6))
    print(calc.difference(8, 9))
    print(calc.square(6))
