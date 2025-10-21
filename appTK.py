import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora Gráfica")
ventana.geometry("350x300")
ventana.config(bg="#e3f2fd")

titulo = tk.Label(ventana, text="Calculadora Básica", font=("Arial", 16, "bold"), bg="#e3f2fd")
titulo.pack(pady=10)

tk.Label(ventana, text="Número 1:", bg="#e3f2fd").pack()
entrada1 = tk.Entry(ventana, width=15, font=("Arial", 12))
entrada1.pack(pady=5)

tk.Label(ventana, text="Número 2:", bg="#e3f2fd").pack()
entrada2 = tk.Entry(ventana, width=15, font=("Arial", 12))
entrada2.pack(pady=5)

def operar(op):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if op == "sumar":
            resultado = num1 + num2
        elif op == "restar":
            resultado = num1 - num2
        elif op == "multiplicar":
            resultado = num1 * num2
        elif op == "dividir":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado = num1 / num2
        etiqueta_resultado.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

frame_botones = tk.Frame(ventana, bg="#e3f2fd")
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="+", width=6, command=lambda: operar("sumar")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="-", width=6, command=lambda: operar("restar")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="×", width=6, command=lambda: operar("multiplicar")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="÷", width=6, command=lambda: operar("dividir")).grid(row=1, column=1, padx=5, pady=5)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14), bg="#e3f2fd", fg="blue")
etiqueta_resultado.pack(pady=15)

tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#f44336", fg="white").pack(pady=5)

ventana.mainloop()
