#%%
from matplotlib.hatch import SouthEastHatch
from classes import Restaurant, User, Delivery

name = User("carlos")

nombre = name.login()

##domicilio = Delivery()

##domicilio.precio_dom()

prueba = Delivery()
hola =prueba.hallar_dist(6.33607, -75.56119,6.17136,-75.58825)
print(hola)


print("Bienvenido a la Chuzona señor(a) " + nombre[0])

xd = {
        "1": ["Mazorca desgranada", 14000, 
        "Mazorca americana desgranada,queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "2": ["Desgranado de carne", 18000, 
        "Carne de res, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "3": ["Desgranado de pollo", 18000, 
        "Pechuga de pollo, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "4": ["Desgranado mixto", 18000, 
        "Carne de res y pollo, acompañadas de bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "5": ["Desgranado combinado", 21000, 
        "Butifarra, chorizo, carne de res, pollo,lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "6": ["Desgranado ranchero especial", 22000, 
        "Salchicha Ranchera, pollo, mazorca, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "7": ["Desgranado suizo especial", 24000, 
        "Salchiza Suiza, Pollo, mazorca, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "8": ["Desgranado de la casa", 28000, 
        "Salchicha Ranchera, butifarra, pollo, carne de res, mazorca, tocineta, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "9": ["Desgranado especial de la costa", 24000, 
        "Butifarra, chorizo, carne de res, pollo, mazorca, tocineta, bollo limpio, lechuga, queso costeño rayado y papitas paja acompañado con salsa tártara."], 
        "10": ["Mazorca desgranada especial", 16000, 
        "Mazorca americana desgranada, trozos de tocineta, queso costeño rayado y papitas paja acompañado con salsa tártara."]
    }

a = Restaurant(xd)
a.pedir(hola)

# %%

