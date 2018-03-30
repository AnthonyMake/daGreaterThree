import random

numGreat = [0,0,0]
arrayLen = 0

print("Hola, voy a encontrar los 3 datos mayores dentro de un Array.")

while arrayLen < 3:
    arrayLen = int(input("\nArmemos el Listado,\nCuentame de cuantos datos quieres que sea:"))
    print("\nNo se Puede!! tiene que ser un número menor que tres!!")

array = random.sample(range(100),arrayLen)

print("\nEste es el array:")
print(array)
print("\nY sus 3 números mayores son:")

for i in range(len(array)):

    if array[i] > numGreat[0]:

        numGreat[2] = numGreat[1]
        numGreat[1] = numGreat[0]
        numGreat[0] = array[i]

    elif array[i] > numGreat[1]:

        numGreat[2] = numGreat[1]
        numGreat[1] = array[i]

    elif array[i] > numGreat[2]:

        numGreat[2] = array[i]

print(numGreat)
print("\n...TaDaa ¯\_(ツ)_/¯")