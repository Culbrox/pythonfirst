temperatura = float(input("Ingrese temperatura:"))

escala = input("es Fahrenheit(F) o celcius(C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)
else :
    print("escala incorrecta")





#def celcius_a_fahrenheit():
#    if escala == "f":
#        celsius = (temperatura - 32) * 5/9
#def fahrenheit_a_celcius():
#    if escala == "c":
#        fahrenheit = temperatura * 1.8 + 32

#            if escala == "f":
#   celsius = (temperatura - 32) * 5/9
#  print(celsius)
# if escala == "c":
#        fahrenheit = temperatura * 1.8 + 32
#    print(fahrenheit)

        #if = si
        #elif = else if = sino
        #else = alternativamente