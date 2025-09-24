# Matematicas: Suma, resta, multiplicacion, division, modulo, exponencial
#               +  ,   -  ,       *       , / ,  // ,   %   ,     **     .
# Asignacion:= ,+= ,  -=  ,      *=       , /=, //= ,  %=   ,     **=    . a
# Basicamente opera lo que contenga la variable con el valor proporcionado despues de la asigncaion

# Comparar: < , > , == , != , <= , >=
# Logica: and, or, not

"""
Tipos de datos:
    Enteros (int , long) = 10
    Flotantes (float) = 10.123
    Numeros Complejos (complex) = 5 + 6i
    Cadenas (String) = "Andrés"
    Booleano (bool) = True False
"""

n1 = int(input("Numero 1: "));
n2 = int(input("Numero 2: "));

m = n1*n2;
d = n1/n2;
p = n2**n1;

print("\nSuma:" , n1+n2);

# La instruccion contenida en una fucnion se indica con ":", y todo lo que tenga una tabulacion
# inicial al comienzo de la linea se considerara como instruccion de la condicion, esto aplica para
# funciones como: if, else, elif, while
# Ademas, no es necesario que la condicion este en parentesis

if(n1>=n2):
    print("Resta: ", n1-n2);
else:
    print("Resta: ", n2-n1);

print("Multiplicacion:" , m, type(m));
print("Division:" , d, type(d));

# Potencia (numero ** potencia)
print("Potencia n2^n1", p, type(p));
# Division entera (aproxima a la parte entera del numero)
print("Divison entera:" , n1//n2);
# Modulo
print("Modulo:" , n1%n2);


# Saltos de linea encasillando en comillas triples ("""Texto1""" """Texto2""")
print("""Texto1
Texto2
Texto3""");

# Para evitar saltos de linea, se usa el parametro end en la funcion print, asignando una cadena al
# parametro
print("Hola", end=", ");
print("Andrés");

# Para separar cadenas concatenadas mediante comas, se usa el parametro sep, asignando el formato de
# separacion entre las cadenas

print("1","2","3","4","5",sep=":")

fibo = 0;
suma = 1
while(fibo<1597):
    print(fibo, suma,sep=",", end=",");
    fibo += suma
    suma += fibo

