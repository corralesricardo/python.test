###Funcion
def saludo(mensaje):
    print ('#hola')
    print(mensaje)
#######################
pesos = input("¿Cuantos pesos Argentinos tienes? ")
pesos = float(pesos)
valor_dolar = 190
dolares = pesos / valor_dolar
dolares = str(dolares)
print("Tienes $" + dolares+" dolares.")

dolares = float(dolares)
if dolares > 1000:
    saludo("#mayorMil")
    print("Tenes mas de Mil dolares!!!")
elif dolares == 1000:
    saludo("#justoMIL")
    print("Tenes Justo Mil dolares!!!")
else:
    saludo("#MenorMil")
    print("Tenes menos de Mil dolares!!!")

print("SALI?")
print('Saliendo')
#######################