s=int(input('Por favor, entre com o número de segundos que deseja converter: '))
m=0
h=0
d=0
while s>= 86400:
    s=s-86400
    d=d+1
while s>=3600:
    s=s-3600
    h=h+1
while s>=60:
    s=s-60
    m=m+1
print(d,'dias,',h,'horas,',m,'minutos e',s,'segundos.')
