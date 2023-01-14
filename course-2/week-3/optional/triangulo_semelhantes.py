class Triangulo:
    
    def __init__(self, a, b, c):
        
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def semelhantes(self, T):

        if (simplify(self.a,
                     self.b,
                     self.c)==
            simplify(T.a,
                     T.b,
                     T.c)):

            return True

        return False

def simplify(a, b, c):
    
    bigSide = a

    if bigSide < b: bigSide = b

    if bigSide < c: bigSide = c
        
    for divider in range(bigSide + 1):
        
        if divider > 1:

            stop = False

            while stop == False:

                divA = a / divider
                divB = b / divider
                divC = c / divider
                

                if (a // divider == divA and
                    b // divider == divB and
                    c // divider == divC):

                    a = int(divA)
                    b = int(divB)
                    c = int(divC)
                    
                else: stop = True

    return a, b, c
