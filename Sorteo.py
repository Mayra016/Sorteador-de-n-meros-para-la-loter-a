import random
numeros = []

def generar():
    global numeros
    i = 1
    while i <= 6:
        num = random.randrange(1, 60)
        numeros.append(num)
        i = i + 1
    return quitarRepetidos()
    
def quitarRepetidos():
    global numeros
    numeros = set(numeros)
    print(numeros)
    while len(numeros) != 6:
        repetidos = 6 - len(numeros)
        i = 1
        while i <= repetidos:
            num = random.randrange(1, 60)
            numeros.add(num)
            i = i + 1
            print(numeros)
        numeros = set(numeros)
    return numeros      
            
print(generar())    
