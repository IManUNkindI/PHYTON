from tkinter import *
# Funciones
def centrar_ventana(ventana):  # Centrar la ventana y ajustar tamaño respecto a frames
    ventana.update_idletasks()
    ancho_ventana = (frame1.winfo_width() + frame2.winfo_width())
    alto_ventana = frame1.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))

def getNombre():  # Obtener texto de Ctext1 mediante Btn1
    texto = Ctext1.get()
    if(texto==""):
        Label3.config(text="Ingrese su nombre")
        Label3.config(fg="red")
    else:
        Label3.config(text=texto)
        Label3.config(fg="black")
    centrar_ventana(ventana)

def getApellido():  # Obtener texto de Ctext2 medianto Btn2
    texto = Ctext2.get()
    if(texto==""):
        Label4.config(text="Ingrese su apellido")
        Label4.config(fg="red")
    else:
        Label4.config(text=texto)
        Label4.config(fg="black")
    centrar_ventana(ventana)

# Crear una ventana
ventana = Tk()
ventana.title("Nombre y Apellido")
ventana.iconbitmap("Kirby.ico")
ventana.resizable(False,False)

#Ubicacion mediante .grid()
# NW    N   NW
# W         E
# SW    S   SE
# (row, coumn, sticky, padx, pady)

# Crear dos frames
# (Contenedor, ancho del borde, relieve)
frame1 = Frame(ventana, borderwidth=2, relief="ridge")
frame2 = Frame(ventana, borderwidth=2, relief="ridge")
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

# Agregar widgets a los frames
# (Contenedor, ancho del borde, texto) 
# sticky(ubicacion en casilla).grid
Label1=Label(frame1, borderwidth=2, text="Nombre:")
Label2=Label(frame1, borderwidth=2, text="Apellido:")
Label3=Label(frame2, borderwidth=2, text="Ingrese su nombre")
Label4=Label(frame2, borderwidth=2, text="Ingrese su apellido")

Label1.grid(row=0, column=0, padx=5, pady=7)
Label2.grid(row=1, column=0, padx=5, pady=7)
Label3.grid(row=0, column=2, padx=5, pady=5)
Label4.grid(row=1, column=2, padx=5, pady=5)

Ctext1=Entry(frame2, borderwidth=2)
Ctext2=Entry(frame2, borderwidth=2)

Ctext1.grid(row=0, column=0, padx=5, pady=5)
Ctext2.grid(row=1, column=0, padx=5, pady=5)

# (Contenedor, ancho del borde, texto, command(funcion a ejecutar))
Btn1=Button(frame2, borderwidth=2, text="Aceptar", command=getNombre)
Btn2=Button(frame2, borderwidth=2, text="Aceptar", command=getApellido)

Btn1.grid(row=0, column=1, padx=5, pady=5)
Btn2.grid(row=1, column=1, padx=5, pady=5)

# Centrar la ventana en la pantalla
centrar_ventana(ventana)
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
