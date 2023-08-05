class Algorithms:
    def __init__(self, logger: bool = True):
        self.logger = logger

    @staticmethod
    def pack(*args):
        return [*args]

    @staticmethod
    def sort(args: list, reverse: bool = True):
        args.sort(reverse=reverse)
        return args

    def my_mod(self, a: int, b: int):
        d, m = a // b, a % b
        if self.logger:
            print(f'{a}/{b} div: {d}, mod: {m}')
        return d, m

    def euclid_e(self, a: int, b: int):
        while True:

            r = self.my_mod(a, b)[1]

            if r == 0:
                break

            a = b
            b = r

        if self.logger:
            print(f'result: {b}')
        return b

    def euclid_f(self, a: int, b: int):
        a, b = self.sort(self.pack(a, b), True)

        while True:
            a = self.my_mod(a, b)[1]
            if a == 0:
                if self.logger:
                    print(f'result: {b}')
                return b

                break
            b = self.my_mod(b, a)[1]
            if b == 0:
                if self.logger:
                    print(f'result: {a}')
                return a
                break