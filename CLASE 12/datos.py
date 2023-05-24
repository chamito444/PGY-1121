#EJEMPLO DE USP GITHUB
print("INGRESO DE DATOS")
print("-----------------------------------")
nombre = input("Ingrese su nombre -> ")
while True:
 try:
  edad = int(input("Ingrese su edad -> "))
  break
 except:
  print("Ingreso de edad erroneo")
print("-----------------------------------")
print(f"Su nombre es -> {nombre}")
print(f"Su edad es -> {edad}")
print("PROGRAMA FINALIZADO 🤐") 
