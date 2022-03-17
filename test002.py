
nombre = input("¿cual es tu nombre: ")

#mayuscula
nom=nombre.upper()
print(nom)
#primera letra en mayuscula
nom=nombre.capitalize()
print(nom)
#minuscula
nom=nombre.lower()
print(nom)
#borra caracteres en balanco
nom = nombre.strip()
print(nom)

#reemplaza carater a por 1
nom=nombre.replace('a','1')
print(nom)
print("primer caracter es: "+nombre[0])
print("cant caracter es: " + str(len(nombre))) 
print("original: " + nombre)
