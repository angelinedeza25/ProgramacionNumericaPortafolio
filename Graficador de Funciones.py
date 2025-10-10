def limpiar(txt):
    txt = txt.replace(" ", "")
    txt = txt.replace("^", "**")
    txt = txt.replace("-x", "-1*x").replace("+x", "+1*x")
    if txt[:1] == "x":
        txt = "1*" + txt
    txt = txt.replace("x", "*x").replace("**x", "*x")
    return txt

def f_val(exp, x):
    try:
        return eval(exp, {"x": x, "__builtins__": {}})
    except:
        return None

def graficar(fa, fb, rx=(-15, 15), ry=(-10, 10)):
    x0, x1 = rx
    y0, y1 = ry
    print("\n=== GRÁFICO EN CONSOLA ===\n")

    for y in range(y1, y0 - 1, -1):
        fila = ""
        for x in range(x0, x1 + 1):
            ya = f_val(fa, x)
            yb = f_val(fb, x)

            ta = ya is not None and abs(ya - y) < 0.5
            tb = yb is not None and abs(yb - y) < 0.5

            if ta and tb:
                fila += "#"
            elif ta:
                fila += "*"
            elif tb:
                fila += "o"
            elif x == 0 and y == 0:
                fila += "+"
            elif x == 0:
                fila += "|"
            elif y == 0:
                fila += "-"
            else:
                fila += " "
        print(fila)

    print("\n[ LEYENDA ]")
    print(" * = Función 1")
    print(" o = Función 2")
    print(" # = Intersección")
    print(" | = Eje Y")
    print(" - = Eje X")
    print(" + = Origen (0,0)\n")

def run():
    print("PROGRAMA GRAFICADOR")
    print("=====================\n")

    f1 = input("Función 1 (ejemplo: 2x+1): ")
    f2 = input("Función 2 (ejemplo: -x+3): ")

    f1 = limpiar(f1)
    f2 = limpiar(f2)

    graficar(f1, f2)

if __name__ == "__main__":
    run()