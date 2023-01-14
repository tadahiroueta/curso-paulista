class Triangulo:
    
    def __init__(self, a, b, c):
        
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def perimetro(self):
        
        return self.a + self.b + self.c
