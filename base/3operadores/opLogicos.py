# AND los 2 deven ser true si uno es falso todo es falso

Resultado = True & True  # Devolver True
Resultado2 = False & True  # Devolver Falso
Resultado3 = True & False  # Devolver Falso
Resultado4 = False & False  # Devolver Falso

# OR devulve falso si ninguna se cumple

Resultado5 = True | True  # Devolver True
Resultado6 = False | True  # Devolver True
Resultado7 = True | False  # Devolver True
Resultado8 = False | False  # Devolver Falso

# NOT nos inverte el valor si le damos un true nos da un true

Resultado9 = not True  # Devolver Falso
Resultado10 = not False  # Devolver True

print(Resultado9)
