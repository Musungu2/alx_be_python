class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        result = a + b
        return result
    
    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        c = a * b
        return c

