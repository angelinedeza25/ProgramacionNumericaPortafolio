import tkinter as tk

def analizar():
    funcion = entrada.get()

    if funcion == "":
        resultado["texto"] = "Agregar función: "
        return
    letters = ""
    cant_letters = 0
    operaciones = 0
    for i in range(len(funcion)):
        c = funcion[i]
        if c.isalpha() and c not in letters:
            letters += c
            cant_letters += 1
        if c in "+-*/^":
            operaciones += 1
        if i < len(funcion) - 1:
            sig = funcion[i + 1]
            if (c.isdigit() and sig.isalpha()) or (c.isalpha() and sig.isalpha()):
                operaciones += 1

    resultado["texto"] = "Variables: " + letters + "\nCantidad: " + str(cant_letters) + "\nOperaciones: " + str(operaciones)

ventana = tk.Tk()
ventana.title("Analizador")
ventana.geometry("300x250")
tk.Label(ventana, text="Ingresa una función:").pack()
entrada = tk.Entry(ventana)
entrada.pack(pady=5)
boton = tk.Button(ventana, text="Analizar", command=analizar)
boton.pack(pady=5)
resultado = tk.Label(ventana, text="", bg="lightgray", width=30, height=6, anchor="w", justify="left")
resultado.pack(pady=10)
ventana.mainloop()