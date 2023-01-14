def dimensoes(matriz):
    return(str(len(matriz))+'X'+str(len(matriz[0])))

def soma_matrizes(m1, m2):

    if dimensoes(m1) != dimensoes(m2):
        return False

    m3=[]

    for i in range(len(m1)):
        row=[]
        
        for ii in range(len(m1[0])):
            row.append(m1[i][ii] + m2[i][ii])

        m3.append(row)

    return m3
