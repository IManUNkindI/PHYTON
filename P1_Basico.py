# No es necesario declarar tipo de variable
# No es necesario ":" al final de cada linea
# El archivo guardado debe tener extension .py
# Se concatenan variables de diferente tipo para mostrar con ","
# Si esta instalado python solo se necesita block de notas y consola de comandos


print("Sumando 2 + 4");
n1 = 2;
n2 = 4;
resultado = n1 + n2;
print("El Resultado es: " , resultado);


# Al igualar una variable se reasigna el valor de esta eliminando lo que contenga
# Para agragar informacion auna variable se puede usar el operador "+="
# Si las variable a concatenar son del mismo tipo solo es necesario llamar la variable  + la siguiente
# variable
# .find(), esta funcion busca la posicion donde se encuentra la cadena de caracteres desada
# Extraer, para extraer la linea de caracteres desada se llama la variable y se le indica las posiciones
# entre las que se encuentra la cadena de caracteres de interes
# El segmento a extraer se indica de la siguiente manera: ['posicion inicial'int:'posicion siguiente al
# ultimo caracter desado'int]
# Comparacion, en esta funcion retornara un valor booleano imperso en pantalla, no es necesario guardar
# la comparacion


txt = "Hola";
txt += " ";
txt += "Andrés";
print(txt);

posFname = txt.find("Andrés");
name = " Felipe";
print("La posision donde inicia la cadea buscada es: " , posFname);

firstname = txt[5:11];
print(firstname + name);

print(firstname == name);


# Palabras reservadas: and, del, for, is, raise, assert, if, else, elif, from, lambda, return, break,
# global, not, try, class, except, or, while, continue, exec, import, yield, def, finally, in, print.
