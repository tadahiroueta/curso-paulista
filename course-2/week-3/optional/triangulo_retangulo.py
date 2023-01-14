class Triangulo:
    
    def __init__(self, a, b, c):
        
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def retangulo(self):

        if (self.a ** 2 + self.b ** 2 == self.c ** 2 or
            self.a ** 2 + self.c ** 2 == self.b ** 2 or
            self.b ** 2 + self.c ** 2 == self.a ** 2):

            return True

        return False
