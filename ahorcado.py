import time
nombre=input("¿introduce tu nombre?:")
print(" hola " + nombre," ah jugar al ahorcado!!")
print("")
time.sleep(1)
print("comienza a adivinar!:")
time.sleep(0.1)
palabra= "argentina"
tuPalabra=""
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tuPalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
        if fallas==0:
            print(" ganaste!")
            break

        tuletra=input("introduce una letra : ")
        tuPalabra+=tuletra
        if tuletra not in tuPalabra :
            vidas-=1
            print ("incorrecto")
            print("tu tienes" + vidas, "vidas")
        if vidas == 0:
                print("perdiste")
        else:
                print("gracias por participar")
