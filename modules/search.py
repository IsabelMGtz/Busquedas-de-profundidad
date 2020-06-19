#Creamos el diccionario con las relaciones

ciudades = {
    'P': ['Tc','Tz','V'],
    'Tz': ['P','X'],
    'Tc': ['P','V'],
    'V': ['P','Tc','X','Z'],
    'X': ['Tz','V','Z','B','H'],
    'Z': ['V','X','B'],
    'H': ['X','F'],
    'B': ['Z','X','J','A'],
    'F': ['H','Y','HJ'],
    'C': ['S','M'],
    'Y':['F', 'J'],
    'J':['Y','B','O'],
    'A':['B','O','S'],
    'HJ':['F','O'],
    'O':['HJ','J','A','N'],
    'N':['O','Ac'],
    'Ac':['N','S','M'],
    'S':['A','Ac','C'],
    'M':['Ac','C'],
    'AD':'C'}
