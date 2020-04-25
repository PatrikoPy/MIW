__all__ = ['Calculator']


class Calculator:
    def add(self, *args):
        current = 0
        try:
            for num in args:
                current += float(num)
            return current
        except:
            print("error")

    def difference(self, a=0, b=0):
        try:
            return float(a) - float(b)
        except:
            print("error")

    def multiply(self, *args):
        current = 1
        try:
            for num in args:
                current *= float(num)
            return current
        except:
            print("error")

    def divide(self, a=1, b=1):
        try:
            return float(a) / float(b)
        except(ZeroDivisionError):
            print("nie dziel przez zero...")
            return 0
        except:
            print("error")


if __name__ == "__main__":
    calc = Calculator()
    print(calc.divide(8, 0))
    print(calc.add(5, 7, 6, 9, 8, 5, 4, 7))
    print(calc.multiply(8, 3, 6))
    print(calc.difference(8, 9))
