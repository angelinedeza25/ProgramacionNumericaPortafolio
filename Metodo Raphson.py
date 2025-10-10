class MetodoRaphson:
    def __init__(self, funcion_str, valor_inicial, tolerancia, iteraciones_max):
        self.funcion_str = funcion_str
        self.valor_actual = valor_inicial
        self.tolerancia = tolerancia
        self.iteraciones_max = iteraciones_max

    def funcion(self, valor_x):
        return eval(self.funcion_str)

    def derivada(self, valor_x):
        incremento = 1e-6
        return (self.funcion(valor_x + incremento) - self.funcion(valor_x - incremento)) / (2 * incremento)

    def calcular_raiz(self):
        for contador in range(self.iteraciones_max):
            valor_funcion = self.funcion(self.valor_actual)
            valor_derivada = self.derivada(self.valor_actual)

            if valor_derivada == 0:
                break

            nuevo_valor = self.valor_actual - valor_funcion / valor_derivada
            print(f"Iteración {contador + 1}: x = {nuevo_valor:.6f}, f(x) = {valor_funcion:.6f}")

            if abs(nuevo_valor - self.valor_actual) < self.tolerancia:
                print(f"\nRaíz aproximada ≈ {nuevo_valor:.6f}")
                return

            self.valor_actual = nuevo_valor

        print("\nEl método no converge")

funcion_ingresada = input("f(x): ")
valor_inicial = float(input("x0: "))
tolerancia = float(input("tolerancia: "))
iteraciones_max = int(input("iteraciones: "))

MetodoRaphson(funcion_ingresada, valor_inicial, tolerancia, iteraciones_max).calcular_raiz()