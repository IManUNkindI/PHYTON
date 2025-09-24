# GUI
# Metdod .config() aplica para Frame y Raiz

# Importar libreria
from tkinter import *

# Declarar el objeto de la ventana
raiz = Tk()

# Titulo de la ventana
raiz.title("Ventana de Pruebas")

# Tamaño definido y posicion en monitor
raiz.resizable(False,False)

# Tamaño definido
raiz.geometry("1200x600+70+65")

# Color de fondo bg (background)
raiz.config(bg = "pink")

# Definir icono de la ventana
raiz.iconbitmap("Kirby.ico")

# Creacion de un Frame
n1Frame = Frame(raiz,width=900,height=600,bg="white")

# Posicion side (dreccion), anchor (cardinales)
# Rellenado fill (x), expand(true)(y)... fill="both"(x,y)
n1Frame.pack()

# Parametros esteticos del frame
n1Frame.config(bd = 10)
n1Frame.config(relief = "groove")
n1Frame.config(cursor = "hand1")

# Label (variable = Label(Contenedor, Parametros)
# .place(), no .pack()
imagen = PhotoImage(file = "KIRBY.png")

Label1 = Label(n1Frame)
Label1.place(x = 400, y = 5)
Label1.config(bg = "white")
Label1.config(text = "Hola Mundo:")

Label2 = Label(n1Frame, image = imagen)
Label2.place(x = 175, y = 50)

# Entry (Cuadro de texto)
#(variable = Entry(Contenedor, Parametros) 
CTexto = Entry(n1Frame)

# grid(), tabla de ubicacion
CTexto.place(x = 10, y = 50)

# Ejecucion constante de la interfaz
raiz.mainloop()
