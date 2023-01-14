class Triangulo:
    
    def __init__(self, a, b, c):
        
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def tipo_lado(self):

        if self.a == self.b == self.c:
            
            return 'equilátero'
        
        if (self.a == self.b or
            self.a == self.c or
            self.b == self.c):

            return 'isósceles'

        if (self.a != self.b or
            self.a != self.c or
            self.b != self.c):

            return 'escaleno'
