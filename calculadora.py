# Importar el módulo tkinter
from tkinter import*

# Crear una ventana
ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('250x300')


# Crear tres campos de texto con sus labels para ingresar y mostrar los números y el resultado
label_1 = Label(ventana, text='Número 1:')
label_1.grid(row=1, column=1)

numero_1 = Entry(ventana)
numero_1.grid(row=2, column=1)

label_2 = Label(ventana, text='Número 2:')
label_2.grid(row=3, column=1)

numero_2 = Entry(ventana)
numero_2.grid(row=4, column=1)

label_3 = Label(ventana, text='Resultado:')
label_3.grid(row=5, column=1)

resultado = Entry(ventana)
resultado.grid(row=6, column=1)

# Crear una función para calcular la suma, resta, multiplicacion y division de los números y borrar e igual y mostrarla en el campo del resultado
def sumar():
  try:
    n1 = float(numero_1.get())
    n2 = float(numero_2.get())
    res = n1 + n2
    resultado.delete(0, END)
    resultado.insert(0, res)
  except:
    resultado.delete(0, END)
    resultado.insert(0, 'Error')

def restar():
  try:
    n1 = float(numero_1.get())
    n2 = float(numero_2.get())
    res = n1 - n2
    resultado.delete(0, END)
    resultado.insert(0, res)
  except:
    resultado.delete(0, END)
    resultado.insert(0, 'Error')

def multiplicar():
  try:
    n1 = float(numero_1.get())
    n2 = float(numero_2.get())
    res = n1 * n2
    resultado.delete(0, END)
    resultado.insert(0, res)
  except:
    resultado.delete(0, END)
    resultado.insert(0, 'Error')

def division():
  try:
    n1 = float(numero_1.get())
    n2 = float(numero_2.get())
    res = n1 / n2
    resultado.delete(0, END)
    resultado.insert(0, res)
  except:
    resultado.delete(0, END)
    resultado.insert(0, 'Error')

def borrar():
    numero_1.delete(0, END)
    numero_2.delete(0, END)
    resultado.delete(0, END)



# Crear un botón para llamar a la función sumar
boton = Button(ventana, text='Sumar', command=sumar)
boton.grid(row=8, column=0)

# Crear un botón para llamar a la función restar
boton = Button(ventana, text='restar', command=restar)
boton.grid(row=8, column=1)

# Crear un botón para llamar a la función multiplicar
boton = Button(ventana, text='multiplicar', command=multiplicar)
boton.grid(row=8, column=2)

# Crear un botón para llamar a la función division
boton = Button(ventana, text='division', command=division)
boton.grid(row=9, column=0)

# Crear un botón para llamar a la función borrar
boton = Button(ventana, text="C", command=borrar)
boton.grid(row=9, column=1)

# Crear un botón para llamar a la función igual
boton = Button(ventana, text ="=")
boton.grid(row=9, column=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()