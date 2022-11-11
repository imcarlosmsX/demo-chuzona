#%%
from classes import Restaurant, User, Delivery
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import json


name = User("carlos")

nombre = name.login()

direccion_destino = input("ingrese la direccion que desea:          ")


df = pd.DataFrame({'direcc':
            [direccion_destino + ", Barranquilla, Atlantico"]})

geolocartor = Nominatim(user_agent = "chuzona")
geocode = RateLimiter(geolocartor.geocode, min_delay_seconds = 1)

df["location"] = df["direcc"].apply(geocode)
df["coordenadas"] = df["location"].apply(lambda x: (x.latitude, x.longitude))

coord = df["coordenadas"]



precio_domi= Delivery()

domicilio = precio_domi.hallar_dist(coord[0][0], coord[0][1])


print("Bienvenido a la Chuzona señor(a) " + nombre)
with open("menu.json") as menu:
    listado = json.load(menu)
    a = Restaurant(listado)
    a.pedir(domicilio, nombre, direccion_destino)

    ##file = open("info_clientes.txt", "w")
    ##file.write( str (nombre) + "," + str (temp_info[0]) + ", " + str (temp_info[1] + domicilio) + "," + str(direccion_destino) + "\n")


# %%
