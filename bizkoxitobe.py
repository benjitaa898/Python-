#crear un programa que ingrese cantidad de notas por cada alumno 
#ingresar la cantidad de alumnos del curso
#calcular promedio de cada niño
#nombre
#genero
#notas (nota1, nota2, nota3 )
#calcular cuantas mujeres hay en el curso 
#calcular el promedio de los hambres 
def promedio(a,b,c):
      prom = (a + b + c)/3
      return prom

def validar_genero(genero)
      generos_validados = ["masculino", "femenino"]
      genero = genero.lower() 
      if genero in generos_validados:
            return True
      else:
            return  False
print ("bienvenido a python") 
print("")

con_fem = 0
con_mas = 0
ca = int(input("ingrese cantidad de alumnos"))
for i in range(0, ca, 1)
      # ingreso de datos
      nombre = input("ingrese nombre del alumno ")
      M: masculino
      F: femenino
      genero = input("ingrese genero del alumno")
      print("ingrese notas")
      nota1 = float(input("NOTA 1: "))
      nota2 = float(input("NOTA 2: "))
      nota3 = float(input("NOTA 3: "))
      

if(genero=="Femenino")
      con_fem = con_fem + 1
      print("es mujer")
else:
      con_mas = con_mas + 1
      print("es hombre")

      pro=promedio(nota1, nota2, nota3)
      print("el promedio del alumno es", pro)
     
print("el promedio de los alumons es", pro)