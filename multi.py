from sympy import symbols, expand

def multiplicar_monomios(expr1, expr2):
    resultado = expand(expr1 * expr2)
    return resultado

# Definir la variable simbólica x
x = symbols('x')

# Pedir al usuario las expresiones para los monomios y multiplicarlos
expresiones = input("Ingresa los monomios separados por espacios (ejemplo: (x+1) (x+2) ...): ")
monomios = [eval(expr) for expr in expresiones.split()]

# Calcular la multiplicación de los monomios
resultado = monomios[0]
for i in range(1, len(monomios)):
    resultado = multiplicar_monomios(resultado, monomios[i])

# Mostrar el resultado
print("El resultado es:")
print(resultado)
